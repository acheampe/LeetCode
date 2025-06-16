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
    pass

def hasCycleDirectedDFS(graph):
    pass

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

print(hasCycleDirectedDFS(acyclic_digraph))
print(hasCycleDirectedDFS(cyclic_digraph))
print(hasCycleDirectedBFS(acyclic_digraph))
print(hasCycleDirectedBFS(cyclic_digraph))