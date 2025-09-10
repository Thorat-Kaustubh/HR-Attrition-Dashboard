import pandas as pd

# Load dataset (use forward slashes in path)
file_path = "C:/Users/USER/Desktop/IBM HR Attrition/HR_Employee_Attrition_dataset.csv"
df = pd.read_csv(file_path)

# 2.1 Handle missing values
print("Missing values before cleaning:\n", df.isnull().sum().sum())
df = df.dropna()  # (no missing values here, but keeping step for robustness)
print("Missing values after cleaning:\n", df.isnull().sum().sum())

# 2.2 Handle duplicates
print("Duplicate rows before cleaning:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate rows after cleaning:", df.duplicated().sum())

# 2.3 Feature Engineering

# Salary Band
def salary_band(income):
    if income < 5000:
        return "Low"
    elif 5000 <= income <= 10000:
        return "Medium"
    else:
        return "High"

df["SalaryBand"] = df["MonthlyIncome"].apply(salary_band)

# Age Group
def age_group(age):
    if 20 <= age < 30:
        return "20-29"
    elif 30 <= age < 40:
        return "30-39"
    elif 40 <= age < 50:
        return "40-49"
    else:
        return "50+"

df["AgeGroup"] = df["Age"].apply(age_group)

# Experience Group
def experience_group(years):
    if years < 3:
        return "Early Career"
    elif 3 <= years <= 7:
        return "Mid Career"
    else:
        return "Senior"

df["ExperienceGroup"] = df["YearsAtCompany"].apply(experience_group)

# Check new columns
print("\n--- New Derived Columns (Sample) ---")
print(df[["MonthlyIncome", "SalaryBand", "Age", "AgeGroup", "YearsAtCompany", "ExperienceGroup"]].head(10))

# 2.4 Save cleaned dataset
output_path = "C:/Users/USER/Desktop/IBM HR Attrition/HR_Employee_Attrition_Cleaned.csv"
df.to_csv(output_path, index=False)
print("\n✅ Cleaned dataset saved to:", output_path)
