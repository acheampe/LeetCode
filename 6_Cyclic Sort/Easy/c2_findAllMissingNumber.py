from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        return all missing numbers not in array
        """

        missingNums = []

        for i in range(len(nums)):

            # Step one: Cyclic sort and condition to skip equal vals
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Return all missing numbers
        for i in range(len(nums)): #n iterate backwards
            
            # if missing, validate that val in num[i] exist
            if i + 1 != nums[i] and nums[nums[i] - 1]:
                missingNums.append(i + 1)
        
        return missingNums

# Test cases
def test_findDisappearedNumbers():
    sol = Solution()

    # Test case 1: General case with multiple missing numbers
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [5, 6]
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 1 failed. Got {sol.findDisappearedNumbers(nums)}"

    # Test case 2: Single element missing
    nums = [1, 1]
    expected = [2]
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 2 failed. Got {sol.findDisappearedNumbers(nums)}"

    # Test case 3: No missing numbers
    nums = [1, 2, 3, 4]
    expected = []
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 3 failed. Got {sol.findDisappearedNumbers(nums)}"

    # Test case 4: All numbers missing
    nums = [2, 2, 2, 2]
    expected = [1, 3, 4]
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 4 failed. Got {sol.findDisappearedNumbers(nums)}"

    # Test case 5: Large array with no missing numbers
    nums = list(range(1, 11))
    expected = []
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 5 failed. Got {sol.findDisappearedNumbers(nums)}"

    # Test case 6: Large array with missing numbers
    nums = [10, 6, 4, 2, 8, 8, 7, 2, 9, 1]
    expected = [3, 5]
    assert sol.findDisappearedNumbers(nums) == expected, f"Test case 6 failed. Got {sol.findDisappearedNumbers(nums)}"

    print("All test cases passed!")


# Run the tests
test_findDisappearedNumbers()