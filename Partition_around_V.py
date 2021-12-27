#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

L = [4, 3, 2, 1]
v = 2

def partition(L, v):
    P = []
    P.append(v)
    for x in L:
        if x > v:
            P.append(x)
        elif x < v:
            P.insert(0, x)
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos

partition(L, v)