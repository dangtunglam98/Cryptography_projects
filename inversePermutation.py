def matrix_multi(A, B):
    result = [[0 for col in range(len(B[0]))] for row in range(len(A))]

    for row in range(len(A)):
        for col in range(len(B[0])):
            for item in range(len(B)):
                result[row][col] += A[row][item] * B[item][col]
    
    print(result)

matrix1 = [[12,7,3], 
		[4 ,5,6], 
		[7 ,8,9]] 
matrix2 = [[5,8,1,1], 
		[6,7,3,2], 
		[4,5,9,3]] 
matrix_multi(matrix1, matrix2)