import pandas as pd

# -----------------------------
# 1. Create messy CSV data
# -----------------------------
data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4
"""

with open("sample.csv", "w") as f:
    f.write(data)

# -----------------------------
# 2. Read CSV with multiple delimiters
# -----------------------------
df = pd.read_csv(
    "sample.csv",
    sep=r'[:,|_]',     # regex for mixed delimiters
    engine="python"
)

# -----------------------------
# 3. Clean column names
# -----------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.replace(r'\s+', '_', regex=True)
      .str.lower()
)

# -----------------------------
# 4. Strip whitespace from values
# -----------------------------
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# -----------------------------
# 5. Rename columns clearly
# -----------------------------
df.columns = [
    "total_bill",
    "tip",
    "sex",
    "smoker",
    "day",
    "time",
    "size"
]

# -----------------------------
# 6. Convert data types (optional but recommended)
# -----------------------------
df["total_bill"] = pd.to_numeric(df["total_bill"])
df["tip"] = pd.to_numeric(df["tip"])
df["size"] = pd.to_numeric(df["size"])

# -----------------------------
# 7. Save cleaned CSV
# -----------------------------
df.to_csv("sample_cleaned.csv", index=False)

# -----------------------------
# 8. Display result
# -----------------------------
print(df)
print("\nCleaned CSV saved as 'sample_cleaned.csv'")
