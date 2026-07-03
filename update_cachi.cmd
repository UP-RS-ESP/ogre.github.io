cd /raid/kenya/ogre.github.io
mkdir ../ogre_foo
mv ClimData/*.png ../ogre_foo
mv ClimData/*.jpg ../ogre_foo
mv ClimData/*.bz2 ../ogre_foo
git pull
mv ../ogre_foo/*.png ClimData
mv ../ogre_foo/*.jpg ClimData
mv ../ogre_foo/*.bz2 ClimData
rm -fr ../ogre_foo
#bundle exec jekyll build
#JEKYLL_ENV=production bundle exec jekyll build
