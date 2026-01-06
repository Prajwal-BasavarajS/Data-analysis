import pandas as pd 

lst = ["geeks","for",'geeks',"have","good","content"]

df1 = pd.DataFrame(lst)

print(df1)


names = ['Prajwal', 'kavya','Abhi','Parth']
degree = ['Engineer', "Engineer", "BSC","Engineer"]
birth_rank = [1,2,3,4]

df2 = pd.DataFrame({"Names":names,"Degree":degree,"Birth Rank": birth_rank})

print("\n",df2,"\n")


df3 = pd.DataFrame(list(zip(names,degree,birth_rank)),columns=['Names',"Degree","Birth_rank"])

print("\n",df3,"\n")

lst_1 = [["tom",22],["krishna",21],['rani',24],['raju',33],['mika',31]]

df_4 = pd.DataFrame(lst_1,columns=['Names','Age'])

print("\n",df_4,"\n")

lst_2 = [["tom","pete",22],["krishna","radha",21],['rani','mukherjee',24],['raju',"bheem",33],['milka',"singh",31]]

df5 = pd.DataFrame(lst_2,columns=["First-Name", 'Last-name','Age'])

print("\n",df5,"\n")


df5["Age"] = df5['Age'].astype(float)

print("\n",df5,"\n")



lst_3 = ['raju','rani','bheem','jaggu']

df6 = pd.DataFrame(lst_3,index = ['a','b','c','d'],columns=["names"])

print("\n",df6,"\n")


lst_4 = [1,2,4,5,6]

df7 = pd.DataFrame(lst_4,columns=["Numbers"],index=['i','ii','iii','iv','v'])

print("\n",df7,"\n")

