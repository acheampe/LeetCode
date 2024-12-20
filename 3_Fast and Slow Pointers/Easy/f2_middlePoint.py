from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Helper function to create a linked list
def createLinkedList(values):
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ return the middle node """

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Problems
head = createLinkedList([1, 2, 3, 4, 5])
sol = Solution()
middle = sol.middleNode(head)
print(middle)  # Output: 3