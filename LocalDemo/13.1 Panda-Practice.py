from loguru import logger
import pandas as pd

import pandas as pd

# -----------------------------
# Step 1: Read source CSV
# -----------------------------
df = pd.read_csv(r"C:\Users\rohitbod@amdocs.com\Desktop\empdetails.csv")

# -----------------------------
# Step 2: Standardize column names
# -----------------------------
df.columns = df.columns.str.strip().str.lower()

# -----------------------------
# Step 3: Clean string columns
#   - Remove quotes
#   - Trim extra spaces
# -----------------------------
string_cols = ['empname', 'email']

for col in string_cols:
    df[col] = (df[col].astype(str).str.replace('"', '', regex=False).str.strip())

# -----------------------------
# Step 4: Normalize text casing
# -----------------------------
df['empname'] = df['empname'].str.title()
df['email'] = (
    df['email']
      .astype(str)
      .str.strip()
      .str.lower()
)

# -----------------------------
# Step 5: Handle NULL / invalid values
# -----------------------------
df = df.replace(['null', 'None', 'nan', ''], pd.NA)

# Convert numeric columns safely
df['empid'] = pd.to_numeric(df['empid'], errors='coerce')
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# Drop rows where empid is missing
df = df.dropna(subset=['empid'])

# -----------------------------
# Step 6: Remove duplicate employees
# Business rule: empid should be unique
# -----------------------------
df = df.drop_duplicates(subset=['empid'], keep='first')

# -----------------------------
# Step 7: Reset index
# -----------------------------
df = df.reset_index(drop=True)

# -----------------------------
# Step 8: Save cleaned data
# -----------------------------
df.to_excel("emp_details_cleaned.xlsx", index=False)
df.to_csv("emp_details_cleaned.csv", index=False)

logger.info("Data cleaning completed successfully.")
