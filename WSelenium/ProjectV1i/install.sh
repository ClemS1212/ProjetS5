#!/bin/bash


sudo apt update
sudo apt install build-essential -y

sudo apt install tshark -y

sudo apt install netcat -y

mkdir Clips
tar -xzvf clips_core_source_640.tar.gz -C ./Clips
cd Clips/clips_core_source_640/core/
gcc -o clips -DLINUX=1 *.c -lm
cd ../../..

sudo apt install xterm -y

python3 -m pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
rm geckodriver*
