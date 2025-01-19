from typing import Optional, List
from collections import deque, defaultdict

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

class Solution: # Time Complexity = O(n) Space = O(h)/ O (log n), worst case O(n) for skewed
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        return node vals in tree by level ordered array groupings 
        """
        #S1: Edge case - if no tree
        if not root:
            return []

        # S2: establish memory/variable needed for operation
        qStack = deque()
        level = 0
        qStack.append((root, level))
        result = []

        while qStack:

            # Prep current level to append to hashmap
            currNode, currLevel = qStack.popleft()

            # S3: Append a new list if appropriate
            if len(result) == currLevel:
                result.append([])
            
            # S4: Append val to appropriate level
            result[currLevel].append(currNode.val)

            if currNode.left:
                qStack.append((currNode.left, currLevel + 1))
            if currNode.right:
                qStack.append((currNode.right, currLevel + 1))
        
        return result

# Test cases for the levelOrder method
def run_tests():
    tests = [
        {
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [9, 20], [15, 7]]
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
            "expected": [[1], [2, 3], [4, 5, 6, 7]]
        },
        {
            "input": [1, None, 2, None, 3, None, 4],
            "expected": [[1], [2], [3], [4]]
        },
        {
            "input": [1, 2, 3, 4, None, None, 5],
            "expected": [[1], [2, 3], [4, 5]]
        },
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"])
        result = solution.levelOrder(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")
        if result != test["expected"]:
            print(f"  Expected: {test['expected']}, Got: {result}")

# Run the tests
run_tests()