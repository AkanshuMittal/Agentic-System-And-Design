import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 92, 80, 88, 76, 90],
    "Passed": [False, True, False, True, False, True],
    "Category": ["A", "A", "B", "C", "C", "A"]
}

# Convert data to DataFrame
df = pd.DataFrame(data)
# print(df)
# print()

## Select single column
print("Name Column: \n", df["Name"])
print()

## Select multiple columns
selected_columns = df[["Name", "Score"]]
print("Selected Columns (Name and Score): \n", selected_columns)
print()

## Filter rows using iloc
filtered_rows = df.iloc[0:3]
print("Filtered Rows (using iloc): \n", filtered_rows)
print()

# Set index
df_indexed = df.set_index("Name")
print("DataFrame with Name as index: \n", df_indexed)
print()

# loc usage
print("Using loc to get data:")
print(df_indexed.loc["Bob"])
print()

# Filter rows where Score > 85
score_filter_rows = df[df["Score"] > 85]
print("Rows where Score > 85: \n", score_filter_rows)
print()

# Filter rows where Score > 85 and Passed is True
complex_filter_rows = df[(df["Score"] > 85) & (df["Passed"] == True)]
print("Rows where Score > 85 and Passed is True: \n", complex_filter_rows)
print()

# Sort the filtered rows in descending order of Score
sorted_filtered_rows = complex_filter_rows.sort_values("Score", ascending=False)
print("Sorted Filtered Rows (by Score descending): \n", sorted_filtered_rows)
print()

# Chain filtering and sorting
chained_result = df[df["Score"] > 85].sort_values("Score", ascending=False)[["Name", "Score"]]
print("High-performing students: \n", chained_result)