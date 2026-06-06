#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/nepal/tron.github.io/ClimData/
python3 /raid/nepal/tron.github.io/ClimData/codes/read_StromPi_Logs.py /raid/nepal/tron/prt_data

