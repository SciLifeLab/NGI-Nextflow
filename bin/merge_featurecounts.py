#!/usr/bin/env/python

import argparse
import os
import re
from collections import defaultdict


def do_the_thing(dest_dir,out_file,input_files):
   table_dict=defaultdict(dict)

   import pdb 
   pdb.set_trace() 

   for input_file in input_files:
       sample_name=os.path.basename(input_file)
       sample_name= sample_name.replace("Aligned.sortedByCoord.out_gene.featureCounts.txt","")
       table_dict[sample_name]=dict()
       with open(input_file, 'r') as f:
           for line in f:
               if not line.startswith('E'):
                   continue
               line_info=line.split('\t')
               gene=line_info[0]
               gene_count=line_info[-1:]
               table_dict[sample_name][gene]=gene_count 
    
    




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Merges the counts for all the samples in a project
    """)
    parser.add_argument("dest_dir", metavar='Output directory', nargs='?', default='.',
                                   help="Path to output.")
    parser.add_argument("out_file", metavar ='Name of output file', nargs='?', default='all_counts.txt',
                                   help= "Name of the output file that will be created")
    parser.add_argument("input_files", metavar='Input file', nargs=argparse.REMAINDER, default='*.featureCounts.txt',
                                   help="Path to the outputfiles from FeatureCounts. ")
    args = parser.parse_args()
    do_the_thing(args.dest_dir, args.out_file, args.input_files)
