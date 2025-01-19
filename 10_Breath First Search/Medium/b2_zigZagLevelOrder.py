from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

class Solution: # TC = O(n) SC = O(w) for width of tree and O(n) for result
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        return the zigzag level order traversal of its nodes' values. 
        (i.e., from left to right, then right to left for the next level and alternate between)
        """

        # S1: if no root:
        if not root:
            return []

        # S2: establish memory/variables needed for operation
        result = []
        qstack = deque()
        qstack.append((root, 0)) # node and it's corresponding level

        while qstack:

            currNode, currLevel = qstack.popleft()

            if len(result) == currLevel:
                result.append([])
            
            if (currLevel % 2 )!= 0:
                result[currLevel].insert(0, currNode.val)
            else:
                result[currLevel].append(currNode.val)


            if currNode.left:
                qstack.append((currNode.left, currLevel + 1))
            if currNode.right:
                qstack.append((currNode.right, currLevel + 1))

        return result
        
# Test cases for the zigzagLevelOrder method
def run_tests():
    tests = [
        {
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [20, 9], [15, 7]]
        },
        {
            "input": [1],
            "expected": [[1]]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [[1], [3, 2], [4, 5, 6, 7]]
        },
        {
            "input": [1, None, 2, None, 3, None, 4],
            "expected": [[1], [2], [3], [4]]
        },
        {
            "input": [1, 2, 3, 4, None, None, 5],
            "expected": [[1], [3, 2], [4, 5]]
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"])
        result = solution.zigzagLevelOrder(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")
        if result != test["expected"]:
            print(f"  Expected: {test['expected']}, Got: {result}")

# Run the tests
run_tests()