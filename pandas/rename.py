import pandas as pd

df = pd.read_csv("sales_with_nan_test.csv")
print(df)

df = df.rename(columns={"Price": "Unit_Price", "Quantity": "Units_Sold"})
print(df)