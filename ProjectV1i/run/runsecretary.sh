#!/bin/bash




echo '' > ./commandflow

tail -f commandflow | ../Clips/clips_core_source_640/core/clips &
/bin/python3 EventGeneratorSecretary.py


rm commandflow




