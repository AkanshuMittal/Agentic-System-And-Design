import pandas as pd 

df = pd.read_csv("employees.csv")

# Sorting by single column
x = df.sort_values("Salary", ascending=False)
print(x)

# Sorting by multiple columns
y = df.sort_values(["Department", "Salary"], ascending=[True, False])
print(y)

z = df.sort_index(ascending=False)
print(z)