import pandas as pd

# 1.1 Load dataset
file_path = "C:/Users/USER/Desktop/IBM HR Attrition/HR_Employee_Attrition_dataset.csv"
df = pd.read_csv(file_path)

# 1.2 Dataset shape
print("Dataset Shape (rows, columns):", df.shape)

# 1.3 Column details (data dictionary structure)
columns_info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.values,
    "Non-Null Count": df.notnull().sum().values,
    "Unique Values": [df[col].nunique() for col in df.columns]
})
print("\n--- Columns Info ---")
print(columns_info)

# 1.4 Separate numeric vs categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print("\nNumeric Columns:", numeric_cols)
print("Categorical Columns:", categorical_cols)

# 1.5 Missing values check
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]
print("\n--- Missing Values ---")
print(missing_values if not missing_values.empty else "No missing values found ✅")

# 1.6 Duplicate check
duplicate_count = df.duplicated().sum()
print("\nDuplicate Rows:", duplicate_count)

# 1.7 Basic statistical summary (numeric columns only)
print("\n--- Statistical Summary ---")
print(df.describe().T)

# 1.8 Target variable distribution (Attrition)
if "Attrition" in df.columns:
    attrition_distribution = df["Attrition"].value_counts(normalize=True) * 100
    print("\n--- Attrition Distribution (%) ---")
    print(attrition_distribution)
else:
    print("⚠️ Attrition column not found in dataset")
