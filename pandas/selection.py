import pandas as pd 

df = pd.read_csv("employees.csv")

#print(df.head())

x = df["JoinYear"]

# print(x)

y = df[["Name", "Department"]]

#print(y)

z = df[["Name", "Department", "Salary"]]

print(z)