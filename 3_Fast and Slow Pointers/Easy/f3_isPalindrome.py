from typing import Optional
from collections import deque

# TC = O (n) and SC = O(1)
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        determine if singly Linked list is a palindrome
        """

        # Naive Approach - TC O(n) and SC O(n)
        stack = deque()

        curr = head

        while curr:
            stack.appendleft(curr.value)
            curr = curr.next

        curr = head

        while curr:
            if curr.value != stack.popleft():
                return False
            
            curr = curr.next
    
        return True







# Problems
# head = createLinkedList([1,2,2,1]) 
# sol = Solution()
# isPal = sol.isPalindrome(head)
# print(isPal)  # Output: true

head = createLinkedList([1,2]) 
sol = Solution()
isPal = sol.isPalindrome(head)
print(isPal)  # Output: false