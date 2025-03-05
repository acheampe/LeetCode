from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: ### RECURSIVE APPROACH ####

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Return the number of paths where the sum of the values equals targetSum.
        """
        self.count = 0
        trackSum = defaultdict(int) # Keeps track of cumulative sum.
        trackSum[0] = 1 # Accounts for case where a single full path == target (0 = fullpath - targetSum)

        def deepSearch(node, currSum):
            """
            track current Sum and to accumulate self.count when appropriate
            """

            if not node:
                return
            
            currSum += node.val # Update to currSum

            # Add to count if there exist a node/path that will meet our target
            self.count += trackSum[currSum - targetSum]

            trackSum[currSum] += 1 # update this currSum 

            # Explore the left and right children
            deepSearch(node.left, currSum)
            deepSearch(node.right, currSum)

            trackSum[currSum] -= 1 # backtrack because we no longer want to factor it in our path 


        deepSearch(root, 0) # Initiate search

        return self.count
    
    def solutionApproach(self):
        """
        The goal of this problem is to find the number of paths in a binary tree 
        where the sum of node values equals the given targetSum. The paths **do not**
        need to start at the root or end at the leaf—they can start and end at any node.

        🚀 **Optimal Approach: Prefix Sum + DFS**
        
        Instead of recalculating sums from each node (which is inefficient in O(n²)), 
        we use **prefix sum with a hashmap** to track cumulative sums efficiently.

        ✅ **Steps to Solve the Problem Efficiently:**
        
        1️⃣ **Use a HashMap (`trackFrequency`) to Track Prefix Sums**
        - This keeps track of how many times a specific **cumulative sum** has been encountered.
        - Initialize `trackFrequency[0] = 1` to account for paths that directly sum to `targetSum`.

        2️⃣ **Perform Depth-First Search (DFS)**
        - Start DFS traversal from the root.
        - Maintain `currSum`, which stores the **cumulative sum** from root to the current node.

        3️⃣ **Check for Valid Paths using Prefix Sum**
        - The number of paths ending at the current node that sum to `targetSum` is found by:
            `trackFrequency[currSum - targetSum]`
        - If a previous sum `currSum - targetSum` exists, it means there is a path from an earlier 
            node to the current node with the desired sum.

        4️⃣ **Update `trackFrequency` and Recurse**
        - Increment `trackFrequency[currSum]` since we encountered this sum.
        - Perform DFS on left and right children.

        5️⃣ **Backtrack (Important!)**
        - Before returning, decrement `trackFrequency[currSum]` to remove the current path from the prefix sum count.

        ✅ **Key Learnings**
        - **Using prefix sum avoids recalculating sums from each node, reducing complexity to O(n).**
        - **Backtracking ensures we only consider sums in the current path.**
        - **The approach is efficient for large trees, performing each operation in O(1) on average.**

        ⏳ **Time Complexity:** O(n) - We visit each node once.  
        🏗 **Space Complexity:** O(n) - Due to recursion and prefix sum hashmap storage.
        """


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
                "root": [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1],
                "targetSum": 8
            },
            "expected": 3
        },
        {
            "input": {
                "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
                "targetSum": 22
            },
            "expected": 3
        },
        {
            "input": {
                "root": [],
                "targetSum": 0
            },
            "expected": 0
        },
        {
            "input": {
                "root": [1, -2, -3, 1, 3, -2, None, -1],
                "targetSum": -1
            },
            "expected": 4
        },
        {
            "input": {
                "root": [1],
                "targetSum": 1
            },
            "expected": 1
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