#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 

import heapq

def dijkstra(G,v):
    dist_so_far = [(0, v)]
    final_dist = {}
    final_dist[v] = 0
    while len(dist_so_far) > 0:
        current_distance, current_vertex = heapq.heappop(dist_so_far)
        for vertex, weight in G[current_vertex].items():
            distance = current_distance + weight
            if (vertex not in final_dist) or (distance < final_dist[vertex]):
                final_dist[vertex] = distance
                heapq.heappush(dist_so_far, (distance, vertex))
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)