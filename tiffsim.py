#!/usr/bin/python
#-*-coding:utf-8-*-
from varinfor import   similarity_seq
from libtiff import TIFF
import argparse

__doc__='''
this module helps calculate similarity between two tiff images using variation of information
use it like this:
python tiffsim.py file_a file_b
'''
def similarity_tiff(tiff_filename_a,tiff_filename_b):
    a=TIFF.open(tiff_filename_a)
    b=TIFF.open(tiff_filename_b)
    #seq_a=tuple(x for x in a.read_image().flat)
    #seq_b=tuple(x for x in b.read_image().flat)
    seq_a=(x for img in a.iter_images() for x in img.flat)
    seq_b=(x for img in b.iter_images() for x in img.flat)
    return similarity_seq(seq_a,seq_b)
    #print len(seq_a),len(seq_b)
    
if __name__=='__main__':
    #print similarity_tiff('/home/deli/1.tif','/home/deli/2.tif')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename_a')
    parser.add_argument('filename_b')
    args=parser.parse_args()
    print similarity_tiff(args.filename_a,args.filename_b) 
    

