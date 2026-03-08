import pandas as pd

df = pd.read_csv("sales_with_nan_test.csv")
#print(df)

df["Revenue"] = df["Quantity"] * df["Price"]
#print(df)

df_avg = df.groupby("City")["Revenue"].mean()
#print(df_avg)

#print(df)

# how many orders per region ??

df_count = df.groupby("City")["Order_ID"].count()
#print(df_count)

# count ignores NaN

# Difference between count and size 
df_size = df.groupby("City").size()
#print(df_size)


# Show sum, mean and count together
df_agg = df.groupby("City")["Revenue"].agg(["sum", "mean", "count"])
#print(df_agg)

# Revenue only on sum and mean and count of OrderID

df_agg2 = df.groupby("City").agg({
    "Revenue": ["sum", "mean"],
    "Order_ID": "count"
})
print(df_agg2)