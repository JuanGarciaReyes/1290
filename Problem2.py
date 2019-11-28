def minFallingPathSum(arr):
    if len(arr) < 1:
        return
    for i in range(1,len(arr)):
        for j in range(len(arr[0])):
            if j==0:
               arr[i][j] += min([arr[i-1][j+1], arr[i-1][j]])
            elif j==len(arr[0])-1:
                arr[i][j] += min([arr[i-1][j-1], arr[i-1][j]])
            else:
                min([arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1]])
    return min(arr[-1])