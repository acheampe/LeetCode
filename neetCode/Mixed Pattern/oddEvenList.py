import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(arr):
    if not arr:
        return None
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """return reordered list: odd indices are 
        respectively to the left and even indices to the right
        """
        
        def clarificationQuestions():
            """
            - are there cases where LL is empty?
            - will ordering nodes by switching it's values acceptable? or
            do we really want to switch the order of linked addresses?
            - Is it safe to assume that all node vals will be integers?
            - How big is our LL data?
            """
        
        def Approach():
            """The non-optimized approach to take is creating two dummy nodes and 
            linking odd and even indice nodes to it's respective dummy as we
            traverse the LL, then combine them at the end, however this will be O(n) TC and SC, especially 
            if we are duplicating values in new memory
            
            I think it is possible to do it in O(1) SC with a similar approach if we just redirect the edges since we 
            wont be using addition memory except dummy nodes but that will pass for O(1)
            """
            
        
        if not head: # Empty LL edge case
            return None
        startNode = head # we will return startNode
        evenHead = startNode.next  # connect this to tail of odd LL
        
        currOdd, currEven = startNode, startNode.next
            
        while currEven and currEven.next:
            
            currOdd.next = currEven.next
            currOdd = currOdd.next
            
            currEven.next = currOdd.next
            currEven = currEven.next
   
        # Combine
        currOdd.next = evenHead
        
        return startNode
        
        
        

class TestOddEvenList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5])
        result = self.sol.oddEvenList(head)
        self.assertEqual(linkedlist_to_list(result), [1, 3, 5, 2, 4])

    def test_example_2(self):
        head = list_to_linkedlist([2, 1, 3, 5, 6, 4, 7])
        result = self.sol.oddEvenList(head)
        self.assertEqual(linkedlist_to_list(result), [2, 3, 6, 7, 1, 5, 4])

    def test_empty_list(self):
        head = list_to_linkedlist([])
        result = self.sol.oddEvenList(head)
        self.assertEqual(linkedlist_to_list(result), [])

    def test_single_node(self):
        head = list_to_linkedlist([10])
        result = self.sol.oddEvenList(head)
        self.assertEqual(linkedlist_to_list(result), [10])

    def test_two_nodes(self):
        head = list_to_linkedlist([1, 2])
        result = self.sol.oddEvenList(head)
        self.assertEqual(linkedlist_to_list(result), [1, 2])

if __name__ == '__main__':
    unittest.main()
