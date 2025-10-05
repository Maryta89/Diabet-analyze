# Diabetes Dataset Cleaning and Visualization (Improved Version)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load the dataset
df = pd.read_csv("diabetes_dataset.csv")

# 2️⃣ Basic inspection
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.info())
print(df.describe())

# 3️⃣ Data Cleaning
# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Strip extra spaces from column names
df.columns = df.columns.str.strip()

# Remove outliers using the IQR method
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]

# 4️⃣ Create individual plots

# 1. Distribution Plot
plt.figure(figsize=(8, 6))
sns.histplot(df[numeric_cols[0]], kde=True, bins=30)
plt.title(f"Distribution of {numeric_cols[0]}")
plt.xlabel(numeric_cols[0])
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("1_distribution.png")
plt.close()

# 2. Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=df[numeric_cols[1]])
plt.title(f"Boxplot of {numeric_cols[1]}")
plt.xlabel(numeric_cols[1])
plt.tight_layout()
plt.savefig("2_boxplot.png")
plt.close()

# 3. Correlation Heatmap
plt.figure(figsize=(14, 10))
corr = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap (Numerical Columns)")
plt.tight_layout()
plt.savefig("3_heatmap.png")
plt.close()

# 4. Barplot (for categorical column if available)
categorical_cols = df.select_dtypes(include=['object']).columns
if len(categorical_cols) > 0:
    plt.figure(figsize=(8, 6))
    sns.countplot(x=df[categorical_cols[0]])
    plt.title(f"Barplot of {categorical_cols[0]}")
    plt.xlabel(categorical_cols[0])
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("4_barplot.png")
    plt.close()

# 5. Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]])
plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
plt.xlabel(numeric_cols[0])
plt.ylabel(numeric_cols[1])
plt.tight_layout()
plt.savefig("5_scatterplot.png")
plt.close()

# 6. Pairplot (save separately using seaborn)
pair_cols = numeric_cols[:4]  # use first 4 numerical columns
sns.pairplot(df[pair_cols], diag_kind="kde", plot_kws={'alpha': 0.5})
plt.suptitle("Pairplot of First Four Numerical Columns", y=1.02)
plt.savefig("6_pairplot.png")
plt.close()

print("✅ All charts created and saved successfully!")
