from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ return list including reversed sublist """

        # Edge cases:
        if not head or left == right: 
            return head # no need for reversal
        
        # Create a dummy node to mark head
        dummy = ListNode(0)
        dummy.next = head  # return variable after sublist reversal
        beforeLeft = dummy # initiation point

        # Find node before left
        for _ in range(left - 1): # Calc steps to before left
            beforeLeft = beforeLeft.next
        
        # Reverse desired sublist
        prev = None # sublist reversal direction
        curr = beforeLeft.next

        for _ in range(right - left + 1): # how many steps taken to reverse list

            nextNode = curr.next # save next link (will be sad to lose it)
            curr.next = prev  # reverses link
            prev = curr # update previous
            curr = nextNode # update current Node
        
        # Relink before and after sublist reversals
        beforeLeft.next.next = curr # important to link this first
        beforeLeft.next = prev 

        return dummy.next # for actual head of List


            
def test_reverse_between():
    solution = Solution()
    
    # Test Case 1: Reverse a sublist in the middle
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 2, 4
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [1, 4, 3, 2, 5], "Test Case 1 Failed"

    # Test Case 2: Reverse a single-node sublist (no change)
    head = build_linked_list([5])
    left, right = 1, 1
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [5], "Test Case 2 Failed"

    # Test Case 3: Reverse the entire list
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 1, 5
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [5, 4, 3, 2, 1], "Test Case 3 Failed"

    # Test Case 4: Reverse a sublist at the end
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 3, 5
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [1, 2, 5, 4, 3], "Test Case 4 Failed"

    # Test Case 5: Reverse a single element in the middle
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 3, 3
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [1, 2, 3, 4, 5], "Test Case 5 Failed"

    # Edge Case 1: Reverse sublist starting at head (left = 1)
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 1, 3
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [3, 2, 1, 4, 5], "Edge Case 1 Failed"

    # Edge Case 2: Reverse sublist ending at tail (right = n)
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 3, 5
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [1, 2, 5, 4, 3], "Edge Case 2 Failed"

    # Edge Case 3: Reverse entire list (left = 1, right = n)
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 1, 5
    result_head = solution.reverseBetween(head, left, right)
    assert linked_list_to_list(result_head) == [5, 4, 3, 2, 1], "Edge Case 3 Failed"

    print("All test cases passed!")

# Run the tests
test_reverse_between()

