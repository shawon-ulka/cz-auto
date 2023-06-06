import os, argparse

parser = argparse.ArgumentParser()

#parser.add_argument("-cfg","--cfg_file", type=str, help='Specify Configuration File Location',required=True)
parser.add_argument("-cfg","--cfg_file", type=str, help='Specify Configuration File Location')
args=parser.parse_args()
config_file=args.cfg_file

with open(config_file,'r') as file:
    config_info=file.readlines()


dirdic={}
for line in config_info:
    print(line)
    print(line.lower())

