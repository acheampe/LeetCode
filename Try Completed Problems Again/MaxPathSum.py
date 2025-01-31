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

        TC = O(n)
        SC = O(1)
        """


        def dfs(currNode):
            """
            dfs search for maxPath
            """
            # Establish base/return case:
            if not currNode:
                return 0
            
            # left side recursion
            leftSum = max(dfs(currNode.left), 0) # no need to consider negative val nodes

            # right side recursion
            rightSum = max(dfs(currNode.right), 0) # no need to consider negative val nodes

            # return current maxPath
            self.maxPath = max(self.maxPath, leftSum + rightSum + currNode.val)

            return currNode.val +  max(leftSum, rightSum)

        self.maxPath = float('-inf')
        dfs(root)
        return self.maxPath

### Notes on this:
# 1. Iterate down left and right branches to leave node after developing space to return maxPath (dfs)
# 2. return sum of left side (if sum is negative, ignore and return 0)
###### why ignore? - paths with negative leave nodes will deviate further from max, if both leaves are negative, even if the root is negative, we wanna only return the val of the root
# 3. calculate sum of node.val + leftSum + rightSum to compare to and update current maxPath if needed
# return sum of currVal with the greater value of it's left or right node.val



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
