import pandas as pd 

df = pd.read_csv("sales_with_nan_test.csv")
#print(df)

# how to find revenue
df["Revenue"] = df["Quantity"] * df["Price"]
#print(df)

# What is the total revenue per city ?
df_rev = df.groupby("City")["Revenue"].sum()
print(df_rev)

# Which city earn most ?
df_sorted = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print(df_sorted)

# What is the average revenue in each city ?
df_avg = df.groupby("City")["Revenue"].mean()
print(df_avg)

