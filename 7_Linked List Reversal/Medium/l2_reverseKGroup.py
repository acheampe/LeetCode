from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # SC O(n) and TC O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        reverse the linked list in designated groups
        """

        #S1: Edge case:
        if not head or k == 1:
            return head # no need to reverse these conditions
        
        # S2: Establish condition for initial reversal
        dummyNode = ListNode(0)
        dummyNode.next = head # return this variable 
        startNode = dummyNode

        while True:
            endNode = startNode
            # S3: Seek if endNode will be viable to reverse
            for _ in range(k):
                if not endNode.next:
                    return dummyNode.next # kth node no longer viable to reverse
                endNode = endNode.next
            
            # S4: connect group in cycle
            prevNode = None
            currNode = startNode.next
            newGroupStarts = endNode.next

            for _ in range(k):

                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
            
            # reconnect current group to next starting group
            currGroupEnd = startNode.next
            startNode.next = prevNode
            currGroupEnd.next = newGroupStarts
            
            # Update next startNode point to restart cycle if viable
            startNode = currGroupEnd

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

    # # Test case 2: k = 3, general case
    # head = create_linked_list([1, 2, 3, 4, 5])
    # k = 3
    # expected = [3, 2, 1, 4, 5]
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 2 failed"

    # # Test case 3: k = 1, no changes
    # head = create_linked_list([1, 2, 3, 4, 5])
    # k = 1
    # expected = [1, 2, 3, 4, 5]
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 3 failed"

    # # Test case 4: k = length of the list
    # head = create_linked_list([1, 2, 3, 4, 5])
    # k = 5
    # expected = [5, 4, 3, 2, 1]
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 4 failed"

    # # Test case 5: Single node list
    # head = create_linked_list([1])
    # k = 1
    # expected = [1]
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 5 failed"

    # # Test case 6: List length not a multiple of k
    # head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    # k = 3
    # expected = [3, 2, 1, 6, 5, 4, 7]
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 6 failed"

    # # Test case 7: Empty list
    # head = create_linked_list([])
    # k = 2
    # expected = []
    # assert linked_list_to_list(sol.reverseKGroup(head, k)) == expected, f"Test case 7 failed"

    print("All test cases passed!")

# Run the tests
test_reverseKGroup()