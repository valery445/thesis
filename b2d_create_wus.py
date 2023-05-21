import sys
import random
import os
import time
import pdb
sys.path.append('/home/boincadm/projects/boincdocker/bin')
sys.path.append('/home/boincadm/projects/boincdocker')
from bin.boinc2docker_create_work import boinc2docker_create_work



my_image = "tensorflow/tensorflow"
#my_image = "python:3-slim"
my_command = ['python', '-c']

#Opens file and doubles every float number in it, writes to myOutput.txt
my_command.append("""
import os
import sys

input_directory = '/root/shared/'
output_directory = '/root/shared/results/'

# Get the list of files in the input directory
files = os.listdir(input_directory)

# Find the first .txt file in the directory
input_file = None
for file in files:
    if file.endswith('.txt'):
        input_file = file
        break

if input_file:
    # Read the numbers from the input file
    with open(os.path.join(input_directory, input_file), 'r') as f:
        numbers = [float(x) * 2 for x in f.read().split()]

    # Write the numbers to the output file
    with open(os.path.join(output_directory, 'myOutput.txt'), 'w') as f:
        f.write(' '.join(map(str, numbers)))

    # Write the numbers to stderr
    print(' '.join(map(str, numbers)), file=sys.stderr)
else:
    print('No .txt file found in the input directory')
    """
    )
    
my_args=dict()
my_args['target_nresults'] = 1
my_args['min_quorum'] = 1
my_args['max_error_results'] = 1

#Iteration number
batch_number = 2
my_args['batch'] = batch_number

def pick_two_numbers():
    numbers = random.sample(range(1, 100), 2)
    result = f"{numbers[0]} {numbers[1]}"
    return result
    
def generate_random_numbers():
    numbers = [random.uniform(-1000, 1000) for _ in range(100)]
    numbers_str = ' '.join(map(str, numbers))
    return numbers_str

def inputFiles():
    inputFiles = []
    filenames = ['main.py', 'model.py', 'nodeLogger.py']

    for filename in filenames:
        with open(filename, 'r') as f:
            inputFiles.append(('shared/' + filename, f.read(), []))
    

if len(sys.argv) == 1:
    #No arguments were passed to the script
    my_input_files = []
    my_input_files.append(("shared/test.txt", generate_random_numbers(), []))
    
    #by default wu_name is app_name + pid + unix_time
    #pid = os.getpid()
    #unix_time = time.time()
    #my_args['wu_name'] = f"boinc2docker_test_{pid}_{unix_time}"
    
    #number of batch (can be used for iterations, and added to wu_name)
    #my_args['batch'] = 2
    
    #delay bound is specified in seconds
    #my_args['delay_bound'] = 600
    
    pid = os.getpid()
    unix_time = time.time()
    architecture_name = "arch1"
    my_args['wu_name'] = f"boinc2docker_{batch_number}_{architecture_name}_{pid}_{unix_time}"
    my_args['rsc_memory_bound'] = 5e9
    #my_command = ['python', '/root/shared/main.py', '/root/shared/cfg_1.json']
    #my_command = ['python', '/root/shared/test.py']
    wu = boinc2docker_create_work(image = my_image, command = my_command, create_work_args = my_args, input_files = my_input_files)
    if wu is not None: print(wu)
else:
    #Arguments were passed to the script
    #Let it be that the first argument is the number of workunits to make
    number_of_wus = int(sys.argv[1]);
    for i in range(number_of_wus):
        pick_content = pick_two_numbers()
        my_input_files = []
        my_input_files.append(("shared/test.txt", pick_content, []))
        
        pid = os.getpid()
        unix_time = time.time()
        my_args['wu_name'] = f"boinc2docker_{batch}_{pid}_{unix_time}"
        
        wu = boinc2docker_create_work(image = my_image, command = my_command, create_work_args = my_args, input_files = my_input_files)
        if wu is not None: print(wu)
    
    

