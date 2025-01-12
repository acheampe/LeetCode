from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        return True if tree has a root to leaf path that sums up to targetSum
        """

        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)

            
# Helper function to construct a binary tree from a list
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
        {
            "input": {
                "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                "targetSum": 22
            },
            "expected": True
        },
        # {
        #     "input": {
        #         "root": [1, 2, 3],
        #         "targetSum": 5
        #     },
        #     "expected": False
        # },
        # {
        #     "input": {
        #         "root": [],
        #         "targetSum": 0
        #     },
        #     "expected": False
        # },
        # {
                
        #     "input": {
        #         "root": [1, 2],
        #         "targetSum": 0
        #     },
        #     "expected": False
        # },
        # {
                
        #     "input": {
        #         "root": [1,-2,-3,1,3,-2,None,-1],
        #         "targetSum": 3
        #     },
        #     "expected": False
        # },
        # {
                
        #     "input": {
        #         "root": [1],
        #         "targetSum": 1
        #     },
        #     "expected": True
        # }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"]["root"])
        targetSum = test["input"]["targetSum"]
        result = solution.hasPathSum(root, targetSum)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the test cases
run_tests()