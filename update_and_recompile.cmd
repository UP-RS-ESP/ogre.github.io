cd /home/bodo/vacon.github.io
mkdir ../vacon_foo
mv ClimData/*.png ../vacon_foo
git pull
mv ../vacon_foo/*.png ClimData
rm -fr ../vacon_foo
#bundle exec jekyll build
JEKYLL_ENV=production bundle exec jekyll build
