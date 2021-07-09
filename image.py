from ase.io import read,write
import sys
a=read(sys.argv[1])
b=sys.argv[1]
a.write('{}.xyz'.format(b),format='xyz')
lines=[]
with open('{}.xyz'.format(b),'r') as f:
    f=f.readlines()
    for i,line in enumerate(f):
        if i!=1:
            lines.append(line)
with open('{}.xyz'.format(b),'w') as n:
    for i,line in enumerate(lines):
        if i==0:
            n.write(line+'\n')
        else:
            n.write(line)

c=read('{}.xyz'.format(b))
c.write('{}.png'.format(b),format='png')
