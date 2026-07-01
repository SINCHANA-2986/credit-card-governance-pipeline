import pandas as pd

df = pd.read_csv("data/creditcard.csv")

print("Running quality checks...")

null_counts = df.isnull().sum()
duplicates = df.duplicated().sum()
negative_amounts = (df["Amount"] < 0).sum()

expected_columns = ['Time'] + [f'V{i}' for i in range(1,29)] + ['Amount', 'Class']
schema_valid = list(df.columns) == expected_columns

print("\nNull Counts:")
print(null_counts)

print("\nDuplicates:", duplicates)
print("Negative Amounts:", negative_amounts)
print("Schema Valid:", schema_valid)