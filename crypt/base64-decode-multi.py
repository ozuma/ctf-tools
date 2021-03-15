#!/usr/bin/python3

# Ref: TryHackMe [Scripting] room, Task 1
#  https://tryhackme.com/room/scripting

import sys
from base64 import *

filename = sys.argv[1]
counts = int(sys.argv[2])

f = open(filename, "r")
str_base64 = f.read()
f.close()

for i in range(counts):
	str_base64 = b64decode(str_base64)

print(str_base64)
