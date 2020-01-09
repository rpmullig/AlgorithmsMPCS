'''
Returns the index of the target value of a sorted array input
    A Divide and Conquer search algorithm that runs in O(log_2 n)

returns -1 if target is not in array 

'''

def binary_search(arr, target):
    l: int = 0 
    r: int = len(arr) - 1
    while r >= l:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1
    
    
# examples
print(binary_search([1, 3, 5, 6, 7, 100], 3)) # returns 1
print(binary_search([1, 3, 5, 6, 7, 100], 4)) # returns -1 
print(binary_search([1, 3, 5, 6, 7, 100], 100)) # returns 5
print(binary_search([1, 3, 5, 6, 7, 100], 1)) # returns 0
