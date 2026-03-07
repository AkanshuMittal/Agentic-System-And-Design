import pandas as pd 

df = pd.read_csv("employees.csv")

x = df[(df["Department"] == "AI") & (df["Salary"] > 80000)][["Name", "Salary"]].sort_values("Salary", ascending=False)
print(x)

# y = x[["Name", "Salary"]]
# print(y)

# z = y.sort_values("Salary", ascending=False)
# print(z)