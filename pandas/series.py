import pandas as pd 

arr = pd.Series([90, 85, 80])
print(arr)
print()

arr_2 = pd.Series([90, 85, 80], index=["Alice", "Bob", "Charlie"])
print(arr_2)
print()


## Suppose you are analyzing 
# Daily Temperature

# How will you create a pandas series

temp = pd.Series([30, 32, 28, 31], index=["Monday", "Tuesday", "Wednesday", "Thursday"])
print(temp) 