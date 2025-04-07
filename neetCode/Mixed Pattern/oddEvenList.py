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
        # TODO: Implement this method
        pass

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
