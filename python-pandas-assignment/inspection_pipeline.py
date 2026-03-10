import pandas as pd

# Load the dataset
df = pd.read_csv("employees.csv")

print(f"First 5 rows : \n{df.head()}")
print()
print(f"Last 5 rows: \n{df.tail()}")
print()
print("Structural information:")
df.info()
print()
print(f"Summary statistics: \n{df.describe()}")
print()

# Select single column
age = df["Age"]
print(f"Age column: \n{age}")
print()

## Select multiple columns
data = df[["Name", "Department"]]
print("Selected Columns (Name and Department):")
print(data)
print()

## Filter rows
Salary = df[df["Salary"] > 50000]
print(f"Employees with salary > 50000: \n{Salary}")
