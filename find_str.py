#!/bin/python
# Description: write a function that searches for a string in a file
# Kenia Segura Aba
# 06-26-2019

def find_str(keyword, file_name):
  search_file = open (file_name, 'r')
  search_str = ''
  for line in search_file:
    search_str += line.strip()
  count = search_str.count(keyword)
  print (keyword, 'was found', count, 'times.')

find_str('ATCG', 'PhiX_genome.fasta')
