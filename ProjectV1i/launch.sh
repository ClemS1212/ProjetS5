#!/bin/bash


touch nc.txt
echo '' > network.txt


#nc -nlvp 1234 &
#(cd run ; python3 prog.py) &
(tail -f nc.txt | /bin/bash) &

sleep 3
echo 'print("Starting...")' >> network.txt



echo 'import os' >> network.txt
echo 'import signal' >> network.txt
echo 'from selenium import webdriver' >> network.txt
echo 'driver = webdriver.Firefox()' >> network.txt

python3 launch.py


