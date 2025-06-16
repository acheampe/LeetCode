from collections import deque

def hasCycleUndirectedBFS(graph):
    pass

def hasCycleUndirectedDFS(graph):
    """Detect cycle if any - return True if cyclic"""

    visited = set()
    
    def isCycle(node, parent):
        
        visited.add(node)
        
        for nei in graph[node]:
            if nei not in visited:
                if isCycle(nei, node):
                    return True
            
            #if nei is parent, then we are just backtracking
            elif nei != parent:
                return True
        
        return False
    
    for node in graph:
        #ensures we explore only unvisited components, otherwise there maybe a false result
        if node not in visited:
            # parent state is important to distinguishing when you are backtracking and when there is a cycle detection
            if isCycle(node, None):
                return True
    
    return False
            


graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

print(hasCycleUndirectedDFS(graph))

def hasCycleDirectedBFS(graph):
    pass # attempt tomorrow.
            

def hasCycleDirectedDFS(graph):
    recStack, visited = set(), set()
    
    def isCyclic(node):
        
        # visted marks fully explored nodes
        visited.add(node) # nodes in visited can be visited from a different path
        recStack.add(node) # tracks which nodes are in active path
        
        for nei in graph[node]:
            if nei not in visited:
                if isCyclic(nei):
                    return True
            if nei in recStack:
                return True
        
        recStack.remove(node) #backtrack - removes nodes from active DFS path
        return False
    
    # important for disconnected nodes
    for node in graph:
        if node not in visited:
            if isCyclic(node):
                return True
    
    return False

cyclic_digraph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

acyclic_digraph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

# print(hasCycleDirectedDFS(acyclic_digraph))
# print(hasCycleDirectedDFS(cyclic_digraph))
print(hasCycleDirectedBFS(acyclic_digraph))
print(hasCycleDirectedBFS(cyclic_digraph))