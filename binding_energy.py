#example usage python3 binding_energy.py adsorbent_directory_name adsorbate_directory_name
import sys
lines=[]
with open("OSZICAR","r") as myfile:
    for line in myfile:
        lines.append(line.rstrip('\n'))
#    for line in lines:
#        print(line)
a=float(lines[-1][27:43])
print("adsorbed system energy = ",a)
a_lines=[]
with open("./{}/OSZICAR".format(sys.argv[1]),"r") as cluster:
    for a_line in cluster:
        a_lines.append(a_line.rstrip('\n'))
b=float(a_lines[-1][27:43])
print("adsorbent_energy = ", b)
c_lines=[]
with open("./{}/OSZICAR".format(sys.argv[2]),"r") as molecule:
    for c_line in molecule:
        c_lines.append(c_line.rstrip('\n'))
c=float(c_lines[-1][27:43])
print("adsorbate_energy = ", c)
BE=float(a-(b+c))
print("Binding Energy in eV  = ",BE)

