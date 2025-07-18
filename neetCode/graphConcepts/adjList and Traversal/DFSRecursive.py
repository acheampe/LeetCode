def DFSRecursive(graph):
    
    result = []
    
    def recur(node):
        
        if not node or node in visited or node not in graph:
            return

        result.append(node)
        visited.add(node)
        
        for nei in graph[node]:
            recur(nei)
    
    visited = set()
    
    recur('A')
    
    return result
inputGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(DFSRecursive(inputGraph))  # ['A', 'B', 'D', 'E', 'F', 'C']