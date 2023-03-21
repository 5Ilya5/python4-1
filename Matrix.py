A = [[8, 7, 5], 
        [3, 4, 9], 
        [9, 6, 6], 
        [0, 5, 3]] 
transResult = [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]]
for a in range(len(A)): 
    for b in range(len(A[0])): 
        transResult[b][a] = A[a][b]
print("The transpose of matrix A is: ") 
for res in transResult: 
    print(res)