#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_StromPi_Logs.py /raid/Nepal/tron/prt_data

