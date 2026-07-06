magick technical_university_of_kenya_logo.png -resize 400x technical_university_of_kenya_logo_400x.png
magick UP_1200x_logo.png -resize 400x UP_400x_logo.png
magick Kenya_Electricity_Generating_Company_Logo_1200x.png -resize 400x Kenya_Electricity_Generating_Company_Logo_400x.png
magick -quality 99 -density 300 UP_400x_logo.png Kenya_Electricity_Generating_Company_Logo_400x.png technical_university_of_kenya_logo_400x.png -fuzz 1% -trim -bordercolor white -border 400x0 +repage +append 3logos_400x.jpg
magick Olkaria_Topo_GNSS_stations_with_inset.png -resize 1200x Olkaria_Topo_GNSS_stations_with_inset2.jpg
magick 3logos_400x.jpg -resize 1200x 3logos_1200x.jpg
magick -quality 99 -density 300 3logos_1200x.jpg Olkaria_Topo_GNSS_stations_with_inset2.jpg -fuzz 1% -trim -bordercolor white -border 0x10 +repage -gravity center -append 3Logo_map_OGRE.jpg
#magick 3Logo_map_OGRE.jpg -resize 600x 3Logo_map_OGRE.jpg
rm 3logos_400x.jpg
rm Olkaria_Topo_GNSS_stations_with_inset2.jpg
