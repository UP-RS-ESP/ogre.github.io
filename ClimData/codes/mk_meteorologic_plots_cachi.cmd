#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok01/ "Olkaria 1 AU" 01_Olkaria1AU OK01 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data_tinyblack.py /raid/kenya/ogre/clim_data/ok02/ "KenGen Geolabs" 02_Geolab ok02 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data_tinyblack.py /raid/kenya/ogre/clim_data/ok03/ "Well OW-914" 03_OW914 ok03 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok04/ "Well OW-907" 04_OW907 ok04 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok05/ "Well OW-730" 05_OW730 ok05 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok06/ "Well OW-52" 06_OW52 ok06 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok07/ "KenGen Dinner Club" 07_DinnerClub ok07 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok08/ "Olomayiana" 08_Olomayiana ok08 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/ok09/ "V" 09_ ok09 /raid/kenya/ogre.github.io/ClimData/

cd /raid/kenya/ogre.github.io/ClimData/
python3 /raid/kenya/ogre.github.io/ClimData/codes/read_meteorologic_data.py /raid/kenya/ogre/clim_data/tukn/ "Technical University of Kenya, Nairobi" 10_TUKN tukn /raid/kenya/ogre.github.io/ClimData/

