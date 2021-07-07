import os
import sys
#config_no=int(input("configuration number: "))
#num_atoms=int(input("number of atoms: "))
#count=0
line_list=[]
with open('XDATCAR','r') as f:
    f=f.readlines()
    with open('{}.vasp'.format(sys.argv[1]),'w') as n:
        for i in range(0,7):
            n.write(f[i])
        n.write('Direct'+'\n')
        for i,line in enumerate(f):
            if line.startswith("Direct"):
                if int(line.split('=')[1])==int(sys.argv[1]):
                    k=i+int(sys.argv[2])
                    for j in range(i+1,k+1):
                        n.write(f[j])
