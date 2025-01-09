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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        return a post order traversal
        NOTE: post oder is ofter used as an approach to delete tree
        """

        if not root:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] ### Note using list concatenation can be less efficient than appending to a single shared list.

def test_postorder_traversal():
    # Test case 1: root = [1, null, 2, 3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    expected_output1 = [3, 2, 1]

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
    expected_output2 = [4, 6, 7, 5, 2, 9, 8, 3, 1]

    # Test case 3: root = []
    root3 = None
    expected_output3 = []

    # Test case 4: root = [1]
    root4 = TreeNode(1)
    expected_output4 = [1]

    # Instantiate the solution class
    solution = Solution()

    # Assertions
    assert solution.postorderTraversal(root1) == expected_output1, "Test case 1 failed"
    assert solution.postorderTraversal(root2) == expected_output2, "Test case 2 failed"
    assert solution.postorderTraversal(root3) == expected_output3, "Test case 3 failed"
    assert solution.postorderTraversal(root4) == expected_output4, "Test case 4 failed"

    print("All test cases passed!")


# Run the tests
test_postorder_traversal()
