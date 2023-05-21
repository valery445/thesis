import glob
import json
import os
import shutil
import subprocess
import sys
from db_deleteUnsentJobs import db_deleteUnsentJobs
from makeIterationTemplate import makeIterationTemplate
from create_wus import create_wus

projectFolder = '/home/boincadm/projects/boincdocker'

# Copy empty.pkl to agregation.pkl
shutil.copy(os.path.join(projectFolder, 'model', 'defaults', 'empty.pkl'),
            os.path.join(projectFolder, 'model', 'agregation.pkl'))

# Delete globalModelWeights files and copy model_initial.pkl to globalModelWeights_1.pkl
for filename in glob.glob(os.path.join(projectFolder, 'model', 'globalModels', 'globalModelWeights*.pkl')):
    os.remove(filename)
shutil.copy(os.path.join(projectFolder, 'model', 'defaults', 'model_initial.pkl'),
            os.path.join(projectFolder, 'model', 'globalModels', 'globalModelWeights_1.pkl'))
            
# Delete files in /results that haven't yet been agregated
for filename in glob.glob(os.path.join(projectFolder, 'results', '*.pkl')):
    os.remove(filename)

# Call db_deleteUnsentJobs function and update learning.json
with open(os.path.join(projectFolder, 'model', 'learning.json'), 'r') as f:
    data = json.load(f)
db_deleteUnsentJobs('virtualbox', data['iterationNumber'])
data['agregatedCount'] = 0
data['iterationNumber'] = 1
with open(os.path.join(projectFolder, 'model', 'learning.json'), 'w') as f:
    json.dump(data, f, indent=4)

# Delete virtualbox_ files and call makeIterationTemplate function
for filename in glob.glob(os.path.join(projectFolder, 'model', 'iterationTemplates', 'virtualbox_*')):
    os.remove(filename)
template = makeIterationTemplate(projectFolder, 1)

# Empty log files
for filename in ['agregator_error_log.txt', 'agregator_log.txt', 'agregator_values.txt', 'new_iteration_values.txt']:
    open(os.path.join(projectFolder, 'model', 'logs', filename), 'w').close()

# Delete globalModelWeights files in download directory
for filename in glob.glob(os.path.join(projectFolder, 'download', '**', 'globalModelWeights_*'), recursive=True):
    if filename.endswith('.pkl') or filename.endswith('.pkl.md5'):
        os.remove(filename)

# Stage global model file
os.chdir(projectFolder)
shell_script = './bin/stage_file'
args = ['--copy', os.path.join(projectFolder, 'model', 'globalModels', 'globalModelWeights_1.pkl')]
subprocess.check_output([shell_script] + args)

print("The learning has been successfully restarted to 1(first) iteration!")

if len(sys.argv) == 2:
    N = int(sys.argv[1])
    print(f"Making {N} new workunits\n")
    create_wus(N, 1, template)
    
if len(sys.argv) > 2:
    print("Too many arguments! Can be only one additional - number of wus to make!")
    sys.exit(1)
