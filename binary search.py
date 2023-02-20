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

