import model
import time
import sys
import json
import pickle
import os
import glob
import pdb

#Change working directory to where all the input files are (/root/shared)
#os.chdir('/root/shared')

if len(sys.argv) != 2: 
  print("Enter: main.py [path/to/config_file]")
  exit()
with open(str(sys.argv[1]), 'r') as cfg:
  config = json.load(cfg)
  for n in ['split', 'epchg']: 
    if not n in config: 
      print("Configuration error! Expected structure -> split: <int>, epchg: <int>")
      exit()
  print("The settings are loaded:")
  print("- The subset from dataset is going to be 1/" + str(config['split']))
  print("- There is going to be", config['epchg'], "epochs.")


mod = model.Model(config['split'])
for filename in glob.glob("globalModelWeights_*.pkl"):
    with open(filename, 'rb') as f:
        W = pickle.load(f)
print("Incoming global weights:\n", W[0][0][0][0])
mod.setWeights(W)

print("Starting work...")
time.sleep(3)

#while True: # Цикл обучения
g = mod.train( epochs=config['epchg'] )        # обучение и вычисление локального градиента
print("Gradients:\n", g[0][0][0][0])

with open('localGradients.pkl', 'wb') as f:
    pickle.dump(g, f)
    
print('SUCCESS')
