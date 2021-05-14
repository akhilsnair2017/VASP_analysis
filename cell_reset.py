#/usr/bin/python3
import os
import sys
from ase.io import read,write
def reset_vacuum(input_file,new_lattice,output_file):
    a=read(input_file)
    b=new_lattice
    a.set_cell([b,b,b])
    a.center()
    a.write('{}.vasp'.format(output_file),format='vasp')
reset_vacuum(sys.argv[1],sys.argv[2],sys.argv[3])
