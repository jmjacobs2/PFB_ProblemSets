#!/usr/bin/env python3

class DNARecord(object):
#define class attributes
 # sequence ='ATGCGTGCATGCAGTGCACATG'
 # gene_name = 'sequence'
 # species_name = 'Unknown organism'

  #define class attributes
  def __init__(self, sequence, gene_name, species_name):
    self.sequence = sequence
    self.gene_name = gene_name
    self.species_name = species_name

  #define methods e.g. length
  def get_length(self):
    length = len(self.sequence)
    return length

  #define nucleotide composition
  def get_nuc_comp(self):
    for nt in self.sequence:
      nt_count = {}
      dna = self.sequence
      unique = set(dna) 
      for nt in unique:
        count = dna.count(nt)
        nt_count[nt] = count
    return nt_count
    # if nt in nt_count:
      #  nt_count[nt] += 1
     # else:
      #  nt_count[nt] = 1
     # return nt_count
     # return nt_count
     # a_count = self.sequence.count('A')
     # t_count = self.sequence.count('T') 
     # c_count = self.sequence.count('C')
     # g_count = self.sequence.count('G')
     # all_count = 
     # return all_count

  def get_GC(self):
    length = len(self.sequence)
    c_count = self.sequence.count('C')
    g_count = self.sequence.count('G')
    gc_content = (c_count + g_count) / length
    return gc_content

#output a fasta formatted sequence
  def fasta(self):
    sequence_name = '>' + self.gene_name
    sequence_nt = '\n' +  self.sequence
    sequence_fasta = sequence_name + sequence_nt  
    return sequence_fasta

dna_rec_obj_1 = DNARecord('ATGCGTGCATGCAGTGCACATG', 'sequence', 'Unknown organism')

for d in [dna_rec_obj_1]:
  print('sequence:', d.sequence, '\n', 'name:', d.gene_name, '\n', 'species:', d.species_name,sep='')
  #prints the sequence length11
  print('sequence length is:', dna_rec_obj_1.get_length())
  print('nt composition is:', dna_rec_obj_1.get_nuc_comp())
  print('GC content is:', dna_rec_obj_1.get_GC())
  print('fasta file looks like:'+ '\n', dna_rec_obj_1.fasta(), sep='')
