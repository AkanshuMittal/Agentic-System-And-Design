import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [25,30],
    "Salary": [50000, 60000]
}

df = pd.DataFrame(data)

print(df)