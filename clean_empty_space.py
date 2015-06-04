#!/usr/bin/env python3

import sys
from numpy import *
import fileinput


for line in fileinput.input(sys.argv[1:]):
	cleanline = line.strip()
	if cleanline:
		print(cleanline)
