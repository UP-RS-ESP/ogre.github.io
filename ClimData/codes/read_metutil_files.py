#!/usr/bin/env python

import pandas as pd
import numpy as np
import glob, tqdm, os, re, sys


def ITRF_XYZ_to_WGS84(x, y, z):
    a = 6378137.0  # in meters
    b = 6356752.314245  # in meters
    f = (a - b) / a
    f_inv = 1.0 / f
    e_sq = f * (2 - f)
    eps = e_sq / (1.0 - e_sq)
    p = np.sqrt(x * x + y * y)
    q = np.arctan2((z * a), (p * b))
    sin_q = np.sin(q)
    cos_q = np.cos(q)
    sin_q_3 = sin_q * sin_q * sin_q
    cos_q_3 = cos_q * cos_q * cos_q
    phi = np.arctan2((z + eps * b * sin_q_3), (p - e_sq * a * cos_q_3))
    lam = np.arctan2(y, x)
    v = a / np.sqrt(1.0 - e_sq * np.sin(phi) * np.sin(phi))
    h = (p / np.cos(phi)) - v
    lat = np.degrees(phi)
    lon = np.degrees(lam)
    return lon, lat, h


if __name__ == "__main__":
    lfile_fn = sys.argv[1]
    met_file_dir = sys.argv[2]
    outfile_fn = sys.argv[3]

    # lfile_fn = os.path.join("2023", "lfile.")
    # met_file_dir = "2023/G"
    # outfile_fn = "Nepal_2023_G"
    met_files = glob.glob(os.path.join(met_file_dir, "met_*.*"))
    met_files.sort()

    # find unique site names:
    met_stations = []
    for i in range(len(met_files)):
        cname = os.path.basename(met_files[i])
        met_stations.append(cname[4:8])
    met_stations = np.unique(met_stations)

    all_stations = []
    for i in tqdm.tqdm(range(len(met_stations)), desc="Reading Files"):
        cmet_station = str(met_stations[i])
        station_met_files = glob.glob(
            os.path.join(met_file_dir, "met_%s.*" % cmet_station)
        )

        dfs = []
        for name in station_met_files:
            df = pd.read_csv(
                name,
                skipinitialspace=True,
                skiprows=4,
                skip_blank_lines=True,
                sep=r"\s+",
                names=[
                    "Yr",
                    "Doy",
                    "Hr",
                    "Mn",
                    "Sec",
                    "Total_Zen",
                    "Wet_Zen",
                    "Sig_Zen",
                    "PW",
                    "Sig_PW",
                    "Press",
                    "Temp",
                    "ZHD",
                    "Grad_NS",
                    "Sig_NS.1",
                    "Grad_EW",
                    "Sig_EW",
                ],
            )
            df["datetime"] = (
                pd.to_datetime(df["Yr"] * 1000 + df["Doy"], format="%Y%j", utc=True)
                + pd.to_timedelta(df["Hr"], unit="h")
                + pd.to_timedelta(df["Mn"], unit="m")
                + pd.to_timedelta(df["Sec"], unit="s")
            )
            df.drop(columns=["Hr", "Mn", "Sec"], inplace=True)
            dfs.append(df)

        df_all = pd.concat(dfs, ignore_index=True)
        df_all.set_index("datetime", inplace=True)
        df_all.sort_index(ascending=True, inplace=True)

        with open(station_met_files[0]) as f:
            first_line = f.readline().strip("\n")
        station_name = first_line[35:39]
        station_elevation = float(first_line.split(":")[1].split("+")[0])
        station_elevation_pm = float(first_line.split(":")[1].split("+")[1][3:-2])
        df_all["Name"] = station_name
        df_all["Elevation_m"] = station_elevation
        df_all["Elevation_pm_m"] = station_elevation_pm

        regexp = station_name
        x_set = 0
        y_set = 0
        z_set = 0
        find0 = 0
        with open(lfile_fn) as file:
            for line in file:
                if find0 == 0 and re.search(regexp, line):
                    split_string = str(line).split(" ")
                    for j in range(2, len(split_string)):
                        if split_string[j] == "":
                            continue
                        elif x_set == 0:
                            x = float(split_string[j])
                            x_set = 1
                        elif x_set == 1 and y_set == 0:
                            y = float(split_string[j])
                            y_set = 1
                        elif x_set == 1 and y_set == 1:
                            z = float(split_string[j])
                            z_set = 1
                            lon, lat, h = ITRF_XYZ_to_WGS84(x, y, z)
                            df_all["lon"] = lon
                            df_all["lat"] = lat
                            df_all["h"] = h
                            break
                    find0 = 1
        all_stations.append(df_all)

    df_all_stations = pd.concat(all_stations)
    df_all_stations.sort_index(ascending=True, inplace=True)

    df_all_stations.to_csv(outfile_fn + "_all_stations.csv.bz2")
    # df_all_stations.to_hdf(outfile_fn + "_all_stations.hdf", key="metutil")
    df_all_stations_mean = df_all_stations.groupby("Name").mean()
    df_all_stations_mean.to_csv(outfile_fn + "_all_stations_mean.csv")
