#!/usr/bin/env python3

import re

fasta_dict = {}
with open("ecoli_18contigs.fasta") as fasta:
  for line in fasta:
    line = line.strip()
    if line.startswith('>'):
      header = re.search(r"^>(\S+)", line) #starts at > through the first white space
      fasta_dict[header.group(1)] = ''
      print(header.group(1))
    else:
      sequence = line
      fasta_dict[header.group(1)] += sequence
#print(fasta_dict)

for key, value in fasta_dict.items():# A view object that displays a list of a given dictionary's (key, value) tuple pair
  print(key, value) #prints dictionary try to use a counter and if else statement to print the few lines; links back to the factorial
