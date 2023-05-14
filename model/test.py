import os
import sys

sys.stdout = sys.stderr

os.chdir('/root/shared')

if os.path.exists('sharedModel.h5'):
    print('sharedModel.h5 exists in the current directory.')
else:
    print('sharedModel.h5 does not exist in the current directory.')

if os.access('sharedModel.h5', os.R_OK):
    print('You have permission to read sharedModel.h5.')
else:
    print('You do not have permission to read sharedModel.h5.')
    


if os.path.exists('CaSeTEST.txt'):
    print('CaSeTEST.txt exists in the current directory.')
else:
    print('CaSeTEST.txt does not exist in the current directory.')

if os.access('CaSeTEST.txt', os.R_OK):
    print('You have permission to read CaSeTEST.txt.')
else:
    print('You do not have permission to read CaSeTEST.txt.')

    
if os.path.exists('case_test.txt'):
    print('case_test.txt exists in the current directory.')
else:
    print('case_test.txt does not exist in the current directory.')

if os.access('case_test.txt', os.R_OK):
    print('You have permission to read case_test.txt.')
else:
    print('You do not have permission to read case_test.txt.')
    
    
# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print(f'Current working directory: {cwd}')

# Get a list of all files in the current working directory
files = os.listdir(cwd)

# Print the list of files
print('Files in the current working directory:')
for file in files:
    print(file)
