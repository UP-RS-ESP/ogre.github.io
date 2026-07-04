#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_StromPi_Logs.py /raid/kenya/ogre/prt_data

