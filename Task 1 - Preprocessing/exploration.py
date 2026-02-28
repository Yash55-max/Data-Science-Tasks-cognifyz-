import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Dataset .csv"
df = pd.read_csv(file_path)

# 1. Explore the dataset
print("--- Dataset Exploration ---")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn Information:")
print(df.info())

# 2. Check for missing values
print("\n--- Missing Values ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# 3. Handle missing values (if any)
# I will decide how to handle them after seeing which columns have missing values.

# 4. Analyze target variable distribution
print("\n--- Target Variable Analysis ('Aggregate rating') ---")
print(df['Aggregate rating'].describe())
print("\nValue Counts for 'Aggregate rating':")
print(df['Aggregate rating'].value_counts().sort_index())

# Plot distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], kde=True, bins=20)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.savefig('rating_distribution.png')
print("\nHistogram saved as 'rating_distribution.png'")
