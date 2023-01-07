import csv
import os
import re 
import subprocess as sp

# TODO Add error handling if needed 
# TODO Weighted samples for different mazes

path = 'gen_mazes\\'

layouts = os.listdir(path)

heuristics = ['manhattanHeuristic', 'euclideanHeuristic', 'nullHeuristic']

score_re = re.compile(r'Scores:[\s]+(\-?[0-9\.]+)')
cost_re = re.compile(r'Path found with total cost of ([0-9]+)')
nodes_re =re.compile(r'Search nodes expanded:\s+([0-9]+)')

searches = ['bfs','dfs','ucs','astar','bd']

with open('results.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')
  
  header = ['layout'] + searches
  writer.writerow(header)
  for i,l in enumerate(layouts):
    print(i)
    row = []
    values = []

    for s in searches:
      for h in heuristics[:1]:
        goal = '_'.join(l.split('_')[:2])

        command = 'py pacman.py -l {3}/{0} -p SearchAgent -a fn={1},heuristic={2},goalPos={4} -q'.format(l, s, h, path, goal)
        output = sp.check_output(command, shell=True)
        output = output.decode("utf-8")
        # print(output, '_'*100)
        score = score_re.search(output)
        cost = cost_re.search(output)
        nodes = nodes_re.search(output)
        value = (float(score.group(1)), float(cost.group(1)), float(nodes.group(1)))
        values.append(str(value))
  
    row = [l] + values
    print(row)
    writer.writerow(row)