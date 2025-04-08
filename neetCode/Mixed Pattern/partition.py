import unittest

# Helper class to create and extract linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(items):
    dummy = ListNode(0)
    current = dummy
    for val in items:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """partition LL so all nodes with vals 
        less than x is to the left of returns LL -- > maintain order"""
        
        def discussApproach():
            """An initial approach will be to create a dummy Node to link all 
            nodes less than x to it, and if original LL can be manipulated, 
            direct all nodes >= x to link to each other in the given input link,
            
            if we can't manipulate the input LL, then we create a dummyNode to link all 
            node with vals >= x then combine both LL together...approach will be 
            subject to the interviewers preference
            
            Either way we will end up with O(n) TC and SC....let me think for a second to 
            see if there is a way we can approach this with O(1) SC...
            
            I dont see a viable way for O(1) SC
            """
        
        if not head:
            return None
        
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)
        left = leftDummy
        right = rightDummy

        while head:
            nextNode = head.next
            head.next = None  # break existing link to avoid corruption
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = nextNode
        
        left.next = rightDummy.next

        return leftDummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         """partition LL based on x input value"""

#         if not head:
#             return None

#         dummyLeftPartition, dummyRightPartition = ListNode(0), ListNode(1)
#         lessThanX, XorMore = dummyLeftPartition, dummyRightPartition

#         currNode = head

#         while currNode:
#             nextNode = currNode.next
#             currNode.next = None # break link to reduce chances of creating a cycle

#             if currNode.val < x:
#                 lessThanX.next = currNode
#                 lessThanX = currNode
            
#             else:
#                 XorMore.next = currNode
#                 XorMore = currNode
            
#             currNode = nextNode
        
#         lessThanX.next = dummyRightPartition.next

        return dummyLeftPartition.next

class TestPartitionList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        head = list_to_linked_list([1, 4, 3, 2, 5, 2])
        x = 3
        expected = [1, 2, 2, 4, 3, 5]
        result = self.sol.partition(head, x)
        self.assertEqual(linked_list_to_list(result), expected)

    # def test_example_2(self):
    #     head = list_to_linked_list([2, 1])
    #     x = 2
    #     expected = [1, 2]
    #     result = self.sol.partition(head, x)
    #     self.assertEqual(linked_list_to_list(result), expected)

    # def test_all_less_than_x(self):
    #     head = list_to_linked_list([1, 1, 1])
    #     x = 5
    #     expected = [1, 1, 1]
    #     result = self.sol.partition(head, x)
    #     self.assertEqual(linked_list_to_list(result), expected)

    # def test_all_greater_equal_x(self):
    #     head = list_to_linked_list([5, 6, 7])
    #     x = 5
    #     expected = [5, 6, 7]
    #     result = self.sol.partition(head, x)
    #     self.assertEqual(linked_list_to_list(result), expected)

    # def test_empty_list(self):
    #     head = list_to_linked_list([])
    #     x = 0
    #     expected = []
    #     result = self.sol.partition(head, x)
    #     self.assertEqual(linked_list_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()