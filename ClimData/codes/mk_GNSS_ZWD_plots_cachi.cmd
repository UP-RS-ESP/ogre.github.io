#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/Nepal/tron.github.io/ClimData/
python codes/plot_metutil_timeseries.py
