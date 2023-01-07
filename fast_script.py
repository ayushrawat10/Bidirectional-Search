import csv
import os
import re 
import subprocess as sp
import time
start = time.time()
# your code here    

# TODO Add error handling if needed 
# TODO Weighted samples for different mazes

from threading import Thread
from time import sleep

def threaded_function(layouts, i):
  output(layouts, i)

def output(layouts, i):
  with open('results_{0}.csv'.format(i), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    
    header = ['layout'] + searches
    writer.writerow(header)
    print(i)
    for l in layouts:
      row = []
      values = []

      for s in searches:
        for h in heuristics[:1]:
          goal = '_'.join(l.split('_')[:2])

          command = 'py pacman.py -l {3}/{0} -p SearchAgent -a fn={1},heuristic={2},goalPos={4} -q'.format(l, s, h, path, goal)
          output = sp.check_output(command, shell=True)
          output = output.decode("utf-8")

          score = score_re.search(output)
          cost = cost_re.search(output)
          nodes = nodes_re.search(output)
          value = (float(score.group(1)), float(cost.group(1)), float(nodes.group(1)))
          values.append(str(value))
    
      row = [l] + values
      print(row)
      writer.writerow(row)
  
path = 'gen_mazes\\'
print(os.getcwd())

layouts = os.listdir(path)
print(os.getcwd())

print(path)
layouts.sort()
# layouts = layouts[:100]
n = len(layouts)

heuristics = ['manhattanHeuristic', 'euclideanHeuristic', 'nullHeuristic']
score_re = re.compile(r'Scores:[\s]+(\-?[0-9\.]+)')
cost_re = re.compile(r'Path found with total cost of ([0-9]+)')
nodes_re =re.compile(r'Search nodes expanded:\s+([0-9]+)')
searches = ['bfs','dfs','ucs','astar','bd']

j=0
threads = []
for i in range(100):
  z = int(j + n/100)
  # print(z, 'asd')
  threads.append(Thread(target = threaded_function, args = (layouts[j:z+1], i+100)))
  j = z+1
  print("thread finished...exiting")

for t in threads:
  t.start()

for t in threads:
  t.join()

print(time.time() - start)


