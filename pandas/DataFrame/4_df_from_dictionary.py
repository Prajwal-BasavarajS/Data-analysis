import pandas as pd 

dic = { "Names": ['Prajwal','Kavya','Sundar','Suma'],
       'Age':[24,22,24,22],
       "Class": ["A" , 'B','C','D' ]}

df_1 = pd.DataFrame(dic)
print('\n',df_1,'\n')


dic_1 = { "Names": ['Prajwal','Kavya','Sundar','Suma'],
       'Age':[24,22,24,22],
       "Class": ["A" , 'B','C','D' ]}


df_2 = pd.DataFrame(dic_1,index = ["roll_no_1","roll_no_2","roll_no_3","roll_no_4"])

print('\n',df_2,'\n')
