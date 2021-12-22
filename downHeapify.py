# import random
# L = [random.randrange(90)+10 for i in range(20)]
L = [50,25,26,56,26,49,35,59,78,71,55,61,88,56]

# Heap shortcuts
def left(i):
  return i*2+1
def right(i):
  return i*2+2
def parent(i):
  return (i-1)/2
def root(i):
  return i == 0
def leaf(L, i):
  return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i):
  return right(i) == len(L)

def down_heapify(L, i):
  if leaf(L, i):
    return

  if one_child(L, i):
    if L[i] > L[left(i)]:
      (L[i], L[left(i)]) = (L[left(i)], L[i])
    return

  if min(L[left(i)], L[right(i)]) >= L[i]:
    return

  if L[left(i)] < L[right(i)]:
    (L[i], L[left(i)]) = (L[left(i)], L[i])
    down_heapify(L, left(i))
    return

  (L[i], L[right(i)]) = (L[right(i)], L[i])
  down_heapify(L, right(i))
  return

print(L)
down_heapify(L, 0)
print(L)