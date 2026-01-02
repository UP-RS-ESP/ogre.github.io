#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_StromPi_Logs.py /raid/nwarg/vacon/prt_data

