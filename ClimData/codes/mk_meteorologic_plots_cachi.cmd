#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data.py /raid/Nepal/tron/clim_data/npa1/ "Bidur (Trishuli Power House)" 01_Bidur /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data_tinyblack.py /raid/Nepal/tron/clim_data/npa2/ "Trishuli 3A Dam Site" 02_Trishuli3A /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data_tinyblack.py /raid/Nepal/tron/clim_data/npa3/ "Sanjen Hydropower Station" 03_Sanjen /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data.py /raid/Nepal/tron/clim_data/npa4/ "Chilime Hydropower Station" 04_Chilime /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data.py /raid/Nepal/tron/clim_data/npa5/ "Dhunche Nepal Electricity Authority" 05_Dhunche /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data.py /raid/Nepal/tron/clim_data/npa6/ "Sanjen Hydropower Headwater" 06_Sanjen2 /raid/Nepal/tron.github.io/ClimData/

cd /raid/Nepal/tron.github.io/ClimData/
python3 /raid/Nepal/tron.github.io/ClimData/codes/read_meteorologic_data.py /raid/Nepal/tron/clim_data/npa7/ "Trishuli 3A Power House" 07_Trishuli3APH /raid/Nepal/tron.github.io/ClimData/

