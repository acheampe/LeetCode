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

        def deepSearch(currNode, currSum):
            """
            deep tree traversal for max path Sum
            """

            if not currNode:
                return 
            
            # Step One: find curr maxsum
            self.maxSum = max(self.maxSum, currSum, currNode.val)

            # Step Two: Compare node val to currSum
            if currNode.left and currNode.right:
                self.maxSum = max(self.maxSum, currNode.left.val + currNode.right.val + currNode.val)
            if currNode.left:
                deepSearch(currNode.left, currSum + currNode.left.val)
            if currNode.right:
                deepSearch(currNode.right, currSum + currNode.right.val)
    

        self.maxSum = float('-inf')
        deepSearch(root, root.val)
        return self.maxSum

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
        {
            "input": {
                "root": [10, 2, 10, None, None, -20, 1]
            },
            "expected": 22
        },
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
