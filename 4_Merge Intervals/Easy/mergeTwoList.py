from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
# Helper function to create a linked list
def createLinkedList(values):
    if not values:  # If the input list is empty, return None
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


# Helper function to convert a linked list to a Python list
def linkedListToList(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# TC = O (n) and SC = O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the merged linked list in non-decreasing order.
        """
        mergeList = ListNode()
        currNode = mergeList


        # iterate both LL while both are true:
        while list1 and list2:
            if list1.val >= list2.val:
                currNode.next = list2
                list2 = list2.next
            
            else:
                currNode.next = list1
                list1 = list1.next

            currNode = currNode.next
        
        # if any remains, attach to mergeList
        if list1:
            currNode.next = list1
        if list2:
            currNode.next = list2
        
        currNode = currNode.next

        return mergeList.next # To return head of merged list

         


        

# Test Case 1: Normal case with interleaved elements
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [1, 1, 2, 3, 4, 4]

# Test Case 2: Both lists are empty
list1 = createLinkedList([])
list2 = createLinkedList([])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: []

# Test Case 3: One list is empty
list1 = createLinkedList([])
list2 = createLinkedList([0])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [0]

# Test Case 4: Lists with non-overlapping ranges
list1 = createLinkedList([1, 2, 3])
list2 = createLinkedList([4, 5, 6])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [1, 2, 3, 4, 5, 6]

# Test Case 5: Lists of different lengths
list1 = createLinkedList([1, 3, 5])
list2 = createLinkedList([2, 4])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [1, 2, 3, 4, 5]

# Test Case 6: Lists with identical elements
list1 = createLinkedList([2, 2, 2])
list2 = createLinkedList([2, 2])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [2, 2, 2, 2, 2]

# Test Case 7: All elements from one list are smaller
list1 = createLinkedList([1, 2, 3])
list2 = createLinkedList([4, 5, 6, 7])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [1, 2, 3, 4, 5, 6, 7]

# Test Case 8: Lists containing negative values
list1 = createLinkedList([-3, -2, -1, 0])
list2 = createLinkedList([-4, -2, 1])
merged = solution.mergeTwoLists(list1, list2)
print(linkedListToList(merged))  # Expected: [-4, -3, -2, -2, -1, 0, 1]
