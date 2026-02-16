#  Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.  
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]  
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]] 
matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sorted_matrix = sorted(matrix, key=lambda row: sum(row))
print(sorted_matrix)