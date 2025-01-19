from typing import Optional, List

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        return the maximum path sum of a given tree
        """

        # TIME COMPLEXITY  = O(n) visits all nodes ones
        # SPACE COMPLEXITY = Average case O(log n) --> O(n) if tree is skewed
        # Iterative Approach

        # Step 1: Establish memory/space needed for operation
        currNode = root
        stack = []
        self.maxSum = float('-inf')

        while currNode or stack:

            # s1: explore leftmost branch
            while currNode.left and currNode.right:
                stack.append(currNode, currNode.right, currNode.left)
                currNode = currNode.left
            
            # s2: Update maxSum
            currNode = stack.pop()
            leftSum = max(currNode.val, 0) # ignore negative


            
             



# Test cases
def run_tests():
    tests = [
        {
            "input": {
                "root": [1, 2, 3]
            },
            "expected": 6
        },
        {
            "input": {
                "root": [-10, 9, 20, None, None, 15, 7]
            },
            "expected": 42
        },
        {
            "input": {
                "root": [-3]
            },
            "expected": -3
        },
        {
            "input": {
                "root": [1, -2, 3]
            },
            "expected": 4
        },
        {
            "input": {
                "root": [2, -1]
            },
            "expected": 2
        },
        # {
        #     "input": {
        #         "root": [10, 2, 10, None, None, -20, 1]
        #     },
        #     "expected": 22
        # },
        {
            "input": {
                "root": [1,2,None,3,None,4,None,5]
            },
            "expected": 15
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"]["root"])
        result = solution.maxPathSum(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()
