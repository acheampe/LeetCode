class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        return triplets that sums up to 0
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        TARGETSUM = 0
        nums.sort() # O(n log n)
        resultTriplets = []
        duplicateTriplet = {}

        for fixedIndex in range(len(nums) - 1):  # O(n)
            leftIndex = fixedIndex + 1
            rightIndex = len(nums) - 1
            
            if fixedIndex != 0 and nums[fixedIndex] == nums[fixedIndex - 1]:
                continue  # skip duplicates

            while leftIndex < rightIndex:

                currentTotal = nums[fixedIndex] + nums[leftIndex] + nums[rightIndex]
                
                if currentTotal == TARGETSUM and tuple([nums[fixedIndex], nums[leftIndex], nums[rightIndex]]) not in duplicateTriplet:
                    resultTriplets.append([nums[fixedIndex], nums[leftIndex], nums[rightIndex]])
                    duplicateTriplet[tuple([nums[fixedIndex], nums[leftIndex], nums[rightIndex]])] = True
                    leftIndex += 1
                
                elif currentTotal > 0:
                    rightIndex -= 1
                
                else:
                    leftIndex += 1
        
        return resultTriplets
    
    def approachSolution(self):
        """
        Because we have sorted the array. We can skip duplicate logic after we append
        triplets with a while logic. This saves us from using memory space. See 
        earlier implementation from a few months ago. 

        if totalVal == 0:
            result.append([nums[startIndex], nums[endIndex], fixedVal])
        
            while startIndex < endIndex and nums[endIndex] == nums[endIndex - 1]:
                endIndex -= 1 # To avoid duplicate calc

            while startIndex < endIndex and nums[startIndex] == nums[startIndex + 1]:
                startIndex += 1 # To avoid duplicates calc
        **rest of logic here***
        """
        


sol = Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
# print(sol.threeSum([0,1,1])) # Expected: []
# print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
# print(sol.threeSum([3,-2,1,0])) # Expected: []
# print(sol.threeSum([1,-1,0])) # Expected: [[-1,0,1]]
# print(sol.threeSum([1,2,-2,-1])) # Expected: []
# print(sol.threeSum([1,-1,-1,0])) # Expected: [[-1,0,1]]
# print(sol.threeSum([-2,0,1,1,2])) # Expected: [[-2,0,2],[-2,1,1]]
print(sol.threeSum([0,0,0,0])) # Expected: [[0,0,0]]

