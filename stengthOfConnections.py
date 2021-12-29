import csv
from collections import defaultdict
import sys

movies = []

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv:
        if node2 not in movies:
          movies.append(node2)
        make_link(G, node1, node2)
    return G

# Read the marvel comics graph
marvelG = read_graph('marvel.txt')

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2:
                    return distance_from_start[v2]
                open_list.append(neighbor)
    return False

# path from start (after modification on distance())
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current] + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False

strength = {}
movie_length = len(movies)
count = 0
for movie in movies:
  count = count + 1
  sys.stdout.flush()
  sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * count / movie_length))
  characters = list(marvelG[movie].keys())
  for x in range(len(characters)):
    if characters[x] not in strength:
      strength[characters[x]] = {}
    for y in range(x+1, len(characters), 1):
        if characters[y] not in strength:
            strength[characters[y]] = {}

        if characters[y] not in strength[characters[x]].keys():
            (strength[characters[x]])[characters[y]] = 1
            (strength[characters[y]])[characters[x]] = 1
        else:
            (strength[characters[x]])[characters[y]] += 1
            (strength[characters[y]])[characters[x]] += 1

max_strength = 0
max_actor = ""

for actor in strength:
    for key,value in strength[actor].items():
        if value > max_strength:
            max_actor = actor+key
            max_strength = value
print (max_strength, max_actor)





