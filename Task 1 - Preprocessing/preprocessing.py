import pandas as pd

# Load the dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Dataset .csv"
df = pd.read_csv(file_path)

print("--- Preprocessing ---")

# 1. Handle missing values
# Identify columns with missing values
missing_cols = df.columns[df.isnull().any()].tolist()
print(f"Columns with missing values: {missing_cols}")

# Fill missing values in 'Cuisines' with 'Unknown'
if 'Cuisines' in missing_cols:
    df['Cuisines'] = df['Cuisines'].fillna('Unknown')
    print("Filled missing values in 'Cuisines' with 'Unknown'")

# 2. Data Type Conversion
print("\n--- Data Type Check ---")
print(df.dtypes)

# Example: If 'Restaurant ID' is an object but should be int (it seems to be int64 already)
# Let's ensure 'Has Table booking' and 'Has Online delivery' are more useful (e.g., boolean or 0/1)
print("\nUnique values in categorical flags:")
print(f"Has Table booking: {df['Has Table booking'].unique()}")
print(f"Has Online delivery: {df['Has Online delivery'].unique()}")

# Convert yes/no to 1/0
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
print("Converted 'Has Table booking' and 'Has Online delivery' to binary (0/1)")

# 3. Analyze Class Imbalance in 'Aggregate rating'
print("\n--- Class Imbalance Analysis ---")
rating_counts = df['Aggregate rating'].value_counts().sort_index()
total_rows = len(df)
print(f"Total rows: {total_rows}")
print(f"Rows with 0.0 rating: {rating_counts.get(0.0, 0)} ({rating_counts.get(0.0, 0)/total_rows:.2%})")

# Categorizing ratings into groups for better imbalance visualization
def categorize_rating(r):
    if r == 0: return 'Unrated'
    if r < 2.5: return 'Poor'
    if r < 3.5: return 'Average'
    if r < 4.5: return 'Good'
    return 'Excellent'

df['Rating Category'] = df['Aggregate rating'].apply(categorize_rating)
category_counts = df['Rating Category'].value_counts()
print("\nRating Category Distribution:")
print(category_counts)

# Save the preprocessed data
output_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df.to_csv(output_path, index=False)
print(f"\nPreprocessed dataset saved to: {output_path}")
