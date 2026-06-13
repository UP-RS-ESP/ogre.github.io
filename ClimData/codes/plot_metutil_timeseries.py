#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import AutoDateLocator
import matplotlib.dates as mdates
from dateutil.tz import gettz

plt.rcParams["axes.facecolor"] = "#eeeeee"
plt.rcParams["figure.facecolor"] = "#eeeeee"


def gnss_zwd_to_pw(zwd, T_s=None, T_m=None):
    """
    Converts GNSS Zenith Wet Delay (ZWD) to Precipitable Water (PW) in mm.

    Parameters:
    -----------
    zwd : float or numpy array
        Zenith Wet Delay in millimeters (mm).
    T_s : float or numpy array, optional
        Surface temperature in Kelvin (K). Used to estimate T_m if T_m is not provided.
    T_m : float or numpy array, optional
        Weighted mean temperature of the atmosphere in Kelvin (K).

    Returns:
    --------
    pw : float or numpy array
        Precipitable Water in millimeters (mm).
    """
    # Physical Constants
    rv = 461.525  # Specific gas constant for water vapor (J/(kg·K))
    rho_w = 1000.0  # Density of liquid water (kg/m^3)

    # Refractivity constants (Bevis et al., 1994 / Davis et al., 1985)
    k2_prime = 22.1  # K/hPa
    k3 = 373900.0  # K^2/hPa

    # 1. Determine T_m (Weighted Mean Temperature)
    if T_m is None:
        if T_s is None:
            raise ValueError(
                "You must provide either T_m or T_s to calculate the conversion factor."
            )

        # If T_s is given in Celsius (e.g., < 100), convert it to Kelvin
        if np.any(T_s < 100):
            T_s = T_s + 273.15

        # Bevis linear regression formula: T_m = 70.2 + 0.72 * T_s
        T_m = 70.2 + (0.72 * T_s)
    else:
        # If T_m is given in Celsius, convert to Kelvin
        if np.any(T_m < 100):
            T_m = T_m + 273.15

    # 2. Calculate the dimensionless conversion factor (Pi)
    # Note: k2_prime and k3 use hPa, so we scale appropriately in the SI system
    factor_denominator = rho_w * rv * ((k3 / T_m) + k2_prime) * 1e-6
    pi = 1.0 / factor_denominator

    # 3. Calculate Precipitable Water
    pw = pi * zwd

    return pw


def plot_Wet_Zen(df_single_station, df_single_station_msk, pngfname):
    fg, ax = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(12, 10),
        dpi=300,
        layout="constrained",
        sharex=False,
    )
    # PLOT 0
    ax[0].errorbar(
        x=df_single_station_msk.index,
        y=df_single_station_msk["Wet_Zen"],
        yerr=df_single_station_msk["Sig_Zen"],
        linestyle="-",
        marker="o",
        ms=1,
        lw=0.5,
        color="navy",
        label="Zenith Wet Delay",
    )
    # ax0b = ax[0].twinx()
    # ax[0].errorbar(
    #     x=df_single_station_msk.index,
    #     y=df_single_station_msk["PW_local"],
    #     yerr=df_single_station_msk["Sig_PW_local"],
    #     linestyle="",
    #     lw=0.5,
    #     color="lightblue",
    #     label="Precipitable Water",
    # )
    ax[0].grid()
    ax[0].set_ylabel(r"Zenith Wet Delay (mm)", fontsize=14, fontweight="bold")
    ax[0].legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax[0].xaxis.set_major_formatter(date_form)
    ax[0].xaxis.set_major_locator(mdates.HourLocator(interval=24))
    ax[0].xaxis.set_minor_locator(mdates.HourLocator(interval=12))
    ax[0].set_xlim([start_time, end_time])
    ax[0].set_ylim([0, 400])
    # PLOT 1
    ax[1].plot(
        df_single_station.index,
        df_single_station["Wet_Zen"],
        linestyle="",
        marker="o",
        ms=0.2,
        lw=0.5,
        color="navy",
        label="Zenith Wet Delay",
    )
    ax[1].plot(
        df_single_station.index,
        df_single_station["Wet_Zen_12h_rollingmean"],
        linestyle="-",
        marker="",
        lw=0.5,
        color="navy",
        label="Zenith Wet Delay 12-hour rolling mean",
    )
    ax[1].set_ylim([0, 400])
    # ax1b = ax[1].twinx()
    ax[1].grid()
    ax[1].legend(prop={"size": 14})
    ax[1].set_ylabel(r"Zenith Wet Delay (mm)", fontsize=14, fontweight="bold")
    date_form = DateFormatter("%Y-%b")
    date_form.set_tzinfo(gettz("GMT"))
    ax[1].xaxis.set_major_formatter(date_form)
    ax[1].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax[1].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
    fg.suptitle(
        "%s: Zenith Wet Delay" % station_name,
        fontsize=16,
        fontweight="bold",
    )
    fg.savefig(pngfname, dpi=300)
    plt.close(fg)


