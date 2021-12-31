def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 100000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node


def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!                                                                                                                                                                                     
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                new_dist = final_dist[w] + G[w][x]
                if (x not in dist_so_far) or (new_dist < dist_so_far[x]):
                    dist_so_far[x] = new_dist
    return final_dist

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

(a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
            (e,g,1),(e,f,5),(f,g,2),(b,f,1))
G = {}
for (i,j,k) in triples:
    make_link(G, i, j, k)

dist = dijkstra(G, a)
print(dist)