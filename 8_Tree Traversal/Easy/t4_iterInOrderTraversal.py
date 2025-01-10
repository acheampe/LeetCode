from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    ## TIME COMPLEXITY: O(n) because each node is traversed once
    ## SPACE COMPLEXITY: Worst Case O(n) if tree heavily leans on one side, 
    ## best case log n if tree is balanced because the max stack depth corresponse to height of the tree.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        return the inorder traversal of it's node value
        NOTE: inorder is usually used to varify binary tree
        iterative approach
        """

        # Edge case:
        if not root:
            return [] # if tree is empty

        # Space needed for operation
        stack = []
        result = []
        currNode = root

        while currNode or stack:

            # let's move as far left as possible:
            while currNode:
                stack.append(currNode) # store nodes not appended to result
                currNode = currNode.left
            
            # Store current Node:
            currNode = stack.pop()
            result.append(currNode.val)

            # Check currNode right side
            currNode = currNode.right
        
        return result

def test_inorder_traversal():
    # Test case 1: root = [1, null, 2, 3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    expected_output1 = [1, 3, 2]

    # Test case 2: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(8)
    root2.left.right.left = TreeNode(6)
    root2.left.right.right = TreeNode(7)
    root2.right.right.left = TreeNode(9)
    expected_output2 = [4, 2, 6, 5, 7, 1, 3, 9, 8]

    # Test case 3: root = []
    root3 = None
    expected_output3 = []

    # Test case 4: root = [1]
    root4 = TreeNode(1)
    expected_output4 = [1]

    # Instantiate the solution class
    solution = Solution()

    # Assertions
    assert solution.inorderTraversal(root1) == expected_output1, f"Test case 1 failed"
    assert solution.inorderTraversal(root2) == expected_output2, f"Test case 2 failed"
    assert solution.inorderTraversal(root3) == expected_output3, f"Test case 3 failed"
    assert solution.inorderTraversal(root4) == expected_output4, f"Test case 4 failed"

    print("All test cases passed!")


# Run the tests
test_inorder_traversal()
 
# class Solution:  # Concise variant
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         Perform inOrder traversal: left --> root --> right
#         """
#         if not root:
#             return []

#         # Inorder traversal: Combine left subtree, root, and right subtree results
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

