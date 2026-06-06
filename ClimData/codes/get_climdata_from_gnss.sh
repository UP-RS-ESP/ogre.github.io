rsync -avz gnss@141.89.241.129:/home/gnss/nepal/clim_data/npa1 :/home/gnss/nepal/clim_data/npa4 \
  :/home/gnss/nepal/clim_data/npa5 :/home/gnss/nepal/clim_data/npa6 :/home/gnss/nepal/clim_data/npa7 \
  /raid/Nepal/tron/clim_data/

# clim_data for npa1 is at
rsync -avz /raid/Nepal/nepal/npa1/clim_data/npa1 /raid/Nepal/tron/clim_data/

#clim_data for npa2 is at
rsync -avz /raid/Nepal/nepal/npa2/clim_data/* /raid/Nepal/tron/clim_data/npa2

#clim_data for npa3 is at
rsync -avz /raid/Nepal/nepal/npa3/clim_data/* /raid/Nepal/tron/clim_data/npa3
