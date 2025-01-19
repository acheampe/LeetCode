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

        trackSym = deque()

        # S1: duplicate and append initial roots
        trackSym.append((root.left, root.right))

        while trackSym:

            node1, node2 = trackSym.popleft()

            # True condition
            if not node1 and not node2:
                continue

            # S2: Find conditions that presents as false
            if not node2 or not node1 or node1.val != node2.val:
                return False
            
            # S3: Add to queue
            trackSym.append((node1.left, node2.right)) # Outer pair
            trackSym.append((node1.right, node2.left)) # Inner pain

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
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"])
        result = solution.isSymmetric(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()