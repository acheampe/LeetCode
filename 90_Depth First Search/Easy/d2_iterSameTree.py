from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        determine if p and q trees are the same
        NOTE: use a postOrder approach
        """

        # Edge Case 1:
        if not p and not q:
            return True # both empty
        
        if not p or not q:
            # at least one is empty so not the same:
            return False
        
        # Defining memory needed for operation
        qNodeStack = [q]
        pNodeStack = [p]

        while qNodeStack or pNodeStack:
            # focus on finding false

            currQ = qNodeStack.pop()
            currP = pNodeStack.pop()

            if currQ.val != currP.val:
                return False      

            if currQ.right and currP.right:
                qNodeStack.append(currQ.right)
                pNodeStack.append(currP.right)

            if currQ.right == None and currP.right != None or currQ.right != None and currP.right == None:
                return False   
            
            if currQ.left and currP.left:
                qNodeStack.append(currQ.left)
                pNodeStack.append(currP.left)

            if currQ.left == None and currP.left != None or currQ.left != None and currP.left == None:
                return False    

        return True


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

# Test cases
def run_tests():
    tests = [
        {
            "input": {
                "p": [1, 2, 3],
                "q": [1, 2, 3]
            },
            "expected": True
        },
        {
            "input": {
                "p": [1, 2],
                "q": [1, None, 2]
            },
            "expected": False
        },
        {
            "input": {
                "p": [1, 2, 1],
                "q": [1, 1, 2]
            },
            "expected": False
        },
        {
            "input": {
                "p": [],
                "q": []
            },
            "expected": True
        },
        {
            "input": {
                "p": [1],
                "q": [1]
            },
            "expected": True
        },
        {
            "input": {
                "p": [1],
                "q": [2]
            },
            "expected": False
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        p_tree = build_tree(test["input"]["p"])
        q_tree = build_tree(test["input"]["q"])
        result = solution.isSameTree(p_tree, q_tree)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")

# Run the tests
run_tests()