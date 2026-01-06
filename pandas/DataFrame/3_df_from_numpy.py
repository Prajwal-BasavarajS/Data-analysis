import numpy as np
import pandas as pd

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

df = pd.DataFrame(arr,columns=["1D",'2D','3D'])

print(df)

