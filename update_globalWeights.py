import os
import subprocess
import sys

def update_file(filename):
    # Change the working directory
    projectDir = '/home/boincadm/projects/boincdocker'
    os.chdir(projectDir)
    
    # Execute the shell script to get the staged file path
    shell_script = './bin/dir_hier_path'
    file_path = subprocess.check_output([shell_script, filename]).strip().decode('utf-8')
    
    md5_path = os.path.join(file_path + '.md5')
    
    # Delete the files
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(md5_path):
        os.remove(md5_path)
    
    # Execute the shell script
    shell_script = './bin/stage_file'
    model_path = os.path.join('./model/', filename)
    args = ['--copy', model_path]
    try:
        output = subprocess.check_output([shell_script] + args, stderr=subprocess.STDOUT)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f'Error: shell script returned exit code {e.returncode}')
        print(e.output.decode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: expecting one argument - file in /model directory")
        sys.exit(1)
    
    filename = sys.argv[1]
    update_file(filename)
