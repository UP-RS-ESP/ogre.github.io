cd /home/bodo/tron.github.io
#cd /raid/nwarg/tron.github.io
mkdir ../tron_foo
mv ClimData/*.png ../tron_foo
git pull
mv ../tron_foo/*.png ClimData
rm -fr ../tron_foo
#bundle exec jekyll build
JEKYLL_ENV=production bundle exec jekyll build
