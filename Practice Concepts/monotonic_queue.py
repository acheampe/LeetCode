from collections import deque

def increasing_monotonic_queue(arr, n):
	q = deque()
	for i in range(n):
		while len(q) > 0 and q[-1] > arr[i]:
			q.pop()
		q.append(arr[i])
	return q

arr = [1, 2, 8, 3, 4, 10, 5, 6]
n = len(arr)
print(increasing_monotonic_queue(arr, n))

