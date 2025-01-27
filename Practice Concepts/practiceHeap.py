import heapq

nums = [4, 10, 5, 7, 20]
print(nums)

heapq.heapify(nums) # O(n) operative cost

print(nums)

heapq.heappush(nums, 15) # O(log n) operative cost

print(nums)

print(heapq.heappop(nums)) # O(log n) operative cost

print(nums)

print(heapq.nlargest(3, nums)) # O(n log k)

print(heapq.nlargest(1, nums)) # O(n log k)

print(heapq.nsmallest(3, nums)) # O(n log k), k being the size requested
# essentially a heap of size k is created, and the root of that k-sized heap is compared
# to n-k heap to decided if we have our desired output
# if we need to update k heap, we add it and heapify the list each time. 