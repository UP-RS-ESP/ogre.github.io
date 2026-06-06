#!/usr/bin/env python

import numpy as np
import pandas as pd
import os, glob, tqdm, sys
import py7zr
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import AutoDateLocator
import matplotlib.dates as mdates
from dateutil.tz import gettz

plt.rcParams["axes.facecolor"] = "#eeeeee"
plt.rcParams["figure.facecolor"] = "#eeeeee"

data_path = sys.argv[1]
station_name = sys.argv[2]
file_prefix = sys.argv[3]
output_path = sys.argv[4]

filelist = glob.glob(os.path.join(data_path, "npa*.??m.7z"))
filelist.sort()

dfs = []
for i in tqdm.tqdm(range(len(filelist))):
    if not os.path.exists(filelist[i][:-3]):
        if os.path.getsize(filelist[i]) == 0:
            print("File is empty %s" % filelist[i])
            continue
        with py7zr.SevenZipFile(filelist[i], "r") as archive:
            archive.extractall(path=os.path.dirname(filelist[i]))
    #    if os.path.getsize(filelist[i][:-3]) < 900:
    #        print('File is small %s'%filelist[i][:-3])
    #        continue

    df = pd.read_csv(
        filelist[i][:-3],
        sep=" ",
        skipinitialspace=True,
        skiprows=9,
        on_bad_lines="skip",
        skip_blank_lines=True,
        names=["year", "month", "day", "h", "m", "s", "P_hpa", "T_C", "rh"],
    )
    df["year"] += 2000

    df["date"] = pd.to_datetime(df[["year", "month", "day", "h", "m", "s"]], utc=True)
    df.drop(columns=["year", "month", "day", "h", "m", "s"], inplace=True)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)
df_all.set_index("date", inplace=True)
df_all.T_C.drop(df_all[df_all.T_C < -40].index, inplace=True)
df_all.sort_index(ascending=True, inplace=True)
# Drop NaT rows
df_all["TMP"] = df_all.index.values  # index is a DateTimeIndex
df_all_noNat = df_all[df_all.TMP.notnull()].copy()  # remove all NaT values
df_all_noNat.drop(["TMP"], axis=1, inplace=True)
# df_all[df_all.index.isnull()]
df_all = df_all_noNat.copy()
df_all_noNat = None
start_time = np.max(df_all.index) - np.timedelta64(10, "D")
start_time.replace(hour=0, minute=0, second=0, microsecond=0)
end_time = np.max(df_all.index)
end_time.replace(hour=23, minute=59, second=59, microsecond=0)
mask = (df_all.index > start_time) & (df_all.index <= end_time)
df_all = df_all.loc[mask]
df_all = df_all.resample("5Min").mean()

df_all["rh_30m_rolling_average"] = df_all["rh"].rolling("30Min").mean()
df_all["P_hpa_30m_rolling_average"] = df_all["P_hpa"].rolling("30Min").mean()

fg, ax = plt.subplots(
    nrows=2, ncols=1, figsize=(12, 10), dpi=300, layout="constrained", sharex=True
)
ax[0].plot(
    df_all.index,
    df_all["T_C"],
    linestyle="-",
    marker="o",
    ms=1,
    lw=0.5,
    color="navy",
    label="T (outside)",
)
ax[0].grid()
ax[0].set_ylabel(r"Temperature ($^\circ$C)", fontsize=14, fontweight="bold")
ax[0].legend(prop={"size": 14})
date_form = DateFormatter("%b-%d")
date_form.set_tzinfo(gettz("GMT"))
ax[0].xaxis.set_major_formatter(date_form)
ax[1].xaxis.set_major_locator(mdates.HourLocator(interval=24))
ax[1].xaxis.set_minor_locator(mdates.HourLocator(interval=12))
ax[0].set_xlim([start_time, end_time])
# ax[0].set_title(
#     "%s: 1-minute logging interval, temperature" % station_name, fontsize=16
# )
ax1b = ax[1].twinx()
lns1 = ax[1].plot(
    df_all.index,
    df_all["P_hpa"],
    linestyle="",
    lw=0.5,
    color="lightgreen",
)
lns2 = ax1b.plot(
    df_all.index,
    df_all["rh"],
    linestyle="",
    lw=0.5,
    color="violet",
)
ax1b.plot(
    df_all.index,
    df_all["rh_30m_rolling_average"],
    marker="o",
    ms=1,
    linestyle="",
    color="purple",
    label="Rel. Humidity, 30-min rolling mean",
)
ax[1].plot(
    df_all.index,
    df_all["P_hpa_30m_rolling_average"],
    marker="o",
    ms=1,
    linestyle="",
    color="darkgreen",
    label="Pressure, 30-min rolling mean",
)
ax1b.set_ylim([0, 100])
ax[1].grid()
ax[1].set_xlabel("Month-Day-Hour (GMT)", fontsize=14, fontweight="bold")
ax[1].set_ylabel("Pressure (hPa)", fontsize=14, color="darkgreen", fontweight="bold")
ax1b.set_ylabel("Rel. Humidity (%)", fontsize=14, color="purple", fontweight="bold")
lines, labels = ax[1].get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1b.legend(lines + lines2, labels + labels2, loc=0, prop={"size": 14})
ax[1].xaxis.set_major_formatter(date_form)
ax[1].xaxis.set_major_locator(mdates.HourLocator(interval=24))
ax[1].xaxis.set_minor_locator(mdates.HourLocator(interval=12))
ax[1].set_xlim([start_time, end_time])
fg.suptitle(
    "%s: temperature, pressure, and relative humidity" % station_name,
    fontsize=16,
    fontweight="bold",
)
# ax[1].set_xlim([np.max(df_all.index) - np.timedelta64(10,'D'), np.max(df_all.index)])
fg.savefig("%s/%s_TempP_last10days.png" % (output_path, file_prefix), dpi=300)
plt.close(fg)
