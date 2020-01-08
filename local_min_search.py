'''
Find (search for) a local min in O(lg n) time
------
Assumptions:
    len(arr) >= 3 
    arr[1] >= arr[2]
    arr[len(arr)-2] <= arr[len(arr)-1]
'''
def local_min_search(arr):
    lo = 0 
    hi = len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2 
        if arr[mid + 1] < arr[mid]:
            lo = mid + 1
        else:
            hi = mid

    return arr[hi]
        
print(local_min_search([9, 7, 7, 2, 1, 3, 7, 5, 4, 7, 3, 3, 4, 8, 6, 9]))
print(local_min_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]))
print(local_min_search([0, -5, -4, -3, -2, -1, 0]))
print(local_min_search([22, 19, 37, 32, 93, 6, 63, 23, 96]))
print(local_min_search([18, 1, 71, 84, 45, 90, 28, 98]))
print(local_min_search([78, 13, 63, 76, 73, 80, 21, 7, 9]))
print(local_min_search([88, 81, 7, 23, 49, 60, 19, 97, 42, 74]))
print(local_min_search([55, 3, 20, 62, 58, 94, 46, 63]))


