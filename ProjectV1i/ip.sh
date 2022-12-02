#!/bin/bash

id1=$((($RANDOM % 5) + 1))
id2=$(($RANDOM % 3))
ip=10.10.1$id2.1$id1

nc -nv $ip 1234 &
