import os
from ase.io import read,write
path='./'
if os.path.isdir('results'):
    pass
else:
    os.mkdir('results')
for dir in os.listdir():
    if os.path.isdir(dir) and len(dir)<4:
        index=''.join([dir[i]for i in range(len(dir)) if i!=0])
        a=read('./{}/CONTCAR'.format(dir))
        a.write('./results/{}.vasp'.format(index),format='vasp')
