magick -quality 99 -density 300 UP_1200x_logo.png Kenya_Electricity_Generating_Company_Logo_1200x.png -fuzz 1% -trim -bordercolor white -border 800x0 +repage +append 2logos_1200x.jpg
magick 2logos_1200x.jpg -resize 1200x 2logos_1200x.jpg
magick centralKenya_withredrectangle.png -resize 1200x centralKenya_withredrectangle2.jpg
magick -quality 99 -density 300 2logos_1200x.jpg centralKenya_withredrectangle2.jpg -fuzz 1% -trim -bordercolor white -border 0x10 +repage -gravity center -append 2Logo_map_OGRE.jpg
