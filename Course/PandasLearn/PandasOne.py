import numpy as np
import pandas as pd

# df = pd.read_csv('salaries.csv') #data frame of salaries.csv
#
# print(df['Salary']) #grabs only salary column
# print(df[['Name','Salary']]) #grabs name and salary columns
#
# print(df['Salary'].mean()) #returns avg salary
#
# ser_of_bool = df['Age']>30
# print(ser_of_bool)
# #print(df[ser_of_bool])
# print(df[df['Age']>30])
#
# print(df['Age'].unique()) #unique age values
# print(df['Age'].nunique()) #number of unique age values
# print(df.columns) #gets column names
# print(df.info()) #info regarding the data frame
# print(df.describe()) #detailed info regarding the data frame
# print(df.index) #info regarding the data frame range

mat = np.arange(0,50).reshape(5,10)
df = pd.DataFrame(data=mat)
print(df)

print('\n')

mat = np.arange(0,10).reshape(5,2)
df = pd.DataFrame(data=mat, columns=['A','B'])
print(df)