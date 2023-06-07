import os, argparse, shutil, subprocess, time

parser = argparse.ArgumentParser()

#parser.add_argument("-cfg","--cfg_file", type=str, help='Specify Configuration File Location',required=True)
parser.add_argument("-cfg","--cfg_file", type=str, help='Specify Configuration File Location')
args=parser.parse_args()
config_file=args.cfg_file

with open(config_file,'r') as file:
    config_info=file.readlines()


dirdic={}
for line in config_info:
    if "libid" in line.lower().strip():
        libid=line.split('=')[1].strip()
        dirdic['libid']=libid

    if "tech" in line.lower().strip():
        tech=line.split('=')[1].strip()
        node=tech[:2]
        dirdic['tech']=tech
        dirdic['node']=node+'nm'

    if "corner" in line.lower().strip():
        corner=line.split('=')[1].strip()
        dirdic['corner']=corner



dirpath=f"{dirdic['node']}/{dirdic['tech']}/{dirdic['libid']}/{dirdic['corner']}"


if not os.path.exists(dirpath):
    os.makedirs(dirpath)


pwd=os.getcwd().replace('\\','/')



# config_dest=dirpath+'/Config'
# config_source=pwd+'/cz_auto_std/Config/'+dirdic['tech']


config_dest=dirpath
config_source=pwd+'/cz_auto_std'

print(config_source)

if os.path.isdir(config_source):
    if os.path.exists(config_dest):
        shutil.rmtree(config_dest)
    shutil.copytree(config_source, config_dest)


lsf_command='bsub -q ulkasemiq ./run_flow' 
command="cd "+dirpath+";chmod -R 777 ./;"+lsf_command
time.sleep(5)
subprocess.call(command, shell=True)
