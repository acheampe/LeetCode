from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        return the preorder traversal of it's node value
        NOTE: Pre-order traversal is used in cases where we need to copy a tree
        Iterative Approach
        """

        if not root:
            return []
        
        # Space needed for operation:
        stack = []
        result = []
        currNode = root

        while stack or currNode:

            while currNode: # explore left branches
                stack.append(currNode)
                result.append(currNode.val)
                currNode = currNode.left
            
            # Explore it's right branch
            currNode = stack.pop()

            currNode = currNode.right
        
        return result

        # Time Complexity: O(n) as we navigated each node just once
        # Space Complexity: Worst Case O(n) if tree is heavily skewed, Average Case: O(log n) for recursive stack.

## EASIER APPROACH
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         Iterative preorder traversal: root --> left --> right
#         """
#         if not root:
#             return []
        
#         # Initialize stack and result list
#         stack = [root]
#         result = []

#         # Process nodes using a stack
#         while stack:
#             currNode = stack.pop()
#             result.append(currNode.val)

#             # Push right child first, so left child is processed first
#             if currNode.right:
#                 stack.append(currNode.right)
#             if currNode.left:
#                 stack.append(currNode.left)
        
#         return result

#         # Time Complexity: O(n) as we navigate each node just once
#         # Space Complexity: Worst Case O(n) if the tree is heavily skewed, Average Case: O(log n) for a balanced tree.




def test_preorder_traversal():
    # Constructing the tree:
    # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(9)

    # Expected Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]
    expected_output = [1, 2, 4, 5, 6, 7, 3, 8, 9]

    # Instantiate the Solution class
    solution = Solution()

    # Call the method and assert the result
    assert solution.preorderTraversal(root) == expected_output
    print("Test passed!")


# Run the test
test_preorder_traversal()
