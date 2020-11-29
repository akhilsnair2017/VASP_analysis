#!/usr/bin/env python
import os
import numpy
import pandas as pd
path="./"
structure_list=[]
energy_list=[]
with open('energy.dat','w') as n:
    for file in os.listdir(path):
        if os.path.isdir(file):
            structure_list.append(file)
            subpath=os.path.join(path,file)
            with open(subpath+'/OSZICAR', "r") as f:
                f=f.readlines()
                line=f[-1].split()
                energy=round(float(line[4]),3)
                energy_list.append(energy)
                n.write('structure_no: {}  Energy: {}\n'.format(file,energy))
dict = {"Geometry Name":structure_list,"Energy":energy_list}
s=pd.DataFrame(dict)
s['RE(eV)'] = s['Energy']-s['Energy'].min()
s=s.round(decimals=3)
blankIndex = [''] * len(s)
s.index = blankIndex
print(s)
print('Minimum energy %s'%s['Energy'].min())

