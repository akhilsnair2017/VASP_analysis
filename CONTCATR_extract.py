import os
from ase.io import read,write
import shutil
path="./"
dst_dir="./"
dir_list=[]
file_list=[]
for dir in os.listdir():
    if os.path.isdir(dir):
        dir_list.append(dir)
        dir_path=os.path.join(path,dir)
        for file in os.listdir(dir_path):
            if file=='CONTCAR':
                file_path=os.path.join(dir_path,file)
                shutil.copy(file_path,os.path.join(dst_dir,dir+".vasp"))
