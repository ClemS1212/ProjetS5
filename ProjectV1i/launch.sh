#!/bin/bash

#touch output.pcap
#chmod o=rw output.pcap
#sudo tshark -a duration:180 -i enp0s3 -w output.pcap &

id=$((($RANDOM % 5) + 1))

ip=10.10.10.$id

rm -f /tmp/f
mkfifo /tmp/f

touch nc.txt
echo '' > network.txt
#xterm -e 'nc -nlvp 1234' &
#xterm -e 'cd run ; python3 prog.py' &
#xterm -e 'tail -f nc.txt | /bin/bash' &

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


