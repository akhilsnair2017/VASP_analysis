import os
import sys
import pandas as pd
path="./"
file_1=sys.argv[1]
file_2=sys.argv[2]
file_list=[file_1,file_2]
atom_list=[]
#print(file_list)
charge_list=[[],[]]
for file,list_no in zip(file_list,charge_list):
    with open(file,'r') as f:
        f=f.readlines()
        atom_1=int(sys.argv[3].strip('-')[0])
        atom_2=int(sys.argv[3].strip('-')[2])
        atom_list=[i for i in range(atom_1,atom_2+1)]
        for i in range(2+atom_1-1,2+atom_2):
            charge=f[i].split()[4]
            list_no.append(charge)
charge_1st=[float(i) for i in charge_list[0]]
charge_2nd=[float(i) for i in charge_list[1]]
charge_trans=[]
for i,j in zip(charge_1st,charge_2nd):
    charge_trans.append(round((i-j),4))
df={'Atom_number':atom_list,'Charge_first':charge_1st,'Charge_second':charge_2nd,'Charge_transfer':charge_trans}
s=pd.DataFrame(df)
print(s)
