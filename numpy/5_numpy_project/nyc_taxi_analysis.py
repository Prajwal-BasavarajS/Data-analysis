import numpy as np

data = np.genfromtxt("/Users/prajwal/Desktop/Data_analysis/numpy/5_numpy_project/nyc_taxis.csv",delimiter = ',' ,dtype = None , names = True,encoding='utf-8')

data1 = np.genfromtxt("numpy/5_numpy_project/nyc_taxis.csv",delimiter = ",",skip_header=1)

# print(data.dtype)
# print(data1[:,[3]])


# distance = data['trip_distance']
# fare = data['fare_amount']

# distane_2d = data[:7]               # 7 stands for 7th colum in excel i.e 8
# fare_2d = data[:9]

# # print(distance)

# print(fare_2d)
# subset = data[:, [7, 9, 12]]   # returns a 2D array with those 3 columns
# print(subset)


# clean_data = np.nan_to_num(data,nan = 0 )
# clean_data = data[~np.isnan(data).any(axis=1)]


# np.savetxt("output_cleaned.csv",clean_data,delimiter=",",fmt="%s")

# np.savetxt("output.csv",clean_data,delimiter=",",fmt= '%s')




fare = data["fare_amount"]
distance = data["trip_distance"]
fees_amount = data['fees_amount']
tip = data["tip_amount"]
toll_amount = data["tolls_amount"]

# correlation betwenn tip distance and fare amount 

correlation = np.corrcoef(distance,fare)[0,1]



mean_distance = np.mean(distance)
mean_fare = np.mean(fare)
total_tip = np.sum(tip)
total_toll_amount = np.sum(toll_amount)

z = (distance - distance.mean()) / distance.std()
outliers = np.where(np.abs(z) > 3)

print(outliers)

print("mean distance",mean_distance)
print("mean fare",mean_fare)
print("total tip",total_tip)
print("total toll amount",total_toll_amount)

print("\ncorrelation between distance and fare amount range(0-1) : ",correlation)

