import numpy as np 

a = np.array([1,2,4,5,3]) 

print(a[0])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[1, 1])

import numpy as np

cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]],
                  [[19,20,21],
                   [22,23,24],
                   [25,26,27]]])


print(cube[2, 1 , 2])





cube = np.random.rand(4, 4, 4)
print("\n",cube,"\n")

print(cube[..., 0])





arr = np.array([[1, 2],
                [3, 4]])

# Add new axis → shape becomes (1, 2, 2)
arr_new = arr[np.newaxis, :, :]

# Now add new "blocks" along the new axis
extra = np.array([[5, 6],
                  [7, 8]])

extra = extra[np.newaxis, :, :]

# Concatenate along axis 0
result = np.concatenate([arr_new, extra], axis=0)

print(result)
print("Shape:", result.shape)




arr = np.array([[1, 2],
                [3, 4]])

extra = np.array([[5, 6],
                  [7, 8]])

result = np.stack([arr, extra], axis=0)

print(result)
print("Shape:", result.shape)


a = np.array([[[2,3,4],
              [2,3,4],
              [2,3,4]],
              [[6,7,8],
               [6,7,8],
               [6,7,8]],
               [[10,11,12],
                [11,12,13],
                [11,12,13]]])

print(np.ndim(a))


