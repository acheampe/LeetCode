from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        """
        return total paths where the sum of values will equal
        targetSum
        TC and SC O(n)
        """

        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        def pathSearch(node, currSum):
            
            if not node:
                return
            
            currSum += node.val

            self.counter += prefixSums[currSum - targetSum]
            
            prefixSums[currSum] += 1

            pathSearch(node.left, currSum)
            pathSearch(node.right, currSum)

            prefixSums[currSum] -= 1

        self.counter = 0
        pathSearch(root, 0)

        return self.counter


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
        # {
        #     "input": {
        #         "root": [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1],
        #         "targetSum": 8
        #     },
        #     "expected": 3
        # },
        # {
        #     "input": {
        #         "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
        #         "targetSum": 22
        #     },
        #     "expected": 3
        # },
        # {
        #     "input": {
        #         "root": [],
        #         "targetSum": 0
        #     },
        #     "expected": 0
        # },
        {
            "input": {
                "root": [1, -2, -3, 1, 3, -2, None, -1],
                "targetSum": -1
            },
            "expected": 4
        },
        # {
        #     "input": {
        #         "root": [1],
        #         "targetSum": 1
        #     },
        #     "expected": 1
        # }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"]["root"])
        targetSum = test["input"]["targetSum"]
        result = solution.pathSum(root, targetSum)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()