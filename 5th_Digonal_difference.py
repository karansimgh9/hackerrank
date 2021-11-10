def difference(arr, n): 
  
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
      
        for j in range(0, n): 
          
            if (i == j): 
                d1 += int(arr[i][j]) 
   
            if (i == n - j - 1): 
                d2 += int(arr[i][j]) 
    return abs(d1 - d2); 
n = int(input(''))
arr = []
for i in range(n):
    row = str(input('')).split()
    arr.append(row)
print(difference(arr,n))
