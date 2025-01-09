from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ## TIME COMPLEXITY: O(n) because each node is traversed once
    ## SPACE COMPLEXITY: Worst Case O(n) if tree heavily leans on one side, if it is balanced well the best case will be O(log n) due to stack of recursion
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        return the preOrder traversal of this tree
        NOTE: preOrder is usually used to copy a tree
        """
        # Recursive approach: preOrder: parent --> left, --> right

        if not root:
            return root

        preOrderResult = []
        # Step 1: Establish a helper function 
        self.helpTrackPreOrder(root, preOrderResult) # for storing result

        return preOrderResult

    def helpTrackPreOrder(self, root, result):
        """
        return result of preOrder tree
        """

        if not root:
            return
        
        result.append(root.val)

        self.helpTrackPreOrder(root.left, result) 
        self.helpTrackPreOrder(root.right, result)
        
        return result

## EASIER APPROACH
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         Recursive preOrder traversal: parent --> left --> right
#         """
#         if not root:
#             return []

#         # Preorder: Process current node, then left, then right
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)




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
