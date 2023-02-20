arr = [1,3,6,9,11,34,55,77,88]
x = 34
j = 0
if len(arr) /2 == 0:
    mid = int(len(arr) / 2)
else:
    mid = int((len(arr) +1)/2)
while True:
    if arr[j] == x:
        print('at position ',j)
        break
    if arr[j] < arr[mid]:
        j = mid
arr2 = [1,5,2,7,3,9,0,6]

# Python Program implementation
# of binary insertion sort

def binary_search(arr, val, start, end):
	if start == end:
		if arr[start] > val:
			return start
		else:
			return start+1

	if start > end:
		return start

	mid = (start+end)/2
	if arr[mid] < val:
		return binary_search(arr, val, mid+1, end)
	elif arr[mid] > val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def insertion_sort(arr):
	for i in xrange(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

print("Sorted array:")
print insertion_sort([37, 23, 0, 17, 12, 72, 31,
						46, 100, 88, 54])


c