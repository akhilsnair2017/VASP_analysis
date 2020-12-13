#!/usr/bin/env python3
def file_split(file_name):
	with open(file_name,'r') as f:
		f=f.readlines()
	line_numbers=[]
	count=0
	symbols=[]
	for i,line in enumerate(f):
		line=line.lstrip()
		if line.startswith('PAW_PBE'):
			line_numbers.append(i)
			count+=1
			line=line.split()
			symbols.append(line[1])
	line_numbers.append(len(f))
	print('\n Spliting POTCAR into %d POTCAR files\n'%count)
	for i in range(count):
		with open(symbols[i]+'_POTCAR', 'w') as n:
			for j in range(line_numbers[i],line_numbers[i+1]):
				n.write(f[j])
file_split('POTCAR')
