def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def new_partition(A, p, r): 
    
    pivot = A[r - 1]
    i = t = p - 1
    for j in range(p, r - 1):
        if(A[j] == pivot):
            t += 1
            swap(A,t,j)
        if(A[j] < pivot):
            t += 1
            swap(A,t,j)
            i += 1
            swap(A,i,t)            
    t += 1
    swap(A,t,r-1)        
    return i+1, t


arr = [10,9,8,7,6,5,5,5,4,3,2,1,5]
new_partition(arr, 0, len(arr))
