#!/bin/python
# Description: write a function that searches for a string in a file and tells
# you if it's there or not.
# Kenia Segura Aba
# 06-26-2019

def find_str(keyword, file_name):
  search_file = open (file_name, 'r')
  count = 0
  for line in search_file:
    if keyword in line:
      count += 1
  print (keyword, 'was found', count, 'times.')

find_str('GAT', 'PhiX_genome.fasta')
