import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Imports and style

sns.set_theme(style="whitegrid", context="notebook")

palette = {
    "No": "#378ADD",
    "Yes": "#D85A30"
}

# Load data

df = pd.read_csv("data/raw/employees.csv")

# Feature engineering

df["Exited"] = df["Attrition"].map({"Yes": 1, "No": 0})

df["SalaryBand"] = pd.cut(
    df["MonthlyIncome"],
    bins=[0, 4000, 7000, float("inf")],
    labels=["Low", "Medium", "High"]
)


# 1 - Salary Band x Overtime

plot_df = (
    df.groupby(["SalaryBand", "OverTime"], observed=True)["Exited"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={"Exited": "AttritionRate"})
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=plot_df,
    x="SalaryBand",
    y="AttritionRate",
    hue="OverTime",
    palette=palette
)

plt.title("Attrition Rate by Salary Band and Overtime", fontsize=14, pad=12)
plt.xlabel("Salary Band")
plt.ylabel("Attrition Rate (%)")
plt.legend(title="OverTime")
plt.tight_layout()

plt.savefig("images/attrition_salary_overtime.png", dpi=300, bbox_inches="tight")
plt.show()


# 2 - Job Satisfaction

attrition_jobsatisfaction = (
    df.groupby("JobSatisfaction")["Exited"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={"Exited": "AttritionRate"})
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=attrition_jobsatisfaction,
    x="JobSatisfaction",
    y="AttritionRate",
    hue="JobSatisfaction",
    palette="Blues_d",
    legend=False
)

for i, v in enumerate(attrition_jobsatisfaction["AttritionRate"]):
    plt.text(i, v + 1, f"{v:.1f}%", ha="center", fontsize=10)

plt.title("Attrition Rate by Job Satisfaction", fontsize=13, pad=10)
plt.xlabel("Job Satisfaction")
plt.ylabel("Attrition Rate (%)")
plt.ylim(0, 30)

plt.tight_layout()

plt.savefig("images/attrition_job_satisfaction.png", dpi=300, bbox_inches="tight")
plt.show()


# 3 - Tenure

df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[0, 2, 7, float("inf")],
    labels=["Early", "Mid", "Senior"]
)

tenure_df = (
    df.groupby("TenureGroup", observed=True)["Exited"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={"Exited": "AttritionRate"})
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=tenure_df,
    x="TenureGroup",
    y="AttritionRate",
    hue="TenureGroup",
    palette="Blues_d",
    legend=False
)

for i, v in enumerate(tenure_df["AttritionRate"]):
    plt.text(i, v + 1, f"{v:.1f}%", ha="center", fontsize=10)

plt.title("Attrition Rate by Tenure", fontsize=13, pad=10)
plt.xlabel("Tenure Group")
plt.ylabel("Attrition Rate (%)")
plt.ylim(0, 32)

plt.tight_layout()

plt.savefig("images/attrition_tenure.png", dpi=300, bbox_inches="tight")
plt.show()