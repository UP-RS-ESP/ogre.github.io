#!/usr/bin/env python

import numpy as np
import pandas as pd
import os, glob, tqdm, sys
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import AutoDateLocator
import matplotlib.dates as mdates
from dateutil.tz import gettz
import datetime

pd.options.mode.chained_assignment = None  # default='warn'


def plot_all_StromPiLog():
    fg, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(12, 10),
        dpi=300,
        layout="constrained",
    )
    station_name_unique = df_all["StationName"].unique()
    colorlist = [
        "navy",
        "black",
        "steelblue",
        "black",
        "purple",
        "black",
        "forestgreen",
        "black",
        "darkorange",
        "black",
        "lightcoral",
        "black",
    ]
    now = datetime.datetime.now()
    now.replace(hour=0, minute=0, second=0, microsecond=0)
    for i in range(len(station_name_unique)):
        cstation_name = station_name_unique[i]
        df = df_all[df_all["StationName"] == cstation_name]
        df["wideV_n"] = (
            df["wide_V_1h_rolling_average"] / df["wide_V_1h_rolling_average"].mean()
        )
        ax.plot(
            df.index,
            df["wideV_n"] + i,
            ms=3,
            linestyle="",
            marker=".",
            color=colorlist[i],
            label=df.iloc[0].StationName,
        )
    ax.grid()
    ax.set_yticks(
        np.linspace(
            1,
            len(station_name_unique),
            num=len(station_name_unique),
            endpoint=True,
        ),
        labels=station_name_unique,
    )
    ax.set_ylabel(r"normalized Voltage (Wide)", fontsize=14, fontweight="bold")
    # ax.legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax.xaxis.set_major_formatter(date_form)
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=24))
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=12))
    ax.tick_params(axis="both", which="major", labelsize=14)
    # start with 10 day history
    start_time = now - datetime.timedelta(days=10)  # np.timedelta64(10, "D")
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = now
    end_time = end_time.replace(hour=23, minute=59, second=59, microsecond=0)
    ax.set_xlim([start_time, end_time])
    ax.set_title(
        "10-day battery voltage history of VACON network: %s to %s"
        % (start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")),
        fontsize=16,
        fontweight="bold",
    )
    fg.savefig("StromPi_last10days.png", dpi=300)
    plt.close(fg)

    fg, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(12, 10),
        dpi=300,
        layout="constrained",
    )
    station_name_unique = df_all["StationName"].unique()
    colorlist = [
        "navy",
        "black",
        "steelblue",
        "black",
        "purple",
        "black",
        "forestgreen",
        "black",
        "darkorange",
        "black",
        "lightcoral",
        "black",
    ]
    now = datetime.datetime.now()
    now.replace(hour=0, minute=0, second=0, microsecond=0)
    for i in range(len(station_name_unique)):
        cstation_name = station_name_unique[i]
        df = df_all[df_all["StationName"] == cstation_name]
        df["wideV_n"] = (
            df["wide_V_1h_rolling_average"] / df["wide_V_1h_rolling_average"].mean()
        )
        ax.plot(
            df.index,
            df["wideV_n"] + i,
            ms=3,
            linestyle="",
            marker=".",
            color=colorlist[i],
            label=df.iloc[0].StationName,
        )
    ax.grid()
    ax.set_yticks(
        np.linspace(
            1,
            len(station_name_unique),
            num=len(station_name_unique),
            endpoint=True,
        ),
        labels=station_name_unique,
    )
    ax.set_ylabel(r"normalized Voltage (Wide)", fontsize=14, fontweight="bold")
    # ax.legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax.xaxis.set_major_formatter(date_form)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.tick_params(axis="both", which="major", labelsize=14)
    start_time = now - datetime.timedelta(days=365)  # np.timedelta64(10, "D")
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = now
    end_time = end_time.replace(hour=23, minute=59, second=59, microsecond=0)
    ax.set_xlim([start_time, end_time])
    ax.set_title(
        "1-year battery voltage history for VACON network: %s to %s"
        % (start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")),
        fontsize=16,
        fontweight="bold",
    )
    fg.savefig("StromPi_last1year.png", dpi=300)
    plt.close(fg)


def plot_single_StromPiLog():
    fg, (ax1, ax2) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(12, 10),
        dpi=300,
        layout="constrained",
    )
    station_name_unique = df_all["StationName"].unique()
    colorlist = [
        "navy",
        "black",
        "steelblue",
        "black",
        "purple",
        "black",
        "forestgreen",
        "black",
        "darkorange",
        "black",
        "lightcoral",
        "black",
    ]
    now = datetime.datetime.now()
    now = now.replace(hour=0, minute=0, second=0, microsecond=0)
    for i in range(len(station_name_unique)):
        cstation_name = station_name_unique[i]
        df = df_all[df_all["StationName"] == cstation_name]
        df["wideV_n"] = (
            df["wide_V_1h_rolling_average"] / df["wide_V_1h_rolling_average"].mean()
        )
        ax1.plot(
            df.index,
            df["wideV_n"] + i,
            ms=3,
            linestyle="",
            marker=".",
            color=colorlist[i],
            label=df.iloc[0].StationName,
        )
    ax1.grid()
    ax1.set_yticks(
        np.linspace(
            1,
            len(station_name_unique),
            num=len(station_name_unique),
            endpoint=True,
        ),
        labels=station_name_unique,
    )
    ax1.set_ylabel(r"normalized Voltage (Wide)", fontsize=14, fontweight="bold")
    # ax1.legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax1.xaxis.set_major_formatter(date_form)
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=24))
    ax1.xaxis.set_minor_locator(mdates.HourLocator(interval=12))
    ax1.tick_params(axis="both", which="major", labelsize=14)
    # start with 10 day history
    start_time = now - datetime.timedelta(days=10)  # np.timedelta64(10, "D")
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = now
    end_time = end_time.replace(hour=23, minute=59, second=59, microsecond=0)
    ax1.set_xlim([start_time, end_time])
    ax1.set_xlabel(
        "Date (%s to %s)"
        % (start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")),
        fontsize=14,
        fontweight="bold",
    )
    for i in range(len(station_name_unique)):
        cstation_name = station_name_unique[i]
        df = df_all[df_all["StationName"] == cstation_name]
        df["wideV_n"] = (
            df["wide_V_1h_rolling_average"] / df["wide_V_1h_rolling_average"].mean()
        )
        ax2.plot(
            df.index,
            df["wideV_n"] + i,
            ms=3,
            linestyle="",
            marker=".",
            color=colorlist[i],
            label=df.iloc[0].StationName,
        )
    ax2.grid()
    ax2.set_yticks(
        np.linspace(
            1,
            len(station_name_unique),
            num=len(station_name_unique),
            endpoint=True,
        ),
        labels=station_name_unique,
    )
    ax2.set_ylabel(r"normalized Voltage (Wide)", fontsize=14, fontweight="bold")
    # ax2.legend(prop={"size": 14})
    date_form = DateFormatter("%b-%d")
    date_form.set_tzinfo(gettz("GMT"))
    ax2.xaxis.set_major_formatter(date_form)
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax2.tick_params(axis="both", which="major", labelsize=14)
    start_time = now - datetime.timedelta(days=365)  # np.timedelta64(10, "D")
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = now
    end_time = end_time.replace(hour=23, minute=59, second=59, microsecond=0)
    ax2.set_xlim([start_time, end_time])
    ax2.set_xlabel(
        "Date (%s to %s)"
        % (start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")),
        fontsize=14,
        fontweight="bold",
    )
    # ax2.set_title(
    #     "1-year battery voltage history for VACON network: %s to %s"
    #     % (start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")),
    #     fontsize=16,
    #     fontweight="bold",
    # )
    fg.savefig("ClimData/StromPi_last10days_last1year.png", dpi=300)
    plt.close(fg)


log_paths = sys.argv[1]
data_paths = "qt01,qt02,qt03,qt04,qt05,qt06,qt07,qt08,qt09,qt10,qt11,qt12"
data_path_single = data_paths.split(",")
station_name = []
filelists = []
for i in range(len(data_path_single)):
    station_name.append(data_path_single[i].upper())
    filelist = glob.glob(
        os.path.join(log_paths, data_path_single[i] + "_prt", "prt_Log_StromPi_DC*")
    )
    filelist.sort()
    filelists.append(filelist)

dfs2 = []
for i in range(len(filelists)):
    dfs = []
    filelist = filelists[i]
    for name in tqdm.tqdm(filelist, desc=str(station_name[i]).upper()):
        # 2024-01-13 05:30:02 Wide: 2.775 V, BAT: 3.493 V, USB: 5.160 V, OUTPUT: 5.150 V
        df = pd.read_csv(
            name,
            sep=" ",
            skipinitialspace=True,
            skiprows=0,
            skip_blank_lines=True,
            names=[
                "day",
                "hours",
                "wide_label",
                "wide_V",
                "wide_unit",
                "bat_label",
                "bat_V",
                "bat_unit",
                "usb_label",
                "usb_V",
                "usb_unit",
                "output_label",
                "output_V",
                "output_unit",
            ],
        )
        df["date"] = pd.to_datetime(df["day"] + " " + df["hours"])
        df["date"] = pd.to_datetime(df["date"], utc=True)
        df.drop(
            columns=[
                "wide_label",
                "wide_unit",
                "bat_label",
                "bat_unit",
                "usb_label",
                "usb_unit",
                "output_label",
                "output_unit",
                "day",
                "hours",
            ],
            inplace=True,
        )
        cols_to_keep1 = [col for col in df.columns if not df[col].isnull().all()]
        dfs.append(df[cols_to_keep1])
    df_all = pd.concat(dfs, ignore_index=True)
    df_all.set_index("date", inplace=True)
    df_all.sort_index(ascending=True, inplace=True)
    # Drop NaT rows
    df_all["TMP"] = df_all.index.values  # index is a DateTimeIndex
    df_all_noNat = df_all[df_all.TMP.notnull()].copy()  # remove all NaT values
    df_all_noNat.drop(["TMP"], axis=1, inplace=True)
    df_all = df_all_noNat.copy()
    df_all_noNat = None
    df_all["wide_V_1h_rolling_average"] = df_all["wide_V"].rolling("1h").mean()
    df_all["StationName"] = str(station_name[i]).upper()
    dfs2.append(df_all)
df_all = pd.concat(dfs2)

# plot_all_StromPiLog()
plot_single_StromPiLog()
