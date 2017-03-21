#!/usr/bin/env/python

import argparse
import os
import re
from collections import defaultdict


def do_the_thing(dest_dir,out_file,input_files):
   table_dict=defaultdict(dict)


     while input_files:
        for input_file in input_files:
            sample_name=os.path.basename(fastq_file)
            sample_name.replace("Aligned.sortedByCoord.out_gene.featureCounts.txt","")
            with open(input_file, 'r') as f:
                if not line.startswith('ENSG')
                    next(f)
                for line in f:
                    
                    gene=
                    gene_count=
                    table_dict[sample_name]=dict()
                    table_dict[sample_name][gene]=gene_count 
    
    




 if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Merges the counts for all the samples in a project
    """)
    parser.add_argument("dest_dir", metavar='Output directory', nargs='?', default='.',
                                   help="Path to output. ")
    parser.add_argument("out_file" metavar ="Name of output file", nargs '?', default="all_counts.txt",
                                   help= "Name of the output file that will be created"
    parser.add_argument("input_files", metavar='Input file', nargs='+', default='*.featureCounts.txt',
                                   help="Path to the outputfiles from FeatureCounts. ")
    args = parser.parse_args() 
