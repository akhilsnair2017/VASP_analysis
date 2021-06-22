import os
path="./"
for dir in os.listdir():
    if os.path.isdir(dir) and dir.isdigit():
        dir_path=os.path.join(path,dir)
        with open(dir_path+'/OUTCAR') as f:
            f=f.readlines()
            last_line=f[-1].strip()
            if last_line.startswith("Voluntary"):
                pass
            else:
                print(dir)
~
