from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def createLinkedList(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]  # Create cycle
    
    return nodes[0]

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        return true if array/linkedlist is cyclic
        """
        if not head or not head.next:
            return False
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next # Traverse link 2x as fast
            slow = slow.next  # Traverse link one at a time 

            if fast == slow:  # Detected cycle
                return True
        
        return False 
        


 # Create linked list with cycle
head = createLinkedList([3, 2, 0, -4], 1)

# Test the solution
sol = Solution()
print(sol.hasCycle(head))  # Output: True

# Create linked list without cycle
head = createLinkedList([1, 2], -1)
print(sol.hasCycle(head))  # Output: False
