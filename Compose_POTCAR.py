import os,shutil
cur_path='./'
pot_dir='/home/akhil/potpaw_PBE'
with open('POSCAR','r') as f:
        f=f.readlines()
        sym_list=list(f[5].split())
        for ele in sym_list:
                if ele not in os.listdir(cur_path):
                        pot_path=pot_dir+'/'+ele+'/POTCAR'
                        shutil.copy(pot_path,cur_path+ele)
        with open(cur_path+'POTCAR','w') as final_potcar:
                for ele in sym_list:
                        with open(ele,'r') as sub_pot_file:
                                for line in sub_pot_file:
                                        final_potcar.write(line)
