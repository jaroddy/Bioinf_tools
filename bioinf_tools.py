# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:04:34 2022

@author: jarod
"""


from Bio import SeqIO
import pandas as pd
import numpy as np


def fasta_extractor(fasta_path, fasta):
    
    sequences = []
    
    with open(fasta, 'r') as file:
        for Seq_record in SeqIO.parse(file, 'fasta'):
            format_string = "%s" % Seq_record.seq
            sequences.append(format_string)
            
    return sequences
    
def one_hot_encoder(sequences):
    
    temp_base = []
    
    pattern = 'ACGTN'
    
    full_seq_dict = {}
    single_seq_dict = {}
    
    char_to_int = dict((c,i) for i, c in enumerate(pattern))
    int_to_char = dict((i,c) for i, c in enumerate(pattern))
    n = 0
    
    for seq in sequences:
        
        int_seq = [char_to_int[char] for char in seq]
        
        one_hot_seq = list()
        
        for base in int_seq:
            
           
           if base == 4:
               
               temp_base = [0,0,0,0]
               one_hot_seq.append(temp_base)
               
           else:
            
               temp_base = [0 for _ in range(len(pattern)-1)]
               temp_base[base] = 1
               one_hot_seq.append(temp_base)
             
        one_hot_seq = np.array(one_hot_seq)
        
        single_seq_dict = {n:one_hot_seq}
        
        full_seq_dict[n] = single_seq_dict[n]
        
        n = n + 1
        
        #print(single_seq_dict)   
    #return full_seq_dict
    return full_seq_dict