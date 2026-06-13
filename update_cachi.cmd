cd /raid/Nepal/tron.github.io
mkdir ../tron_foo
mv ClimData/*.png ../tron_foo
mv ClimData/*.jpg ../tron_foo
mv ClimData/*.bz2 ../tron_foo
git pull
mv ../tron_foo/*.png ClimData
mv ../tron_foo/*.jpg ClimData
mv ../tron_foo/*.bz2 ClimData
rm -fr ../tron_foo
#bundle exec jekyll build
#JEKYLL_ENV=production bundle exec jekyll build
