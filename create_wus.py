import os
import pickle
import json
import model
import pdb
import sys
import time
sys.path.append('/home/boincadm/projects/boincdocker/py/Boinc')
sys.path.append('/home/boincadm/projects/boincdocker/bin')
#sys.path.append('/home/boincadm/projects/boincdocker')

from create_work import create_work

# Function create_workunits(N) - N is the number of wu's to create
# arguments are given, also appname is given, input files are given and stages
# should call bin/create_work args file1 file2 file3 ... to make one wu
# after it makes N wus, go into database WU table, and modify it so old unsent results do not get sent

my_args=dict()
my_args['target_nresults'] = 1
my_args['min_quorum'] = 1
my_args['max_error_results'] = 1
my_args['rsc_disk_bound'] = 500000000
my_args['rsc_memory_bound'] = 2000000000
#input_files = ('hostvm_new_ga.vdi', 'vbox_job.xml', 'boinc_app')
#input_files = ('hostvm_learning.vdi', 'vbox_job.xml', 'boinc_app', 'sharedModel.h5', 'main.py', 'model.py', 'nodeLogger.py', 'cfg_1.json', 'globalModelWeights.pkl')
input_files = ['hostvm_learning.vdi', 'vbox_job.xml', 'boinc_app', 'sharedModel.h5', 'main.py', 'model.py', 'nodeLogger.py', 'cfg_1.json']
#my_args['wu_name']

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

'''
if len(sys.argv) < 2:
    print("Error: expecting an argument - number of workunits to make")
    sys.exit(1)

n = int(sys.argv[1])

for i in range(n):
    autowu_name = create_work("virtualbox", my_args, input_files)
    print(autowu_name)
'''