def plot_PW(df_single_station, df_single_station_msk, pngfname):
    fg, ax = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(12, 10),
        dpi=300,
        layout="constrained",
        sharex=False,
    )
    # PLOT 0
    # ax[0].errorbar(
    #     x=df_single_station_msk.index,
    #     y=df_single_station_msk["Wet_Zen"],
    #     yerr=df_single_station_msk["Sig_Zen"],
    #     linestyle="-",
    #     marker="o",
    #     ms=1,
    #     lw=0.5,
    #     color="navy",
    #     label="Zenith Wet Delay",
    # )
    ax[0].errorbar(
        x=df_single_station_msk.index,
        y=df_single_station_msk["PW"],
        yerr=df_single_station_msk["Sig_PW"],
        linestyle="",
        lw=0.5,
        color="lightblue",
        label="Precipitable Water (VMF1)",
    )
    ax[0].plot(
        df_single_station_msk.index,
        df_single_station_msk["PW_local"],
        linestyle="-",
        lw=0.5,
        color="navy",
        label="Precipitable Water (local temperature)",
    )
    ax[0].grid()
    ax[0].set_ylabel(
        "Precipitable Water (mm)", fontsize=14, color="black", fontweight="bold"
    )
    ax[0].legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax[0].xaxis.set_major_formatter(date_form)
    ax[0].xaxis.set_major_locator(mdates.HourLocator(interval=24))
    ax[0].xaxis.set_minor_locator(mdates.HourLocator(interval=12))
    ax[0].set_xlim([start_time, end_time])
    ax[0].set_ylim([0, 60])
    # PLOT 1
    ax[1].plot(
        df_single_station.index,
        df_single_station["PW"],
        linestyle="",
        marker=".",
        ms=0.2,
        lw=0.5,
        color="lightblue",
        label="Precipitable Water (VMF1)",
    )
    ax[1].plot(
        df_single_station.index,
        df_single_station["PW_local"],
        linestyle="-",
        marker="",
        lw=0.3,
        color="navy",
        label="Precipitable Water (local temperature)",
    )
    # ax[1].fill_between(
    #     df_single_station.index,
    #     df_single_station["Wet_Zen"] - df_single_station["Sig_Zen"],
    #     df_single_station["Wet_Zen"] + df_single_station["Sig_Zen"],
    #     linestyle="-",
    #     lw=0.5,
    #     color="navy",
    #     alpha=0.3,
    #     label=r"$\sigma$ Zenith Wet Delay",
    # )
    ax[1].set_ylim([0, 70])
    ax[1].grid()
    ax[1].legend(prop={"size": 14})
    ax[1].set_ylabel(r"Precipitable Water (mm)", fontsize=14, fontweight="bold")
    date_form = DateFormatter("%Y-%b")
    date_form.set_tzinfo(gettz("GMT"))
    ax[1].xaxis.set_major_formatter(date_form)
    ax[1].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax[1].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
    fg.suptitle(
        "%s: Precipitable Water" % station_name,
        fontsize=16,
        fontweight="bold",
    )
    fg.savefig(pngfname, dpi=300)
    plt.close(fg)


