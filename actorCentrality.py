import csv
from collections import defaultdict
import sys
actors_list = []
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
    tsv = csv.reader(open(filename), delimiter="\t")
    G = {}
    for (node1, node2, node3) in tsv:
        if node1 not in actors_list:
          actors_list.append(node1)
        make_link(G, node1, (node2+node3))
    return G    

# Read the imdb graph
marvelG = read_graph('imdb-1.tsv')

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
                if neighbor == v2: return distance_from_start[v2]
                open_list.append(neighbor)
    return False

# path from start (after modification on distance())
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

centrality_list = {}
count = 0
len_actor = len(actors_list)
for actor in actors_list:
    centrality_list[actor] = centrality(marvelG, actor)
    count = count + 1
    sys.stdout.flush()
    sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * count / len_actor))

# minimum = centrality_list[actors_list[0]]
# actor_name = ""
# for actor in centrality_list.keys():
#   if centrality_list[actor] < minimum:
#     minimum = centrality_list[actor]
#     actor_name = actor

top_centrality = {}
number = 1
for k, v in sorted(centrality_list.items(), key=lambda item: item[1]):
    top_centrality[number] = {}
    (top_centrality[number])[k] = v
    if number > 19:
      print(top_centrality)
      break
    else:
      number += 1
    