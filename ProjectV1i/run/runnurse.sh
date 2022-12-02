#!/bin/bash

id1=$((($RANDOM % 5) + 1))
id2=$(($RANDOM % 3))
ip=10.10.1$id2.1$id1


#echo 'nc -nv '$ip' 1234' >> ../nc.txt



echo '' > commandflow
#echo '' > ../network.txt
tail -f commandflow | ../Clips/clips_core_source_640/core/clips &
/bin/python3 EventGeneratorNurse.py

rm commandflow




