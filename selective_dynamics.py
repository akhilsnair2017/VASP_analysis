#example Usage: python3 selective_dynamics.py POSCAR F 1 2 
import os
import sys
def select(file_name,constrain,init_num,final_num):
    with open(file_name,"r") as f:
        f=f.readlines()
        with open("new_"+file_name,"w") as n:
            for i,line in enumerate(f):
                if not line.isspace():
                    line=line.rstrip('\n')
                    if i in range(7+int(init_num),8+int(final_num)):
                        line='{}   {}'.format(line,'F F F')
                    elif i>7:
                        line='{}   {}'.format(line,'T T T')     
                    n.write(line+ '\n')
                if i==6:
                    n.write('Selective Dynamics \n')
select(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
