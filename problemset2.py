#!/usr/bin/env python3
import sys
dna_code = sys.argv[1]
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if dna_code in dna:
  print(dna_code, ' in DNA')
else:
  print(dna_code, ' is not there in the DNA')
