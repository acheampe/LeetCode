from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

class Solution: # TC = O (n) and SC = O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None
        
        slow = head  # Reset slow to head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# Example 1: Cycle at node with value 2
head = createLinkedList([3, 2, 0, -4], 1)
sol = Solution()
cycle_start = sol.detectCycle(head)
print(cycle_start.val if cycle_start else None)  # Output: 2

# Example 2: Cycle at node with value 1
head = createLinkedList([1, 2], 0)
cycle_start = sol.detectCycle(head)
print(cycle_start.val if cycle_start else None)  # Output: 1

# Example 3: No cycle
head = createLinkedList([1], -1)
cycle_start = sol.detectCycle(head)
print(cycle_start)  # Output: None
