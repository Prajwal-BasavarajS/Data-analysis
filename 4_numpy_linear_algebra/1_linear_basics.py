import numpy as np

a = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# rank 

print("\nrank of matrix A : ",np.linalg.matrix_rank(a))

print("\nTrace of matrix A : ", np.trace(a) )

print("\nDeterminant of matrix A is : ", np.linalg.det(a))

print("\ninverse of matrix A :\n", np.linalg.inv(a))

print("\nMAtrix raise power of matrix A is :\n ", np.linalg.matrix_power(a,2),"\n")

