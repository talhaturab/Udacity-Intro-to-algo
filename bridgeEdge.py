# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       

from os import curdir


def check_for_red(root, leave, R):
    open_list = [root]
    check_list = [root]

    if len(R) > 0:
        direct_connection = R[root].keys()
        while (len(open_list) > 0):
            current = open_list[0]
            del open_list[0]
            for neighbour in R[current]:
                if (neighbour == leave) & (neighbour not in direct_connection):
                    return True
                if neighbour not in check_list:
                    check_list.append(neighbour)
                    open_list.append(neighbour)
    return False


def create_rooted_spanning_tree(G, root):
    S = {}

    open_list = [root]
    check_list = [root]

    while (len(open_list) > 0):
        current_root = open_list[0]
        del open_list[0]
        for leave in G[current_root]:
            if leave not in check_list:
                check_list.append(leave)
                open_list.append(leave)
                if check_for_red(current_root, leave, S) == False:
                    if current_root not in S:
                        S[current_root] = {}
                    (S[current_root])[leave] = "green"
                    if leave not in S:
                        S[leave] = {}
                    (S[leave])[current_root] = "green"

            elif check_for_red(current_root, leave, S) == True:
                    if current_root not in S:
                        S[current_root] = {}
                    (S[current_root])[leave] = "red"
                    if leave not in S:
                        S[leave] = {}
                    (S[leave])[current_root] = "red"
    return(S)

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def create_root_leaves_dict(S, root):
    open_list = [root]
    check_list = []
    root_leaves_dict = {}

    while (len(open_list) > 0):
        curent = open_list[0]
        del open_list[0]
        check_list.append(curent)
        if curent not in root_leaves_dict:
            root_leaves_dict[curent] = {}
        for neighbor in S[curent].keys():
            if (neighbor not in check_list) & (S[curent][neighbor] == "green"):
                (root_leaves_dict[curent])[neighbor] = 1
                open_list.append(neighbor)

    return (root_leaves_dict)


def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    open_list = [root]
    order_number = 0
    order = {}
    x = 0
    root_leaves_dict = create_root_leaves_dict(S, root)

    while (len(open_list) > 0):
        current = open_list[x]
        leaves_marked = True
        for neighbor in root_leaves_dict[current].keys():
            if neighbor not in order.keys():
                open_list.append(neighbor)
                leaves_marked = False
        
        if leaves_marked:        
            order_number = order_number + 1
            order[current] = order_number
            del open_list[x]

        x = len(open_list) - 1
    
    return order

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    root_leaves_dict = create_root_leaves_dict(S, root)
    number_of_descendants = {}

    for point in root_leaves_dict.keys():
        open_list = [point]
        count = 1
        while (len(open_list) > 0):
            current = open_list[0]
            del open_list[0]
            for neigbour in root_leaves_dict[current].keys():
                open_list.append(neigbour)
                count += 1
        number_of_descendants[point] = count
    return number_of_descendants

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def create_root_leaves_dict_with_red(S, root):
    open_list = [root]
    check_list = []
    root_leaves_dict = {}

    while (len(open_list) > 0):
        curent = open_list[0]
        del open_list[0]
        check_list.append(curent)
        if curent not in root_leaves_dict:
            root_leaves_dict[curent] = {}
        for neighbor in S[curent].keys():
            if (neighbor not in check_list) & (S[curent][neighbor] == "green"):
                (root_leaves_dict[curent])[neighbor] = 1
                open_list.append(neighbor)
            if S[curent][neighbor] == "red":
                (root_leaves_dict[curent])[neighbor] = 1

    return (root_leaves_dict)

def create_order_in_sequence(root, order):
    order_in_sequence = [root]
    open_list = [root]
    while (len(open_list) > 0):
        current = open_list[0]
        del open_list[0]
        for neighbour in order[current]:
            if neighbour not in order_in_sequence:
                order_in_sequence.insert(0, neighbour)
                open_list.append(neighbour)
    return order_in_sequence

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    
    root_leaves_dict = create_root_leaves_dict_with_red(S, root)
    order_in_sequence = create_order_in_sequence(root, root_leaves_dict)
    lpo = {}

    for element in order_in_sequence:
        lowest = po[element]
        for neigbour in root_leaves_dict[element]:
            if po[neigbour] < lowest:
                lowest = po[neigbour]
            if neigbour in lpo.keys():
                if lpo[neigbour] < lowest:
                    lowest = lpo[neigbour]
        lpo[element] = lowest

    return lpo

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    root_leaves_dict = create_root_leaves_dict_with_red(S, root)
    order_in_sequence = create_order_in_sequence(root, root_leaves_dict)
    hpo = {}

    for element in order_in_sequence:
        highest = po[element]
        for neigbour in root_leaves_dict[element]:
            if po[neigbour] > highest:
                highest = po[neigbour]
            if neigbour in hpo.keys():
                if hpo[neigbour] > highest:
                    highest = hpo[neigbour]
        hpo[element] = highest

    return hpo

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    
    rooted_spanning_tree = create_rooted_spanning_tree(G, root)
    po = post_order(rooted_spanning_tree, root,)
    no_of_descendants = number_of_descendants(rooted_spanning_tree, root)
    lpo = lowest_post_order(rooted_spanning_tree, root, po)
    hpo = highest_post_order(rooted_spanning_tree, root, po)
    root_leaves = create_root_leaves_dict(rooted_spanning_tree, root)
    bridges = []

    for element in rooted_spanning_tree.keys():
        if (hpo[element] <= po[element]) & (lpo[element] > (po[element] - no_of_descendants[element])):
            if element != root:
                bridges.append(element)

    for root in root_leaves.keys():
        for x in root_leaves[root].keys():
            if x == bridges[0]:
                bridges.append(root)
    
    bridge_edges_elements = [(bridges[1], bridges[0])]
    return bridge_edges_elements


def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

test_bridge_edges()