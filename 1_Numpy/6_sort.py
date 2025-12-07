import numpy as np

d_type = [("name",'S10'),('year',int),('cgpa',float)]
vals = [('prajwal',2002,9.2),("pankaj",2003,9.2),("kshema",2002,9.2)]
a = np.array(vals,dtype=d_type)
print(np.sort(a,order=['year','cgpa']))
