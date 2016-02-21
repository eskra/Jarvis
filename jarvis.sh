#!/usr/bin/env bash

python3 nlu.py audio > output.txt &
wait
python3 handle_intent.py