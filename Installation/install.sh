sudo apt-get install -y cmake git libasound2-dev python3-pip
sudo pip3 install -r ./Requirements.txt
mkdir ../.tmp
cd ../.tmp
wget http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -xvzf pa_stable_v190600_20161030.tgz
cd ./portaudio
./configure
sudo make
sudo make install
sudo ldconfig
cd ../
sudo rm -r ./.tmp
sudo python3 Record.py