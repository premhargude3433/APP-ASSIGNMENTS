# Experiment No. 12
# Title: Exploratory Data Analysis (EDA)

# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 2. Load the customer churn dataset
df = pd.read_csv("customer_churn.csv")

# 3. Display first few records
print("First Five Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display column names
print("\nColumn Names:")
print(df.columns)

# 4. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Select numerical columns
num = df.select_dtypes(include=['number'])

for col in num.columns:
    print("\nColumn:", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Mode:", df[col].mode()[0])
    print("Standard Deviation:", df[col].std())
    print("Variance:", df[col].var())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Quantiles:", df[col].quantile([0.25, 0.5, 0.75]))

# 5. Data Visualization

# Histogram
for col in num.columns:
    plt.figure()
    plt.hist(df[col].dropna(), bins=10, edgecolor='black')
    plt.title("Histogram of " + col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# Box Plot
for col in num.columns:
    plt.figure()
    sns.boxplot(y=df[col])
    plt.title("Box Plot of " + col)
    plt.show()

# Scatter Plot (first two numerical columns)
if len(num.columns) >= 2:
    plt.figure()
    plt.scatter(df[num.columns[0]], df[num.columns[1]])
    plt.xlabel(num.columns[0])
    plt.ylabel(num.columns[1])
    plt.title("Scatter Plot")
    plt.show()

# Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(num.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 6. Handling Missing Data
print("\nMissing Values:")
print(df.isnull().sum())

# Fill numerical missing values with mean
for col in num.columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical missing values with mode
for col in df.select_dtypes(include=['object']).columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nCleaned Dataset:")
print(df)

# 7. Detecting Outliers using Z-score
num = df.select_dtypes(include=['number'])

if len(num.columns) > 0:
    z_scores = num.apply(
        lambda col: zscore(col) if col.nunique() > 1 else 0
    )

    print("\nZ-Scores:")
    print(z_scores)

    # Identify outliers
    outliers = (z_scores.abs() > 3)
    print("\nDetected Outliers:")
    print(df[outliers.any(axis=1)])

    # Remove outliers
    df_no_outliers = df[~outliers.any(axis=1)]
    print("\nDataset After Removing Outliers:")
    print(df_no_outliers)

    # 8. Capping Outliers
    def cap_values(series):
        upper_limit = series.mean() + 3 * series.std()
        lower_limit = series.mean() - 3 * series.std()
        return series.clip(lower=lower_limit, upper=upper_limit)

    for col in num.columns:
        df[col] = cap_values(df[col])

# 9. Verify Cleaned Dataset
print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nFinal Dataset:")
print(df)

# 10. Save Cleaned Dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")
