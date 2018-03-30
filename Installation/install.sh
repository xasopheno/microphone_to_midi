apt-get install -y cmake git libasound2-dev python3-pip
mkdir ../.tmp
cd ../.tmp
wget http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -xvzf pa_stable_v190600_20161030.tgz
cd ./portaudio
./configure
make
make install
ldconfig
pip3 install -r ./Requirements.txt
cd ../
rm -r ./.tmp
python3 Record.py