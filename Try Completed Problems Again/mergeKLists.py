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
        returns linkedlist of input list of sorted LL

        TC: O(n log k) for heappush operation
        SC: O(k) k space representing number of linkedList
        """

        # edge case:
        if not lists or all(l is None for l in lists):
            return None # to return an empty tree
        
        minHeap = []

        for index, headNode in enumerate(lists):
            
            if headNode:
                # add the first three nodes of each linkedlist
                heapq.heappush(minHeap, (headNode.val, index, headNode))  # O (log k)
        # create a dummyNode
        dummyNode = ListNode(0)  # return dummyNode.next
        currTail = dummyNode 

        while minHeap:

            _, index, node = heapq.heappop(minHeap) # O (log k)

            currTail.next = node
            currTail = currTail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, index, node.next))  # O (n log k)          

        return dummyNode.next 

    def approachSummary(self):
        """
        Summary of approach strategy.

        Solution: 
        Time Complexity = O(n log k)
        Space Complexity = O(k)

        Approaching this solution is a better of separating concerns to derive
        to the solution.

        Step 1: The first concern is to address the edge case of no list present 
        or no trees within the list. 

        Step 2: Is to set up a min_heap of the first nodes in each tree within 
        the list. The values in the min_heap should contain the value, the index 
        of the array (important to maintain uniqueness to negate exception error)
        and the node itself)

        Step 3: Set up a dummy Node that returns dummyNode.next

        Step 4: Is to pop min_heap and add it's value to dummy tree

        Step 5: push the next node of the same tree of the node that was added to 
        dummy to min_heap to maintain K nodes  and repeat cycle.

        Step 6: return dummy.next 

        TIme Complexity: O(n log k)
        Space Complexity (if not accounting for returned tree): O(k)
        """

        pass 


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

    # def test_empty_list(self):
    #     """Test case when input is an empty list."""
    #     lists = []
    #     expected_output = []
    #     result = self.sol.mergeKLists(lists)
    #     self.assertEqual(self.linkedlist_to_list(result), expected_output)

    # def test_list_of_empty_lists(self):
    #     """Test case when input contains only empty linked lists."""
    #     lists = [self.list_to_linkedlist([])]
    #     expected_output = []
    #     result = self.sol.mergeKLists(lists)
    #     self.assertEqual(self.linkedlist_to_list(result), expected_output)

    # def test_single_list(self):
    #     """Test case when there's only one sorted linked list."""
    #     lists = [self.list_to_linkedlist([1, 2, 3, 4, 5])]
    #     expected_output = [1, 2, 3, 4, 5]
    #     result = self.sol.mergeKLists(lists)
    #     self.assertEqual(self.linkedlist_to_list(result), expected_output)

    # def test_multiple_lists_with_duplicates(self):
    #     """Test case when there are duplicate values across multiple lists."""
    #     lists = [
    #         self.list_to_linkedlist([1, 1, 1]),
    #         self.list_to_linkedlist([1, 1, 1]),
    #         self.list_to_linkedlist([1, 1, 1])
    #     ]
    #     expected_output = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    #     result = self.sol.mergeKLists(lists)
    #     self.assertEqual(self.linkedlist_to_list(result), expected_output)

    # def test_lists_of_various_lengths(self):
    #     """Test case when input lists have different lengths."""
    #     lists = [
    #         self.list_to_linkedlist([2, 4, 6, 8]),
    #         self.list_to_linkedlist([1, 3]),
    #         self.list_to_linkedlist([5, 7, 9, 10, 11])
    #     ]
    #     expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #     result = self.sol.mergeKLists(lists)
    #     self.assertEqual(self.linkedlist_to_list(result), expected_output)

if __name__ == "__main__":
    unittest.main()
    