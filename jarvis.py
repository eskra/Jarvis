#!/usr/bin/env python

import os
import subprocess
from time import sleep as wait

os.system("python3 nlu.py audio > output.txt")
os.system("python3 -c 'import handle_intent; handle_intent.mainFunc()'")
