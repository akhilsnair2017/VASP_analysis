from ase.io import read,write
import sys
a=read(sys.argv[1])
b=sys.argv[1]
if b.endswith(".vasp"):
    a.write('{}.xyz'.format(b.strip('.vasp')),format='xyz')
else:
    a.write('{}.xyz'.format(b),format='xyz')
lines=[]
if b.endswith(".vasp"):
    with open('{}.xyz'.format(b.strip('.vasp')),'r') as f:
        f=f.readlines()
        for i,line in enumerate(f):
            if i!=1:
                lines.append(line)
else:
    with open('{}.xyz'.format(b),'r') as f:
        f=f.readlines()
        for i,line in enumerate(f):
            if i!=1:
                lines.append(line)

if b.endswith(".vasp"):
    with open('{}.xyz'.format(b.strip('.vasp')),'w') as n:
        for i,line in enumerate(lines):
            if i==0:
                n.write(line+'\n')
            else:
                n.write(line)
else:
    with open('{}.xyz'.format(b),'w') as n:
        for i,line in enumerate(lines):
            if i==0:
                n.write(line+'\n')
            else:
                n.write(line)

if b.endswith(".vasp"):
    c=read('{}.xyz'.format(b.strip('.vasp')))
    c.write('{}.png'.format(b.strip('.vasp')),format='png')
else:
    c=read('{}.xyz'.format(b))
    c.write('{}.png'.format(b),format='png')
