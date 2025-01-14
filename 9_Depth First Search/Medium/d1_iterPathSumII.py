from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Return all root-to-leaf paths where the sum of node values equals targetSum.
        """
        if not root:
            return []
        
        # Stack stores tuples of (current node, current path, remaining target sum)
        stack = [(root, [root.val], targetSum - root.val)]
        result = []

        while stack:
            currNode, path, remainingSum = stack.pop()

            # Check if it's a leaf node and the sum matches
            if not currNode.left and not currNode.right and remainingSum == 0:
                result.append(path)

            # Push children onto the stack (if they exist)
            if currNode.right:
                stack.append((currNode.right, path + [currNode.right.val], remainingSum - currNode.right.val))
            if currNode.left:
                stack.append((currNode.left, path + [currNode.left.val], remainingSum - currNode.left.val)) # creates own copy of path

        return result


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
        {
            "input": {
                "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
                "targetSum": 22
            },
            "expected": [[5, 4, 11, 2], [5, 8, 4, 5]]
        },
        {
            "input": {
                "root": [1, 2, 3],
                "targetSum": 5
            },
            "expected": []
        },
        {
            "input": {
                "root": [1, 2],
                "targetSum": 0
            },
            "expected": []
        },
        {
            "input": {
                "root": [],
                "targetSum": 0
            },
            "expected": []
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