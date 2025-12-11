import numpy as np 

a_zeros = np.zeros((3,3))       #zeros

a_ones = np.ones((3,3))     #ones

a_arrange = np.arange(0,10,2)      #range 

print(a_zeros,"\n")
print(a_ones)
print(a_arrange)

x = np.array([12,12,4])

y = np.array([4,6,8])

print(x+y,"add")
print(x-y,"sub")
print(x*y,"multi")
print(x/y,"div")