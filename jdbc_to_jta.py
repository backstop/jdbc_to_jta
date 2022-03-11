#!/usr/bin/env python3

# Changes JDBC style SQL parameters to JTA style.
# Copyright 2022 Backstop Solutions Group. Released under the MIT license.

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--infile', required=True, help='Input file')
parser.add_argument('-o', '--outfile', required=True, help='Output file')

args = parser.parse_args()

infile = open(args.infile, 'r')
lines = infile.readlines()

outfile = open(args.outfile, 'w')

# meaning: "backslash, then nothing or any amount of whitespace, then the end of the line"
line_continued_re = re.compile(r'\\[\s]*$')

query_start_at = 1
next_place = query_start_at
for line in lines:
    parts = line.split('?')
    newline = parts[0]
    for i, p in enumerate(parts[1:]):
        newline += "?{}{}".format(next_place, p)
        next_place += 1
    outfile.writelines(newline)

    if not line_continued_re.search(line):
        next_place = query_start_at

infile.close()
outfile.close()
