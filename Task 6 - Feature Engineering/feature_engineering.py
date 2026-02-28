import pandas as pd

# Load the preprocessed dataset
# Note: Has Table Booking and Online Delivery were already encoded to 1/0 in Task 1.
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Feature Engineering ---")

# 1. Extract Lengths
print("Extracted feature: Restaurant Name Length")
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)

print("Extracted feature: Address Length")
df['Address Length'] = df['Address'].apply(len)

# 2. Extract Count of Cuisines
print("Extracted feature: Cuisine Count")
# Handles the 'Unknown' values introduced in preprocessing
df['Cuisine Count'] = df['Cuisines'].apply(lambda x: 0 if x == 'Unknown' else len(x.split(', ')))

# 3. Encoding other categorical variables (if not already done)
# We already did Table Booking and Online Delivery. Let's do 'Is delivering now'
if 'Is delivering now' in df.columns:
    print("Encoded feature: Is delivering now (Yes/No -> 1/0)")
    df['Is delivering now'] = df['Is delivering now'].map({'Yes': 1, 'No': 0})

# 4. Interaction Feature (Example: Cost per Person)
print("Created feature: Cost per Person (Average Cost for two / 2)")
df['Cost per Person'] = df['Average Cost for two'] / 2

# Display the head of the new features
print("\n--- New Features Preview ---")
print(df[['Restaurant Name', 'Restaurant Name Length', 'Address Length', 'Cuisine Count', 'Is delivering now', 'Cost per Person']].head())

# Save the final engineered dataset
output_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Final_Engineered_Dataset.csv"
df.to_csv(output_path, index=False)
print(f"\nEngineered dataset saved to: {output_path}")

# Statistics for new features
print("\n--- Statistical Summary of New Features ---")
print(df[['Restaurant Name Length', 'Address Length', 'Cuisine Count', 'Cost per Person']].describe().transpose()[['mean', 'std', 'min', 'max']])
