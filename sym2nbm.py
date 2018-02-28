#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(description="Convert Project64 .sym to Nemu .nbm")
parser.add_argument("sym", help="Symbol file")
args = parser.parse_args()

output = "Root\n"

with open(args.sym) as inf:
  for line in inf:
    pieces = line.split(",")
    if len(pieces) < 2:
      continue
    output += "\t"
    if pieces[1] == "code":
      output += "CPU 0x%s: " % (pieces[0])
    else:
      output += "MEM 0x%s: " % (pieces[0])
    output += pieces[2].strip()
    output += "\n"

print(output)
