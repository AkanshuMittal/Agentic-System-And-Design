import pandas as pd 

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Math": [90, 80,85],
    "Science": [88, 92, 89]
}

df = pd.DataFrame(data)
print(df)

# Created index automatically
# Understand data type automatically 
# Formatted as table 