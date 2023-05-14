import model
import time
import sys
import json
import pickle
import os
import pdb

#Change working directory to where all the input files are (/root/shared)
#os.chdir('/root/shared')

# Redirect all print output to stderr
#sys.stdout = sys.stderr

if len(sys.argv) != 2: 
  print("Введите: main.py [путь/к/конфигу]")
  exit()
with open(str(sys.argv[1]), 'r') as cfg:
  config = json.load(cfg)
  for n in ['split', 'input', 'node', 'addr', 'epchg']: 
    if not n in config: 
      print("Ошибка конфигурации! Необходима структура -> split: <int>, input: <int>, epchg: <int>, node*: [<str>, <int>], addr: [ node1, ..., nodeN ]")
      exit()
  print("Настройки загружены:")
  print("- От датасета будет взята 1/" + str(config['split']))
  print("- Градиенты будут ожидаться от", config['input'], "клиентов")
  print("- Обмен градиентами после обучения, равного", config['epchg'], "эпохам.")
  print("- Хост (адрес для приёма):", config['node'][0], ":", config['node'][1])
  print("- Узлы для отправки:")
  for d in config['addr']:
    print("  *", d[0], ":", d[1])

#net = sock.NetworkNode(config['node'], config['addr'])
mod = model.Model(config['split'], '_'.join(map(str,config['node'])) + ".log")
with open('globalModelWeights.pkl', 'rb') as f:
    W = pickle.load(f)
#with open('/home/boincadm/projects/boincdocker/thesis/Weights_non_binary.txt', 'w') as f:
#    f.write(W)
mod.setWeights(W)
print("Начало работы...")
time.sleep(3)

#while True: # Цикл обучения
g = mod.train( epochs=config['epchg'] )        # обучение и вычисление локального градиента
# Write list to file
#with open('/root/shared/results/gradients.pkl', 'wb') as f:
#    pickle.dump(g, f)
with open('localGradients.pkl', 'wb') as f:
    pickle.dump(g, f)
#print(g)
#print('SUCCESS', file=sys.stderr)
'''
  net.sendData( g )                       # рассылка градиентов
  while net.waitGrads( config['input'] ): # ожидание градиентов от заданного количества входящих узлов
    print("Ожидание получения градиентов от всех узлов... [" + str(len(net.recieved)) + "/" + str(config['input']) + "]", end="\r")
    time.sleep(1)
  print("Все градиенты загружены!" + " "*10, end="\r")
  mod.applyAggGrads([g] + net.recieved, [1.0] + [0.25] * len(net.recieved))
  print("Градиенты применены... Перевычисление значения точности:")
  mod.checkAccuracy() 
  net.clearRecv()      # очистка от старых принятых градиентов
  mod.random_dataset() # произвести перевыборку датасета
'''
