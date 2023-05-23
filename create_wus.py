import os
import pickle
import json
import model
import pdb
import sys
import time
import subprocess
from itertools import chain

projectFolder = os.path.realpath(os.path.join(os.path.dirname(__file__),'..'))
#sys.path.append(os.path.join(projectFolder, 'py/Boinc'))
#sys.path.append(os.path.join(projectFolder, 'bin'))
#from create_work import create_work

my_args=dict()
my_args['target_nresults'] = 1
my_args['min_quorum'] = 1
my_args['max_error_results'] = 1
# Disk memory in bytes
my_args['rsc_disk_bound'] = 500_000_000
# Physical memory in bytes
my_args['rsc_memory_bound'] = 2_000_000_000
# Input files should be put in the same order as input_template!
input_files = ['hostvm_learning.vdi', 'vbox_job.xml', 'boinc_app', 'sharedModel.h5', 'main.py', 'model.py', 'nodeLogger.py', 'cfg_1.json']


# Function from create_work.py by boinc2docker
def create_work(appname,create_work_args,input_files):
    """
    Calls bin/create_work with extra args specified by create_work_args
    """
    return subprocess.check_output((['bin/create_work','--appname',appname]+
                           list(chain(*(['--%s'%k,'%s'%v] for k,v in create_work_args.items())))+
                           [i for i in input_files]),
                           
                          cwd=projectFolder)


def create_wus(N, batch, template):
    my_args['wu_template'] = template
    my_args['batch'] = batch
    input_files.append(f'globalModelWeights_{batch}.pkl')
    for i in range(N):
        pid = os.getpid()
        unix_time = time.time()
        my_args['wu_name'] = f"virtualbox_{batch}_{pid}_{unix_time}"
        autowu_name = create_work("virtualbox", my_args, input_files)
        print(my_args['wu_name'])

if __name__ == "__main__": 
    if len(sys.argv) < 4:
        print("Error: expecting three arguments - N (number of workunits to make), batch (iteration number), input template")
        sys.exit(1)

    N = int(sys.argv[1])
    batch = int(sys.argv[2])
    template = sys.argv[3]
    create_wus(N, batch, template)
    
