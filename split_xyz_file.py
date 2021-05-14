import sys
import os
from ase.io import read,write
def xyz_file_split(file_name,division_string,number_of_atoms):
        with open(file_name,"r") as f:
                f=f.readlines()
                line_no=[]
                for i,line in enumerate(f):
                        if line.startswith(division_string):
                                line_no.append(i)
                for i in line_no:
                        with open("{}.xyz".format(line_no.index(i)),"w") as new_f:
                                for j in f[i:i+number_of_atoms+2]:
                                        new_f.write(j)
xyz_file_split(sys.argv[0],sys.argv[1],sys.argv[2])
lattice_constants=[[15.0043438644878222,0.0000164194168466,0.0000000],
                    [7.5021762330599913,12.9942430255901833,0.000000],
                    [0.000000000000,0.000000000000,26.5236593133820051]]
for file in os.listdir():
        if file.endswith("xyz"):
                file_name=file.split('.')
                a=read(file)
                a.set_cell(lattice_constants)
                a.write('{}.vasp'.format(file_name[0]))
