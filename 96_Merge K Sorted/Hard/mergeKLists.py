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

        # Edge Case:
        if not lists or all(l is None for l in lists): # checks if all trees in list is empty
            return None # for returning an empty tree
        
        # Establish min_heap of eventual size
        min_heap = []
        
        # Add first node of each tree in list
        for index, node in enumerate(lists):

            if node: # incases where tree is empty
                # Push node.val, index, and node onto min_heap
                heapq.heappush(min_heap, (node.val, index, node))
        
        # Establish return tree
        dummyNode = ListNode(0) # return dummyNode.next
        tailNode = dummyNode # current iteration of tree

        while min_heap:

            # To return top of tree O(log k) operation
            _, treeIndex, node = heapq.heappop(min_heap)

            # Add to new ordered tree
            tailNode.next = node # add the node itself, not the value
            tailNode = tailNode.next

            if node.next:
                # Push new val and node to min_heap from the tree of recent heappop()
                heapq.heappush(min_heap, (node.next.val, treeIndex, node.next))
        
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
    