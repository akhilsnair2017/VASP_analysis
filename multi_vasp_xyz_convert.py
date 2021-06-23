from ase.io import read,write
import os
path="./"
for vasp_file in os.listdir():
    if vasp_file.endswith("vasp"):
        a=read(vasp_file)
        file_name=vasp_file.split('.')[0]
        a.write('{}.xyz'.format(file_name),format='xyz')
