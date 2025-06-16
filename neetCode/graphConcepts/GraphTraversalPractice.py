from collections import deque

def DFSTraversal(graph):
    
    stack = []
    visited = set()
    
    stack.append("A")
    visited.add("A")
    
    result = []
    
    while stack:
        
        curr = stack.pop()
        result.append(curr)
        
        for con in reversed(graph[curr]):
            if con not in visited:
                stack.append(con)
                visited.add(con) 
    
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


def DFSRecursive(graph):
    
    visited = set()
    
    def dfs(node):
        
        if not node or node in visited:
            return None

        result.append(node)
        visited.add(node)
        
        for nei in graph[node]:
            dfs(nei)
    
    result = []
    dfs("A")
        
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

def BFSTraversal(graph):
    """Traverse Graph using BFS"""
    
    stack = deque()
    visited = set()
    
    stack.append("A")
    visited.add("A")
    
    result = []
    
    while stack:
        
        curr = stack.popleft()
        result.append(curr)
        
        for con in graph[curr]:
            if con not in visited:
                stack.append(con)
                visited.add(con)
    
    return result
    

inputGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(BFSTraversal(inputGraph))  # ['A', 'B', 'C', 'D', 'E', 'F']