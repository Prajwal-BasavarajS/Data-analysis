import numpy as np

# dot or matrix multiplication

a = np.array([[1,2],[3,4]])

b = np.array([[2,2],[2,2]])

res = np.dot(a,b)

print(res)


c = 2 + 3j

d = 3 + 4j

res1 = np.dot(c,d)

print("\n",res1)


# vdot 

e = 2 + 3j

f = 3 + 4j

res2 = np.vdot(e,f)

print("\n",res2)
