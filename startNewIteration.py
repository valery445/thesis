import os
import pickle
import json
import pdb
import sys
import subprocess
from create_wus import create_wus
from db_deleteUnsentJobs import db_deleteUnsentJobs
from makeIterationTemplate import makeIterationTemplate

def startNewIteration(projectFolder, agr, newWorkunitNumber):
    # Set the paths for the directories and files
    modelFolder = os.path.join(projectFolder, 'model')
    learningFile = os.path.join(modelFolder, 'learning.json')
    with open(learningFile, 'r') as f:
        data = json.load(f)
    
    # Load the global weights file
    W0_file = os.path.join(modelFolder, 'globalModels/') + f"globalModelWeights_{data['iterationNumber']}.pkl"
    with open(W0_file, 'rb') as f:
        W0 = pickle.load(f)
    # Log global values before change
    i_val = os.path.join(modelFolder, 'logs', 'new_iteration_values.txt')
    with open(i_val, 'a') as f:
        f.write('Global model before:')
        f.write(str(W0[0][0][0][0]))
        f.write('\n')
    # Log agregation to be added
        f.write('Agregated count:')
        f.write(str(data['agregatedCount']))
        f.write('\n')
        f.write('Agregation:')
        f.write(str(agr[0][0][0][0]))
        f.write('\n')
            
    # Update global weights using agregation and agregated count from learning file
    W = W0.copy()
    for l, _ in enumerate(agr):
        W[l] = W0[l] + agr[l] / data['agregatedCount']
                
    # Log global values after change
    with open(i_val, 'a') as f:
        f.write('Global model AFTER:')
        f.write(str(W[0][0][0][0]))
        f.write('\n\n')
            
    # Increment iteration number and reset agregated count to 0 in learning file
    data['iterationNumber'] += 1
    data['agregatedCount'] = 0
            
    # Save the updated global weights
    W_file = os.path.join(modelFolder, 'globalModels/') + f"globalModelWeights_{data['iterationNumber']}.pkl"
    with open(W_file, 'wb') as f:
        pickle.dump(W, f)
             
    # Empty agregation file
    empty = list(agr[i]-agr[i] for i,_ in enumerate(agr))
    with open(os.path.join(modelFolder, 'agregation.pkl'), 'wb') as f:
        pickle.dump(empty, f)
            
    with open(learningFile, 'w') as f:
        json.dump(data, f, indent=4)
            
    # Deletes results and workunits of older iteration which haven't been sent yet
    db_deleteUnsentJobs("virtualbox", data['iterationNumber'] - 1)
            
    # Stage new globalModelWeights_n.pkl
    os.chdir(projectFolder)
    shell_script = './bin/stage_file'
    args = ['--copy', W_file]
    subprocess.check_output([shell_script] + args)
            
    # Make new input template
    template = makeIterationTemplate(projectFolder, data['iterationNumber'])
    # Create newWorkUnitNumber of wus with batch equal to iteration number and new template
    create_wus(newWorkunitNumber, data['iterationNumber'], template)
