import pandas as pd

df = pd.read_csv("sales_with_nan_test.csv")
print(df)
# Detect missing data 
x = df.isnull()
#print(x)

# Count missing data in each column
y = df.isnull().sum()
#print(y)

# Drop missing value
df_clean = df.dropna()
#print(df_clean)

# Drop only rows where quantity is missing
df_clean2 = df.dropna(subset=["Quantity"])
#print(df_clean2)

df_clean3 = df.dropna(subset=["Quantity", "Price"])
#print(df_clean3)

# Drop columns with missing values 
z = df.dropna(axis=1)
#print(z)

## Strategy 2: Fill missing values with mean or median

# Fill quantity with zero
df["Quantity"] = df["Quantity"].fillna(0)
#print(df)

# Fill value with mean and median 

df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df)

df["Price"] = df["Price"].fillna(df["Price"].median())
print(df)