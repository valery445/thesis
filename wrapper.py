import sys
import random
import os
import time
sys.path.append('/home/boincadm/projects/boincdocker/bin')
from bin.boinc2docker_create_work import boinc2docker_create_work



my_image = "python:3-slim"
my_command = ['python', '-c']

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
        numbers = [int(x) * 2 for x in f.read().split()]

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

def pick_two_numbers():
    numbers = random.sample(range(1, 100), 2)
    result = f"{numbers[0]} {numbers[1]}"
    return result

if len(sys.argv) == 1:
    #No arguments were passed to the script
    my_input_files = []
    my_input_files.append(("shared/test.txt", "20 30", []))
    pid = os.getpid()
    unix_time = time.time()
    my_args['wu_name'] = f"boinc2docker_test_{pid}_{unix_time}"
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
        wu = boinc2docker_create_work(image = my_image, command = my_command, create_work_args = my_args, input_files = my_input_files)
        if wu is not None: print(wu)
    
    

