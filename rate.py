from math import *
import pandas as pd
from statistics import *
kbt=0.026 #eV
pref=10E9
def thermo_equb_const(G):
    return exp(-G/kbt)
def electro_equb_const(G,U):
    return exp(-(U-G)/kbt)
def thermo_rate_const(ea,pref):
    return pref*exp(-ea/kbt)
def electro_rate_const(pref,ea,U,G):
    return pref*exp(-ea/kbt)*exp(-0.5*(U-G)/kbt)
reactions=['O2(aq)--O2(dl)','O2(dl)+*--O2*','O2*+H--OOH*','OOH*+H--O*+H2O','O*+H--OH*','OH*+H--O*+H2O']
pref=[8E5,1E8,1E9,1E9,1E9,1E9]
pref=[float(i) for i in pref]
G=[0.00,-0.345,-0.688,-2.185,-0.905,-0.797]
G=[float(i) for i in G]
ea=[0.00,0.00,0.26,0.26,0.26,0.26]
ea=[float(i) for i in ea]
U=[0,0.2,0.4,0.6,0.8,1,1.2,1.4]
U=[float(i) for i in U]
U_app=float(input('Potential: '))
eq_list=[]
kf_list=[]
kb_list=[]
for i,react in enumerate(reactions):
    if i==1 or i==2:
        K_eq=thermo_equb_const(G[i])
        k_f=thermo_rate_const(ea[i],pref[i])
        k_b=K_eq/k_f
    else:
        K_eq=electro_equb_const(G[i],U_app)
        k_f= electro_rate_const(pref[i],ea[i],U_app,G[i])
        k_b=K_eq/k_f
    eq_list.append(K_eq)
    kf_list.append(k_f)
    kb_list.append(k_b)
d={'Reactions':reactions,'Equb_Constant':eq_list,'Forward_rate':kf_list,'Backward_rate':kb_list}
s = pd.DataFrame(d)
print(s)
