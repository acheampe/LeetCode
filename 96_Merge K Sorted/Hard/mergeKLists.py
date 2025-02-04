from typing import List, Optional
import unittest
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        return sorted linkedlist by merging the three input list

        Args: List containg LL

        Output: One sorted Linked List

        Time Complexity: O (n log k)
        Space Complexity: O (k) for min_heap operation space
        """

        # Edge case
        if not lists or all(l is None for l in lists):
            return None  # Correctly return None when all lists are empty
        
        # Establish memory needed for operation
        mergedResult = ListNode(0)
        tail = mergedResult
        min_heap = []

        # heappush first value of each array
        for i in range(len(lists)): # O(k) operations

            if lists[i]: # if not None (edge case within list)
                heapq.heappush(min_heap, (lists[i].val, i, lists[i])) # index necessary to maintain uniqueness
        
        # Add min val to output and update heap if it's next LL val
        while min_heap:
            
            _, index, currNode = heapq.heappop(min_heap) # O(log k)

            tail.next = currNode
            tail = tail.next

            if currNode.next:
                heapq.heappush(min_heap, (currNode.next.val, index, currNode.next)) 
        
        return mergedResult.next


class TestMergeKList(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def list_to_linkedlist(self, values):
        """Helper function to convert a list to a linked list."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linkedlist_to_list(self, head):
        """Helper function to convert a linked list to a list."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_example_1(self):
        """Test case from example 1."""
        lists = [
            self.list_to_linkedlist([1, 4, 5]),
            self.list_to_linkedlist([1, 3, 4]),
            self.list_to_linkedlist([2, 6])
        ]
        expected_output = [1, 1, 2, 3, 4, 4, 5, 6]
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

    def test_empty_list(self):
        """Test case when input is an empty list."""
        lists = []
        expected_output = []
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

    def test_list_of_empty_lists(self):
        """Test case when input contains only empty linked lists."""
        lists = [self.list_to_linkedlist([])]
        expected_output = []
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

    def test_single_list(self):
        """Test case when there's only one sorted linked list."""
        lists = [self.list_to_linkedlist([1, 2, 3, 4, 5])]
        expected_output = [1, 2, 3, 4, 5]
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

    def test_multiple_lists_with_duplicates(self):
        """Test case when there are duplicate values across multiple lists."""
        lists = [
            self.list_to_linkedlist([1, 1, 1]),
            self.list_to_linkedlist([1, 1, 1]),
            self.list_to_linkedlist([1, 1, 1])
        ]
        expected_output = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

    def test_lists_of_various_lengths(self):
        """Test case when input lists have different lengths."""
        lists = [
            self.list_to_linkedlist([2, 4, 6, 8]),
            self.list_to_linkedlist([1, 3]),
            self.list_to_linkedlist([5, 7, 9, 10, 11])
        ]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result = self.sol.mergeKLists(lists)
        self.assertEqual(self.linkedlist_to_list(result), expected_output)

if __name__ == "__main__":
    unittest.main()
    