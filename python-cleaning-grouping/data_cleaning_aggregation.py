import pandas as pd 
import numpy as np 

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
#print(df)


## Detect and print missing values
data_missing = df.isnull()
print("Missing values in the dataset: \n", data_missing)
print()

## Fill missing salary values with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print("Salary column after filling missing values with mean: \n", df["Salary"])
print()

## Drop the Temporary_Notes column
df_dropped_notes = df.drop(columns=["Temporary_Notes"])
print("Dataset after dropping Temporary_Notes column: \n", df_dropped_notes)
print()

## Rename Salary to Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})
print("Dataset after renaming Salary column to Annual_Salary: \n", df)
print()

## Group by Department and calculate average Annual_Salary
df_department_grouped = df.groupby("Department")["Annual_Salary"].mean()
print("Average Annual Salary by Department: \n", df_department_grouped)
print()

## Group by employees and count number of employees in each department
df_employee_count = df.groupby("Department")["Employee"].count()
print("Number of employees in each department: \n", df_employee_count)
print()

summary = df.groupby("Department").agg({
    "Annual_Salary": "mean",
    "Employee": "count"
})
print("Final Summary Table:")
print(summary)

