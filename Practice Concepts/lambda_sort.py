intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
intervals.sort(key=lambda x: x[0]) # retrieves the first values of each interval and then sorts interval
print(intervals)

pairs = [(1, 5), (2, 3), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 1), (2, 3), (1, 5)]

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
