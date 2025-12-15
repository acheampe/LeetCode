from collections import OrderedDict # combination of Linkedlist and deque data structure

storage = OrderedDict()
"""“An OrderedDict is implemented as a hash map that maps keys to nodes in a 
doubly linked list. The hash map provides O(1) access to the node, and the linked 
list provides O(1) reordering and eviction. Because we already have the node reference, 
we never traverse the list.”"""

storage['A'] = 12
storage['B'] = 13
storage['C'] = 14

print(storage.keys()) # reinserting keys does not remov

storage['A'] = 15

print(storage.keys()) # reinserting keys does not move key

del storage['A']
storage['A'] = 16

print(storage.keys())

# move most recently used, (Move 'B)
storage.move_to_end('B')

print(storage.keys())

# evict least recently used
storage.popitem(last=False)
print(storage.keys())