import array
from collections import defaultdict

# def buildAjGraph(edges: list[list[str]]) -> dict:
#     undirectedGraph = defaultdict(set)

#     for node1, node2 in edges:
#         undirectedGraph[node1].add(node2)
#         undirectedGraph[node2].add(node1)
    
#     return {node : list(neighbors) for node, neighbors in undirectedGraph.items()}
        
   
   		
# print(buildAjGraph( [
#     ["A", "B"],
#     ["A", "C"],
#     ["B", "D"],
#     ["C", "D"],
#     ["E", "F"]
# ]))

# def buildAjGraphFromTuple(edges: list[tuple]) -> dict:
#     undirectedGraph = defaultdict(set)

#     for node1, node2, weight in edges:
#         undirectedGraph[node1].add((node2, weight))
#         undirectedGraph[node2].add((node1, weight))
    
#     return {node : list(neighbors) for node, neighbors in undirectedGraph.items()}
        
   
   		
# print(buildAjGraphFromTuple([("A", "B", 3), ("A", "C", 4), ("B", "D", 5), ("C", "D", 8), ("E", "F", 6)]))

def buildAjGraphFromMatrix(matrix: list[list[int]], nodes: list[str]) -> dict:
    assert len(matrix) == len(nodes), "Number of rows in matrix must match number of nodes."
    for row in matrix:
        assert len(row) == len(nodes), "Each row in matrix must have length equal to number of nodes."

    undirectedGraph = defaultdict(set)

    for index, array in enumerate(matrix):
        for j, val in enumerate(array):
            if val == 1:
                undirectedGraph[nodes[index]].add(nodes[j])
    
    return {key: list(neighbors) for key, neighbors in undirectedGraph.items()}
        
   
#        A  B  C  D
matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0],  # D
]
nodes = ["A", "B", "C", "D"]
 		
print(buildAjGraphFromMatrix(matrix, nodes))