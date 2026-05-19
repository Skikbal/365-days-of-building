matrix = [[1,2,3],[4,5,6],[7,8,9]]


transpose = [[0,0,0],[0,0,0],[0,0,0]]

for i in range (len(matrix)): 
    for j in range(len(matrix[i])):
        transpose[i][j] = matrix[j][i]

print(transpose)
     