if __name__ == "__main__":
    # hdf_files = sys.argv[1]

    # make one file per station with all data
    csv_files = [
        "Nepal_2023_G_all_stations.csv.bz2",
        "Nepal_2024_G_all_stations.csv.bz2",
        "Nepal_2025_G_all_stations.csv.bz2",
        "Nepal_2026_G_all_stations.csv.bz2",
    ]
    dfs = [pd.read_csv(file) for file in csv_files]
    df = pd.concat(dfs, axis=0, ignore_index=False)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.set_index("datetime")

    unique_stations = df["Name"].unique()
    for i in range(len(unique_stations)):
        station_name = unique_stations[i]
        print(station_name)
        if (
            station_name != "NPA1"
            and station_name != "NPA2"
            and station_name != "NPA3"
            and station_name != "NPA4"
            and station_name != "NPA5"
            and station_name != "NPA6"
            and station_name != "NPA7"
        ):
            continue
        if station_name == "NPA1" or station_name == "NPA5":
            # will need to merge climate data for station NPA1 (old and new climate data)
            continue
        df_single_station = df[df.Name == station_name]
        # remove negative zenith wet delay
        df_single_station2 = df_single_station.drop(
            df_single_station[df_single_station["Wet_Zen"] < 0].index
        )
        df_single_station = df_single_station2.groupby(level=0).mean(numeric_only=True)
        df_single_station2 = None
        df_single_station = df_single_station.asfreq("h").reindex()
        # Load in T data from met station and calculate PW from local climate data
        #
        metdata_fname = "%s_meteorologic_data.csv.bz2" % station_name
        df_met = pd.read_csv(metdata_fname)
        df_met["date"] = pd.to_datetime(df_met["date"], format="ISO8601")
        df_met = df_met.set_index("date")
        df_met2 = df_met.groupby(level=0).mean(numeric_only=True)
        df_met = df_met2.resample("1h").mean()
        df_met2 = None
        df_merged = pd.merge(
            df_single_station, df_met, left_index=True, right_index=True
        )
        if "T1_C" in df_merged.columns:
            # rename outside temperature to T_C for calculation
            df_merged.rename(columns={"T1_C": "T_C"}, inplace=True)
        df_merged["PW_local"] = gnss_zwd_to_pw(
            df_merged["Wet_Zen"] * 100, T_s=df_merged["T_C"], T_m=None
        )
        outfile_fn = "G_ZWD"
        df_single_station.to_csv(outfile_fn + "_%s.csv.bz2" % station_name)
        # df_single_station.to_hdf(outfile_fn + "_%s.hdf" % station_name, key="metutil")
        start_time = np.max(df_merged.index) - np.timedelta64(10, "D")
        start_time.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = np.max(df_merged.index)
        end_time.replace(hour=23, minute=59, second=59, microsecond=0)
        mask = (df_merged.index > start_time) & (df_merged.index <= end_time)
        df_merged_msk = df_merged.loc[mask]
        # df_merged_msk = df_merged_msk.resample("1h").mean()
        df_merged["Wet_Zen_12h_rollingmean"] = (
            df_merged["Wet_Zen"].rolling("12h", center=True).mean()
        )
        df_merged["PW_12h_rollingmean"] = (
            df_merged["PW"].rolling("12h", center=True).mean()
        )
        pngfname = "%s_plot_Wet_Zen_2panels.png" % station_name
        plot_Wet_Zen(df_merged, df_merged_msk, pngfname)
        pngfname = "%s_plot_PrecipitableWater_2panels.png" % station_name
        plot_PW(df_merged, df_merged_msk, pngfname)
