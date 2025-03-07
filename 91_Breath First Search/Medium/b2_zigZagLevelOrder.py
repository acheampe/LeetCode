from typing import Optional, List
from collections import deque

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

class Solution: # TC = O(n) SC = O(w) for width of tree and O(n) for result
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        return the zigzag level order traversal of its nodes' values. 
        (i.e., from left to right, then right to left for the next level and alternate between)
        """

        # S1: if no root:
        if not root:
            return []

        # S2: establish memory/variables needed for operation
        result = []
        qstack = deque()
        qstack.append((root, 0)) # node and it's corresponding level

        while qstack:

            currNode, currLevel = qstack.popleft()

            if len(result) == currLevel:
                result.append([])
            
            if (currLevel % 2 )!= 0:
                result[currLevel].insert(0, currNode.val)
            else:
                result[currLevel].append(currNode.val)


            if currNode.left:
                qstack.append((currNode.left, currLevel + 1))
            if currNode.right:
                qstack.append((currNode.right, currLevel + 1))

        return result

    def solutionApproach(self):
        """
        🚀 **Approach Summary: Zigzag Level Order Traversal (BFS with Deque)**

        **🔹 Key Insight:**  
        - This problem is a **variation of level-order traversal (BFS)**  
        - The **zigzag order** means:
          - **Even levels** (0, 2, 4, ...): Append values **normally (left to right)**  
          - **Odd levels** (1, 3, 5, ...): Append values **in reverse (right to left)**  

        **💡 Steps to Solve:**
        1️⃣ **Edge Case:** If the tree is empty, return `[]`.  
        2️⃣ **Use a Deque (`dequeStack`) to perform BFS traversal**, storing `(node, level)` pairs.  
        3️⃣ **Process nodes level by level:**  
            - If a new level is encountered, **append a new empty list** to `outputOrder`.  
            - If the level is **even**, append node values **normally**.  
            - If the level is **odd**, **insert values at index 0** (to reverse the order).  
        4️⃣ **Add child nodes to `dequeStack`** (left first, then right).  
        5️⃣ **Continue until all levels are processed, then return `outputOrder`**.

        **🔹 Time Complexity:**  
        - **O(n)** → Each node is visited **once**.  
        - The `insert(0, val)` operation for odd levels is **O(k)** where `k` is the level size.  
        - In the worst case (complete tree), `k ≈ n`, making the worst case **O(n^2)** if using a list.  
        - However, **using `deque` keeps it O(n)` in practice**.

        **🔹 Space Complexity:**  
        - **O(n)** → The worst case (skewed tree) stores all nodes in memory at once.
        - The `outputOrder` list also requires **O(n)** space.

        ✅ **Why This Works?**  
        - **Using a deque ensures efficient level-order traversal.**  
        - **Appending new lists at each level prevents index errors.**  
        - **Reversing order only when necessary avoids unnecessary computations.**
        """
        
        pass
        
# Test cases for the zigzagLevelOrder method
def run_tests():
    tests = [
        {
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [20, 9], [15, 7]]
        },
        {
            "input": [1],
            "expected": [[1]]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [[1], [3, 2], [4, 5, 6, 7]]
        },
        {
            "input": [1, None, 2, None, 3, None, 4],
            "expected": [[1], [2], [3], [4]]
        },
        {
            "input": [1, 2, 3, 4, None, None, 5],
            "expected": [[1], [3, 2], [4, 5]]
        }
    ]

    solution = Solution()
    for i, test in enumerate(tests):
        root = build_tree(test["input"])
        result = solution.zigzagLevelOrder(root)
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")
        if result != test["expected"]:
            print(f"  Expected: {test['expected']}, Got: {result}")

# Run the tests
run_tests()