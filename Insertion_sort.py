'''
Pseudocode (note 1-based index)
-------------------------------
Insertiong-Sort(Arr,n) 
for j = 2 to n
  key = A[j]
  i = j - 1
  while i > 0 and A[i] > key
    A[i+1] = A[i]
    i = i - 1
   A[i+1] = key
'''

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key: int = arr[j]
        i: int = j - 1
        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr

# examples 
print(insertion_sort([4, 5, 10, 23, 1, 3])) # output: 1, 3, 4, 5, 10, 23
