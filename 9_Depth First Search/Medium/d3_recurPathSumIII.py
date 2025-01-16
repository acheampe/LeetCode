from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         """
#         return number of paths that eventually sums up to targetSum along 
#         its path
#         """

#         if not root:
#             return 0 # cant sum up to targetSum if there is no path
        
#         self.pathCount = 0
#         path = deque()
#         pathSum = 0

#         self.pathCountHelper(root, targetSum, path, pathSum)

#         return self.pathCount

#     def pathCountHelper(self, node, targetSum, path, pathSum):
#         """
#         count valid paths that can sum up to target
#         """


#         if not node:
#             return
        
#         path.append(node.val)
#         pathSum += node.val

#         if pathSum == targetSum:
#             self.pathCount += 1
#             pathSum -= path.popleft()

#         elif not node.left and not node.right and pathSum > targetSum: # reduce pathSum value
#             while path and pathSum > targetSum:
#                 pathSum -= path.popleft()

#                 if pathSum == targetSum:
#                     self.pathCount += 1
        
#         elif pathSum > targetSum:
#             pathSum -= path.popleft()
        
#         self.pathCountHelper(node.left, targetSum, path + deque([]), pathSum)
#         self.pathCountHelper(node.right, targetSum, path + deque([]), pathSum)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Return the number of paths where the sum of the values equals targetSum.
        """

        if not root:
            return 0 
        
        self.pathCount = 0

        if root.val == targetSum:
            self.pathCount += 1
        
        return self.trackValidPaths(root, targetSum + root.val)

    def trackValidPaths(self, currNode, sumTarget):
        """
        Count valid paths and return count
        """

        if not currNode:
            return
        
        if currNode.val == sumTarget:
            print(currNode.val)
            self.pathCount += 1
        
        if currNode.left:
            print(currNode.left.val)
            currNode.left.val = currNode.val + currNode.left.val 

        if currNode.right:
            print(currNode.right.val)
            currNode.right.val = currNode.val + currNode.right.val
        
        self.trackValidPaths(currNode.left, sumTarget)
        self.trackValidPaths(currNode.right, sumTarget)

        return self.pathCount

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
        {
            "input": {
                "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
                "targetSum": 22
            },
            "expected": 3
        },
        # {
        #     "input": {
        #         "root": [],
        #         "targetSum": 0
        #     },
        #     "expected": 0
        # },
        # {
        #     "input": {
        #         "root": [1, -2, -3, 1, 3, -2, None, -1],
        #         "targetSum": -1
        #     },
        #     "expected": 4
        # },
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