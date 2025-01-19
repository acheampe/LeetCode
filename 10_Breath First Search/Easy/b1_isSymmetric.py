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

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        BFS implementation to check if a binary tree is symmetric.
        """

        def symmetric(currNode, trackSymmetry):
            """return if tree is symmetric"""

            
            if currNode.left and currNode.right:
                trackSymmetry.append(currNode.left.val)
                trackSymmetry.appendleft(currNode.right.val)
                symmetric(currNode.left, trackSymmetry)
                symmetric(currNode.right, trackSymmetry)
            
            elif currNode.left and not currNode.right:
                trackSymmetry.appendleft(currNode.left.val) 
                symmetric(currNode.left, trackSymmetry)

            elif currNode.right and not currNode.left:
                trackSymmetry.appendleft(currNode.left.val)
                symmetric(currNode.right, trackSymmetry)                           

        trackSymm = deque()
        symmetric(root, trackSymm)

        while trackSymm:
            if trackSymm.popleft() !=  trackSymm.pop():
                return False
        return True

# Test cases
def run_tests():
    tests = [
        {
            "input": [1, 2, 2, 3, 4, 4, 3],
            "expected": True
        },
        {
            "input": [1, 2, 2, None, 3, None, 3],
            "expected": False
        },
        {
            "input": [1],
            "expected": True
        },
        {
            "input": [],
            "expected": True
        },
        {
            "input": [1, 2, 2, 3, None, None, 3],
            "expected": False
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"])
        result = solution.isSymmetric(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()