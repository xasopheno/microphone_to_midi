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
cd ../
wget https://aubio.org/pub/aubio-0.4.6.tar.bz2
tar xf aubio-0.4.6.tar.bz2
cd aubio-0.4.6
./waf configure build
./waf install
python3 setup.py build
python3 setup.py install
ldconfig
cd ../../Installation/
pip3 install -r ./Requirements.txt
rm -r ../.tmp