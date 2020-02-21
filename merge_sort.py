'''
MergeSort: Divide and Conquer Algorithm
-----------------------------
MergeSort(A, p, r)
  if p < r
    q = floor((p + r) / 2) 
    MergeSort(a, p, q)        # T(n/2)
    MergeSort(a, p, q)        # T(n/2)
    Merge(A, p, q, r)         # O(n)
    
    
Merge(A, p, q, r)
  n_1 = q - p + 1
  n_2 = r - q
  Create Arrays left (L) and right (R)
  #populate the arrays
  for i to n_1
    L[i] = A[p+i-1]
  for j to n_2
    R[j] = A[q+j]
  L[n_1 + 1] = math.infinity (sentenel value) 
  R[n_2 + 1] = math.infinity (sentenenl value) 
  
  i = 1 
  j = 1 
  for k=p to r
    if L[i] <= R[j]
      A[k] = L[i]
      i = i + 1
    else
      A[k] = R[j]
      j = j + 1

Recurrence: O(n) + 2*T(n/2), using master's theorem 

Run time: O(n log n)
Space time: O(n)
'''

import math

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 

    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 

    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 

    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 

    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 

        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = math.floor((l+(r-1))/2)

        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

def merge_sort(arr):
    mergeSort(arr, 0, len(arr)-1)

# examples 
print(merge_sort([4, 5, 10, 23, 1, 3])) # output: 1, 3, 4, 5, 10, 23
