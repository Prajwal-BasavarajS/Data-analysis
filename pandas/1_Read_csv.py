import pandas as pd

df = pd.read_csv("/Users/prajwal/Desktop/Data_analysis/pandas/December 2016 Sales.csv")
df = pd.read_csv("/Users/prajwal/Desktop/Data_analysis/pandas/December 2016 Sales.csv",usecols=["Date" , "Transaction Amount"])
df = pd.read_csv("/Users/prajwal/Desktop/Data_analysis/pandas/December 2016 Sales.csv",index_col= "Cashier")
df = pd.read_csv("/Users/prajwal/Desktop/Data_analysis/pandas/December 2016 Sales.csv",na_values= ["N/A","Unknown"])

print(df)



# Sample data stored in a multi-line string
data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4
"""

# Save the data to a CSV file
with open("sample.csv", "w") as file:
    file.write(data)
print(data)


# Load the CSV file using pandas with multiple delimiters
df1 = pd.read_csv('sample.csv',
                 sep='[:, |_]',  # Define the delimiters
                 engine='python')  # Use Python engine for regex separators

df2 = pd.read_csv("/Users/prajwal/Desktop/Data_analysis/sample.csv", na_values=["Nan","unknown"])
print(df1)

with open("sample2.csv", "w") as file:
           file.write(df1)

print(df2)