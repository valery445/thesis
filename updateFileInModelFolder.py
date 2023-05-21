import os
import subprocess
import sys

projectFolder = '/home/boincadm/projects/boincdocker'
modelFolder = os.path.join(projectFolder, 'model')

if len(sys.argv) < 2:
    print(f"Error: expecting one argument - file in {modelFolder}")
    sys.exit(1)
    
filename = sys.argv[1]

# Change the working directory
os.chdir(projectFolder)

# Check if the filename exists in the model directory
filePath = os.path.join(modelFolder, filename)
if not os.path.exists(filePath):
    raise FileNotFoundError(f"File {filePath} does not exist")

# Execute the shell script to get the staged file path
shell_script = './bin/dir_hier_path'
downloadPath = subprocess.check_output([shell_script, filename]).strip().decode('utf-8')
md5downloadPath = os.path.join(downloadPath + '.md5')

# Delete the files
if os.path.exists(downloadPath):
    os.remove(downloadPath)
if os.path.exists(md5downloadPath):
    os.remove(md5downloadPath)

# Stage file
shell_script = './bin/stage_file'
args = ['--copy', filePath]
subprocess.check_output([shell_script] + args)

