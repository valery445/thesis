import os
import subprocess

projectFolder = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
inputFilesFolder = os.path.join(projectFolder, 'thesis/inputFiles')

# Change the working directory
os.chdir(projectFolder)

# Get all files in the inputFilesFolder
filenames = os.listdir(inputFilesFolder)

for filename in filenames:
    filePath = os.path.join(inputFilesFolder, filename)

    # Stage file
    shell_script = './bin/stage_file'
    args = ['--copy', filePath]
    subprocess.check_output([shell_script] + args)


