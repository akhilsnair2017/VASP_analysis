import os,shutil
import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.io import Trajectory
from ase.calculators.vasp import Vasp
from ase.optimize import BFGS
from ase.calculators.vasp import Vasp
from ase.io import read
from ase.vibrations import Vibrations
from ase.constraints import FixAtoms
from ase.thermochemistry import HarmonicThermo
path='./'
cluster=read('POSCAR') #read geometry of the input file
calc=Vasp(ncore=4,istart=0,icharg=2,ialgo=38,ismear=0,sigma=0.1,ibrion=2,nsw=300,isif=2,prec="Normal",ediff=1E-4,ediffg=-0.02,xc="pbe",ispin=2,lcharg=True,encut=470,lorbit=11,nelmin=6,nelm=60,ivdw=11,isym=0,lreal="Auto",gamma=True)
cluster.calc=calc
cluster_energy=cluster.get_potential_energy()
print('Energy: ',cluster_energy) #printing out optimized energy at zero sigma width to output file
print('Unit cell\n',cluster.get_cell()) #printing out lattice vectors of the last optimized configuration to output file
print('Coordinates\n',cluster.get_positions())# printing out optimized coordinates to output file
os.mkdir('freq')
dst_dir=path+'freq'
files=[file for file in os.listdir() if os.path.isfile(file)]
for file in files:
        shutil.copy(file,dst_dir)
os.chdir(dst_dir)
os.system('cp CONTCAR POSCAR')
atoms=read('POSCAR')
fa=FixAtoms(mask=[a.symbol=='Pt' for a in atoms]) # freezing all the reaction species
atoms.set_constraint(fa)
atoms.write('POSCAR',format='vasp')
freq_cluster=read('POSCAR')
freq_calc=Vasp(ncore=4,istart=0,icharg=2,ialgo=38,ismear=0,sigma=0.1,ibrion=5,nsw=300,isif=2,prec="Normal",ediff=1E-4,ediffg=-0.02,xc="pbe",ispin=2,lcharg=True,encut=470,lorbit=11,nelmin=6,nelm=60,ivdw=11,isym=0,lreal="Auto",gamma=True,potim=0.015,nfree=2)
freq_cluster.calc=freq_calc
vib = Vibrations(freq_cluster)
vib.run()
vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies=vib_energies,
                        potentialenergy=potentialenergy,
                        atoms=freq_cluster) #harmonic approximation for the adsorbate species vibration
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)
S = thermo.get_entropy(temperature=298.15)
H = thermo.get_helmholtz_energy(temperature=298.15)

