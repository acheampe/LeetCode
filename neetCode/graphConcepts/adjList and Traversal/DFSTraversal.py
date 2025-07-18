def DFSTraversal(graph):
    stack = []
    visited = set()
    result = []

    stack.append('A')
    
    while stack:
        curr = stack.pop()
        
        if curr in visited:
            continue
        
        visited.add(curr)
        result.append(curr)
        
        for nei in reversed(graph[curr]):
            if nei not in visited:
                stack.append(nei)

    return result

inputGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(DFSTraversal(inputGraph))  # ['A', 'B', 'D', 'E', 'F', 'C']