import pandas as pd

df = pd.read_csv("sales_with_nan_test.csv")
#print(df)

df_2 = df.drop(columns=["Price", "Quantity"])
print(df_2)