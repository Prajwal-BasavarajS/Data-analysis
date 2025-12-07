# Broadcasting in NumPy allows us to perform arithmetic operations on arrays of 
# different shapes without reshaping them. It automatically adjusts the smaller 
# array to match the larger array's shape by replicating its values along the 
# necessary dimensions. This makes element-wise operations more efficient by reducing 
# memory usage and eliminating the need for loops.

 


import numpy as np 


#  scalar to 1D

a = np.array([[1,2,3],[4,5,6]])

print("dimensions = ",np.ndim(a))

print("\nshape = ",a.shape)

x = 10

print("""\na+x= [ 1 2 3
       4 5 6] + [10]  \n\n""",a+x)


# 1D to 2D 


a1 = np.array([[1,2,3],[4,5,6]])

b1 = np.array([10,20,30])

print("\n",a1+b1)


# broadcasting in conditional operations 

a2 = np.array([12,14,19,21,2,55,33,15])

b2 = np.array(["adult","Child"])


res = np.where(a2>18,b2[0],b2[1])

print("\n",a2)
print(" ",b2)
print("\n",res)


# broadcasting matrix multiplication

a3  = np.array([10,20,20])

b3 = np.array([[20,30,40],[50,60,70]])

print("\n",b3*a3)



fd = np.array([ [0.8, 2.9, 3.9],
                [52.4, 23.6, 36.5],
                [55.2, 31.7, 23.9],
                [14.4, 11.0, 4.9] ])

cpg = np.array([9, 4, 4])
res = fd * cpg
print("\n\n",res)


# Adjusting Temperature Data Across Multiple Locations


temp = np.array([[30,32,34,33,31],
                 [25,27,29,28,26],
                 [20,22,24,23,21]])

corr = np.array([1.5,-0.5,2.1])

res = temp + corr[:,None]



print("\n\n",res)



#  normalizing image data

img = np.array([[100,120,130],
                [90,110,140],
                [80,100,120]])

m = img.mean(axis=1)

s = img.std(axis=1)

nor = (img-m)/s

print("\n\n",nor)



#  broadcasting for centring data in Machine Learning


data = np.array([[10,20],[30,40],[50,60]])

m = data.mean(axis = 0)

res = data - m 

print("\n",res)
