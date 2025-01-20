from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse linked list k nodes at a time and return the modified list.
        """
        # Edge Case
        if k == 1 or not head:
            return head  # No need to reverse if k = 1 or list is empty

        # Initialize a dummy node to simplify edge handling
        dummy = ListNode(0)
        dummy.next = head
        startNode = dummy  # The node before the current group

        while True:
            # Check if there are at least k nodes remaining to reverse
            endNode = startNode
            for _ in range(k):
                endNode = endNode.next
                if not endNode:
                    return dummy.next  # If fewer than k nodes remain, return the result

            # Reverse k nodes
            prevNode = None
            currNode = startNode.next
            nextGroupStart = endNode.next  # Store the start of the next group
            endNode.next = None  # Temporarily break the chain

            # Reverse the current group
            while currNode:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode

            # Reconnect the reversed group to the previous and next groups
            newGroupStart = startNode.next
            startNode.next = prevNode
            newGroupStart.next = nextGroupStart

            # Move startNode to the end of the reversed group
            startNode = newGroupStart 

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
def test_reverseKGroup():
    sol = Solution()

    # Test case 1: k = 2, general case
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 2
    expected = [2, 1, 4, 3, 5]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 1 failed"

    # Test case 2: k = 3, general case
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 3
    expected = [3, 2, 1, 4, 5]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 2 failed"

    # Test case 3: k = 1, no changes
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 1
    expected = [1, 2, 3, 4, 5]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 3 failed"

    # Test case 4: k = length of the list
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 5
    expected = [5, 4, 3, 2, 1]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 4 failed"

    # Test case 5: Single node list
    head = create_linked_list([1])
    k = 1
    expected = [1]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 5 failed"

    # Test case 6: List length not a multiple of k
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    k = 3
    expected = [3, 2, 1, 6, 5, 4, 7]
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 6 failed"

    # Test case 7: Empty list
    head = create_linked_list([])
    k = 2
    expected = []
    assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 7 failed"

    print("All test cases passed!")

# Run the tests
test_reverseKGroup()