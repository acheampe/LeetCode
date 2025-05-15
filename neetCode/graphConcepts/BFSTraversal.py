from collections import deque

def BFSTraversal(graph):
    """Traverse Graph using BFS"""
    
    queue = deque()
    visited = set()
    result = []

    queue.append('A')
    visited.add('A')  # Add here to prevent duplicate entries

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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