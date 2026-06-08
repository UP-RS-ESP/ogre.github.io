rm *.mp4
ffmpeg -i rpi_chilime_dailyNoon.gif -movflags faststart -pix_fmt yuv420p -vf "fps=5,scale=trunc(iw/2)*2:trunc(ih/2)*2" rpi_chilime_dailyNoon.mp4
ffmpeg -i rpi_sanjen2_dailyNoon.gif -movflags faststart -pix_fmt yuv420p -vf "fps=5,scale=trunc(iw/2)*2:trunc(ih/2)*2" rpi_sanjen2_dailyNoon.mp4
ffmpeg -i rpi_langtang_dailyNoon.gif -movflags faststart -pix_fmt yuv420p -vf "fps=5,scale=trunc(iw/2)*2:trunc(ih/2)*2" rpi_langtang_dailyNoon.mp4
rm *.gif
