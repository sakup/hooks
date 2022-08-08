#!/usr/bin/python3

import sys
from time import time

line = sys.stdin.read()
(base, commit, ref) = line.strip().split()
print("Base - " + base)
print("Commit - " + commit)
print("Ref - " + ref)