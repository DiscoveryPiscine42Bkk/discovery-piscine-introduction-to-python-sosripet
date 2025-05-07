#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

i = 0
while i <= 12:
    print(f"Table de{i}", end=": ")
    j = 0
    while j <= 12:
        print(i * j, end=" " if j < 12 else "\n")
        j += 1
    i += 1