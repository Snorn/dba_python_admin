#!usr/bin/env python3
#############################################################################
#
#  Author - Justin Broughton (snornn@gmail.com)
#  GIT repository - https://github.com/Snorn/devops_maxdb
#  Date - 23 May 2019
#  NON INTERACTIVE python script to perform a MAXDB backup and archive tasks
#  This script relies on the setup.py script having been run and the file
#  dba_environment.txt existing in the current directory
#  The PATH environment variable export PATH=$PATH:/sapdb/SID/db/bin
#  PATH can be set in .profile, a BASH example is included in the repository
#
#############################################################################

import json, time, re, os, datetime
from os.path import isfile

def write_to_log(inputstr):
        fout = open("./log_dba_admin.txt", "a+")
        fout.write(dictEnv["Nodename"] + " ")
        fout.write("Information ")
        fout.write(dictEnv["SID"] + " ")
        fout.write(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + " ")
        fout.write("Event Data ")
        fout.write(inputstr + '\n')
        fout.close()

def append_to_json(inputstr):
    dict_json = {
        "hostname" : dictEnv["Nodename"],
        "SID" : dictEnv["SID"],
        "DateTime" : datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"),
        "Data" : inputstr
        }
    return dict_json

def getKeyPairs(output):
    for x in output:
        if re.search(":", x):
            y = x.split(':')
            dictEnv[y[0].strip()] = y[1].strip()

dictEnv = {"DB": "MAXDB"}
dba_file = isfile("dba_environment.txt")

if dba_file:
    filein = open("dba_environment.txt")
    strfile = filein.read().split('\n')
    getKeyPairs(strfile)

    write_to_log("backup in progress")

    with open("sample.json", "a+") as outfile:
        json.dump(append_to_json("backup in progress"), outfile)
    with open("sample.json", "a+") as outfile:
        outfile.write('\n')
        
else:
    print("The DBA Environment file does not exist, rerun setup")
    quit()

