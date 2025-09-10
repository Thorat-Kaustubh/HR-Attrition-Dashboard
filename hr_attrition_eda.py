import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="whitegrid", palette="Set2")

# Load cleaned dataset
file_path = "C:/Users/USER/Desktop/IBM HR Attrition/HR_Employee_Attrition_Cleaned.csv"
df = pd.read_csv(file_path)

# 3.1 Overall Attrition Rate
attrition_rate = df["Attrition"].value_counts(normalize=True) * 100
print("\n--- Overall Attrition Rate (%) ---\n", attrition_rate.round(1))

plt.figure(figsize=(5,5))
sns.countplot(data=df, x="Attrition", palette="Set1")
plt.title("Overall Attrition Distribution")
plt.ylabel("Number of Employees")
plt.show()

# 3.2 Attrition by Department
attrition_dept = (
    df.groupby("Department")["Attrition"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
).round(1)
print("\n--- Attrition by Department (%) ---\n", attrition_dept.sort_values("Yes", ascending=False))

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Department", hue="Attrition", palette="Set2")
plt.title("Attrition by Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.show()

# 3.3 Attrition by Job Role
attrition_jobrole = (
    df.groupby("JobRole")["Attrition"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
).round(1)
print("\n--- Attrition by Job Role (%) ---\n", attrition_jobrole.sort_values("Yes", ascending=False))

plt.figure(figsize=(12,6))
sns.countplot(data=df, x="JobRole", hue="Attrition", palette="Set3")
plt.title("Attrition by Job Role")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.show()

# 3.4 Attrition by Salary Band
attrition_salary = (
    df.groupby("SalaryBand")["Attrition"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
).round(1)
print("\n--- Attrition by Salary Band (%) ---\n", attrition_salary.sort_values("Yes", ascending=False))

plt.figure(figsize=(7,5))
sns.countplot(data=df, x="SalaryBand", hue="Attrition", palette="coolwarm")
plt.title("Attrition by Salary Band")
plt.ylabel("Number of Employees")
plt.show()

# 3.5 Attrition by Age Group
attrition_age = (
    df.groupby("AgeGroup")["Attrition"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
).round(1)
print("\n--- Attrition by Age Group (%) ---\n", attrition_age.sort_values("Yes", ascending=False))

plt.figure(figsize=(7,5))
sns.countplot(data=df, x="AgeGroup", hue="Attrition", palette="Set1")
plt.title("Attrition by Age Group")
plt.ylabel("Number of Employees")
plt.show()

# 3.6 Attrition by Experience Group
attrition_exp = (
    df.groupby("ExperienceGroup")["Attrition"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
).round(1)
print("\n--- Attrition by Experience Group (%) ---\n", attrition_exp.sort_values("Yes", ascending=False))

plt.figure(figsize=(7,5))
sns.countplot(data=df, x="ExperienceGroup", hue="Attrition", palette="Set2")
plt.title("Attrition by Experience Group")
plt.ylabel("Number of Employees")
plt.show()

# 3.7 Attrition by Overtime
if "OverTime" in df.columns:
    attrition_ot = (
        df.groupby("OverTime")["Attrition"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0) * 100
    ).round(1)
    print("\n--- Attrition by Overtime (%) ---\n", attrition_ot.sort_values("Yes", ascending=False))

    plt.figure(figsize=(6,5))
    sns.countplot(data=df, x="OverTime", hue="Attrition", palette="Set1")
    plt.title("Attrition by Overtime")
    plt.ylabel("Number of Employees")
    plt.show()

# 3.8 Attrition by Job Satisfaction
if "JobSatisfaction" in df.columns:
    attrition_jobsat = (
        df.groupby("JobSatisfaction")["Attrition"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0) * 100
    ).round(1)
    print("\n--- Attrition by Job Satisfaction (%) ---\n", attrition_jobsat.sort_values("Yes", ascending=False))

    plt.figure(figsize=(7,5))
    sns.countplot(data=df, x="JobSatisfaction", hue="Attrition", palette="viridis")
    plt.title("Attrition by Job Satisfaction")
    plt.ylabel("Number of Employees")
    plt.show()

# 3.9 Key Insights Summary (Dynamic)
print("\n📌 Key Insights:")

# Overall
overall_yes = attrition_rate.get("Yes", 0)
print(f"1. Overall attrition rate is around {overall_yes:.1f}%.")

# Department
top_dept = attrition_dept["Yes"].idxmax()
print(f"2. Highest attrition is seen in the {top_dept} department.")

# Salary Band
top_salary = attrition_salary["Yes"].idxmax()
print(f"3. Employees in the {top_salary} salary band face the most attrition.")

# Age Group
top_age = attrition_age["Yes"].idxmax()
print(f"4. Younger employees ({top_age}) tend to leave more often.")

# Experience
top_exp = attrition_exp["Yes"].idxmax()
print(f"5. Attrition is highest among {top_exp} employees.")

# Overtime
if "OverTime" in df.columns:
    top_ot = attrition_ot["Yes"].idxmax()
    print(f"6. Employees with Overtime = {top_ot} show higher attrition.")

# Job Satisfaction
if "JobSatisfaction" in df.columns:
    low_jobsat = attrition_jobsat["Yes"].idxmax()
    print(f"7. Employees with Job Satisfaction level = {low_jobsat} have higher attrition.")
