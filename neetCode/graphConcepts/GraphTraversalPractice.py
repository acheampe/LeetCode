from collections import deque

def DFSTraversal(graph):
    pass

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
    pass
    
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
    
    pass

inputGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(BFSTraversal(inputGraph))  # ['A', 'B', 'C', 'D', 'E', 'F']