''' 
Searches a 2D matrix and returns a local minimum (in the north, south, east,
west directions). 
Assumption:
    There always exists a local minimum in a matrix
'''

def is_2D_local_min(arr, x, y):
    if x > 0 and y > 0:
        return arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x][y+1] and arr[x][y] <= arr[x][y-1]
    

def local_min_search_2D(arr):
    
    m: int = len(arr) - 1
    n: int = len(arr[0]) - 1
   
    while is_2D_local_min(arr, m, n) is False:
        p = m // 4
        q = n // 4 

        # check the diagonals 
        NW = tmp = arr[p][q]
        NE = arr[p * 3][q]
        SE = arr[p][q * 3]
        SW = arr[p * 3][q * 3]
        
        directions_v = [NW, NE, SE, SW] 
        directions_c = [[p, q],[p*3,q],[p,q*3],[p*3,q*3]] 
        
        i = 0
        for j in range(1, 4):
            if directions[i] < tmp:
                i = j
        
        m = directions_c[i][0]
        n = directions_c[i][1]
    
    return (m, n)

    
print(local_min_search_2D([[4, 5, 10, 19], [10, 2, 100, 300], [30, 40, 50, 600]]))
