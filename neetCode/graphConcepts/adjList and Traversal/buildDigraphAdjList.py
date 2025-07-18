from collections import defaultdict

def adjListFromDigraph(directedEdges) -> dict:
    
    digraph = defaultdict(set)
    
    for node1, node2 in directedEdges:
        digraph[node1].add(node2) # only node1 to node2 (directed graph)
        
    return {key : list(nodes) for key, nodes in digraph.items()}

edges = [
    ["A", "B"],
    ["A", "C"],
    ["B", "D"],
    ["C", "D"]
]

print(adjListFromDigraph(edges))


def adjListFromWeightedDigraph(directedEdges) -> dict:
    
    digraph = defaultdict(list)
    
    for node1, node2, weight in directedEdges:
        digraph[node1].append((node2, weight)) # only node1 to node2 (directed graph)
        
    return digraph

weighted_edges = [
    ["A", "B", 5],
    ["A", "C", 2],
    ["B", "D", 4],
    ["C", "D", 7]
]

print(adjListFromWeightedDigraph(weighted_edges))


def weightedMatrixToAdjList(matrix, nodes) -> dict:
    
    weightedGraph = defaultdict(list)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if matrix[i][j] != float('inf') and i != j:
                weightedGraph[nodes[i]].append((nodes[j], matrix[i][j]))
    
    return weightedGraph

matrix = [
    [0,  3, float('inf'), 7],
    [8,  0, 2,            float('inf')],
    [5, float('inf'), 0,  1],
    [2, float('inf'), float('inf'), 0]
]

nodes = ['A', 'B', 'C', 'D']

print(weightedMatrixToAdjList(matrix, nodes))