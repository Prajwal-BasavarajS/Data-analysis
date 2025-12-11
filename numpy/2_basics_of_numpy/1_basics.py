import numpy as np


# single dimensional array 


a = [1,2,3,2,5,6,3,2,1,6,89,9]

arr = np.array(a)

print(sorted(arr),"\n")
print()
print(type(arr))



#  shape 
#  multi-dimensional array

b = [12,13,14,15,16]
c = [22,21,23,24,25]
e = [31,32,33,43,35]
f = [41,42,43,44,45]
g = [51,52,53,54,55] 

arr_2 = np.array([b,c,e,f,g])

print("\n",arr_2,"\n")
print(arr_2.shape,"\n")




# dtype


arr_3 = np.array([1.2,1.3,1.4,2.0])

# in array we can write array(2.1) or just pass one argument 
# and cannot pass more than one argument to get the dtype or do any process

print(arr_3.dtype)


# fromiter

var = "Prajwal"

arr_4 = np.fromiter(var,dtype="U2",count=-1)

print(arr_4)


#  numpy.arange( start , stop, step , dtype = None )

arr_5 = np.arange(0,20,3,dtype=float)

print(arr_5)



arr_6 = np.ones([4,4],order = 'f')

arr_7 = np.empty([4,4],dtype=np.int32 ,order = 'c')

print(arr_6)
print()
print(arr_7)


arr_8 = np.linspace(2,30,2)

print(arr_8)








aa = np.linspace(2, 10, 5, 
            dtype = np.int32)

print("\n",aa)



bb= np.empty([4, 3],
         dtype = np.int32,
         order = 'c')
print("\n",bb)



cc = np.ones([4, 3], 
         dtype = np.int64,
         order = 'f')


print("\n",cc)


import numpy as np

# Create a NumPy array
arr10 = np.array([1, 2, 3, 4, 5.2])

# Check the data type of the array
data_type = arr10.dtype
print(data_type)



import numpy as np

arr1 = np.array([1, 2, 3, 4], dtype=np.float64)  

# Creating a 3x3 int32 array of zeros
arr2 = np.zeros((3, 3), dtype=np.int32)  

# Creating a 2x2 complex128 array of ones
arr3 = np.ones((2, 2), dtype=np.complex128)  
print(arr3)
# Creating a 1D bool array
arr4 = np.empty((4,), dtype=np.bool_)  

# Print the arrays and their data types
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)