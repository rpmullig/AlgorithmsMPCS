''' 
Searches a 2D matrix and returns a local minimum (in the north, south, east,
west directions). 
Assumption:
    There always exists a local minimum in a matrix
'''
def local_min_search_2D(arr):
    
    row = (len(arr) - 1)         # boundary check variable
    col = (len(arr[0]) - 1)      # boundary check variable
    
    m = (len(arr) - 1) // 2      # mid row
    n = (len(arr[0]) - 1) // 2   # mid col
    
    current = up = down = left = right = arr[m][n]    # set everything to center
    
    # increment directions, but only if possible and not out of bounds 
    if m < row:
        up = arr[m+1][n]
    if m > 0:
        down = arr[m-1][n]
    if n < col:
        left    = arr[m][n+1]
    if n > col:
        right = arr[m][n+1]

    while current > up or current > down or current > left or current > right:
        
        directions_val  = [up, down, left, right] 
        directions_cord = [[m+1, n],[m-1,n],[m,n+1],[m, n-1]] 
        
        i = 0
        tmp = up
        for j in range(2, 4):
            if directions[i] < tmp:
                i = j
        
        m = directions_c[i][0]
        n = directions_c[i][1]    
            
        current = arr[m][n]
        
        # increment directions, but only if possible and not out of bounds 
        if m < row:
            up = arr[m+1][n]
        if m > 0:
            down = arr[m-1][n]
        if n < col:
            left    = arr[m][n+1]
        if n > col:
            right = arr[m][n+1]


    return (m, n)

    
print(local_min_search_2D([[4, 5, 10, 19], [10, 2, 100, 300], [30, 40, 50, 600]]))
