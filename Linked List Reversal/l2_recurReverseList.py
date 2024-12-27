from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: # TC = O(n) and SC (n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        reverse linked list in place - recursive approach
        """
      
        # Establish Base Case/ termination:
        if not head or not head.next:
            return head
        
    
        reversedListHead = self.reverseList(head.next) # establishing head and breaking down into individual nodes to reverse directions
        # Connect nodes in reverse
        currNode = head.next  # Save the next node (current "lastNode" after recursion)
        currNode.next = head  # Point lastNode back to head (reversing the direction)
        head.next = None  # Disconnect the current node from the original forward list and to prevent a cycle
        return reversedListHead

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to build a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a linked list back to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_reverse_list():
    solution = Solution()
    
    # Test Case 1: Empty List
    # head = build_linked_list([])
    # reversed_head = solution.reverseList(head)
    # assert linked_list_to_list(reversed_head) == [], "Test Case 1 Failed"
    
    # # Test Case 2: Single Element List
    # head = build_linked_list([1])
    # reversed_head = solution.reverseList(head)
    # assert linked_list_to_list(reversed_head) == [1], "Test Case 2 Failed"
    
    # # Test Case 3: Two Element List
    # head = build_linked_list([1, 2])
    # reversed_head = solution.reverseList(head)
    # assert linked_list_to_list(reversed_head) == [2, 1], "Test Case 3 Failed"
    
    # # Test Case 4: Multiple Elements
    # head = build_linked_list([1, 2, 3, 4, 5])
    # reversed_head = solution.reverseList(head)
    # assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1], "Test Case 4 Failed"
    
    # Test Case 5: Negative and Positive Numbers
    head = build_linked_list([-1, 0, 1, 2, 3])
    reversed_head = solution.reverseList(head)
    assert linked_list_to_list(reversed_head) == [3, 2, 1, 0, -1], "Test Case 5 Failed"

    print("All test cases passed!")

# Run the test function
test_reverse_list()       