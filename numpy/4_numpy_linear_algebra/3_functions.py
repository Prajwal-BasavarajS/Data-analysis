import numpy as np

# 1. matmul() - Matrix product of two arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
res_matmul = np.matmul(A, B)
print("matmul:\n", res_matmul)

# 2. inner() - Inner product of two arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
res_inner = np.inner(x, y)
print("inner:", res_inner)

# 3. outer() - Compute the outer product of two vectors
res_outer = np.outer(x, y)
print("outer:\n", res_outer)

# 4. linalg.multi_dot() - Dot product of two or more arrays with optimal order
C = np.array([[1, 2], [3, 4]])
D = np.array([[2, 0], [1, 2]])
E = np.array([[0, 1], [2, 3]])
res_multi_dot = np.linalg.multi_dot([C, D, E])
print("multi_dot:\n", res_multi_dot)

# 5. tensordot() - Tensor dot product along specified axes
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
res_tensordot = np.tensordot(a, b, axes=1)  # sum over last axis of a, first of b
print("tensordot:\n", res_tensordot)

# 6. einsum() - Einstein summation
res_einsum = np.einsum('ij,jk->ik', A, B)  # same as matmul
print("einsum:\n", res_einsum)

# 7. einsum_path() - Shows the lowest-cost contraction path
path_info = np.einsum_path('ij,jk,kl->il', A, B, E, optimize='optimal')
print("einsum_path:\n", path_info)

# 8. linalg.matrix_power() - Raise a square matrix to an integer power
res_power = np.linalg.matrix_power(A, 3)  # A^3
print("matrix_power:\n", res_power)

# 9. kron() - Kronecker product of two arrays
res_kron = np.kron(A, B)
print("kron:\n", res_kron)
