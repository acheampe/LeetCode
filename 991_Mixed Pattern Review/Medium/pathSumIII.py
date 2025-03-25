from collections import defaultdict
from os import path

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: ### RECURSIVE APPROACH ####

    def pathSum(self, root: TreeNode, targetSum: int):
        """
        return the number of paths whose sum equal targetSum
        
        TC: O(n)
        SC: O(n) due to stack + pathTotal
        """
        
        pathTotal = defaultdict(int)
        pathTotal[0] = 1 # initialize 0 val
        
        def deepSearch(node, currSum):
            
            # Base case:
            if node == None:
                return 

            currSum += node.val
   
            self.validCounter += pathTotal[currSum - targetSum]
            
            pathTotal[currSum] += 1 
            
            deepSearch(node.left, currSum)
            deepSearch(node.right, currSum)
            
            # backtrack
            pathTotal[currSum] -= 1


        self.validCounter = 0
        deepSearch(root, 0)
        
        return self.validCounter
    


# Helper function to build a binary tree from a list
def build_tree(values: list[int]) -> TreeNode:
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

# Test cases
def run_tests():
    tests = [
        {
            "input": {
                "root": [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1],
                "targetSum": 8
            },
            "expected": 3
        },
        {
            "input": {
                "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
                "targetSum": 22
            },
            "expected": 3
        },
        {
            "input": {
                "root": [],
                "targetSum": 0
            },
            "expected": 0
        },
        {
            "input": {
                "root": [1, -2, -3, 1, 3, -2, None, -1],
                "targetSum": -1
            },
            "expected": 4
        },
        {
            "input": {
                "root": [1],
                "targetSum": 1
            },
            "expected": 1
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"]["root"])
        targetSum = test["input"]["targetSum"]
        result = solution.pathSum(root, targetSum)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()