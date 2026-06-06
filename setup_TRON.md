git clone https://github.com/UP-RS-ESP/vacon.github.io.git
cd vacon.github.io
rm -fr .editorconfig .gitattributes .github docs test CHANGELOG.md minimal-mistakes-jekyll.gemspec README.md screenshot-layouts.png screenshot.png



sudo apt-get remove ruby
sudo apt update
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
curl -sL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash -
source .bashrc

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc

rbenv install 3.4.5
rbenv global 3.4.5

sudo apt-get install rubygems

Hosting is done through nginx
Webpage only needs to be build - not hosted:
git pull
bundle exec jekyll build


# Install python on VM
sudo apt install python3 python3-numpy python3-pandas python3-tqdm

mkdir -p /home/bodo/vacon/logs

crontab -e
30 2 * * * /home/bodo/vacon.github.io/ClimData/codes/get_climdata_from_gnss.sh 2>&1 | tee /home/bodo/vacon/logs/get_climdata_from_gnss_`date +"%d-%m-%Y"`.log
35 2 * * * /home/bodo/vacon.github.io/ClimData/codes/mk_meteorologic_plots.cmd 2>&1 | tee /home/bodo/vacon/logs/mk_meteorologic_plots_`date +"%d-%m-%Y"`.log
10 3 * * * /home/bodo/vacon.github.io/recompile.cmd 2>&1 | tee /home/bodo/vacon/logs/recompile_`date +"%d-%m-%Y"`.log






