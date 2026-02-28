import pandas as pd

# Load the preprocessed dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Descriptive Analysis ---")

# 1. Statistical measures for numerical columns
print("\n--- Statistical Measures for Numerical Columns ---")
# Selecting columns that are purely numerical and meaningful for statistics
numerical_cols = ['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes', 'Has Table booking', 'Has Online delivery']
stats = df[numerical_cols].describe().transpose()
# Adding Median separately as describe() doesn't include it by name (though 50% is median)
stats['median'] = df[numerical_cols].median()
print(stats[['mean', 'median', 'std', 'min', 'max']])

# 2. Distribution of Categorical Variables
print("\n--- Distribution of Categorical Variables ---")

def print_top_distribution(col_name, top_n=10):
    print(f"\nTop {top_n} {col_name}:")
    counts = df[col_name].value_counts().head(top_n)
    percentage = (df[col_name].value_counts(normalize=True) * 100).head(top_n)
    dist_df = pd.DataFrame({'Count': counts, 'Percentage (%)': percentage})
    print(dist_df)

print_top_distribution('Country Code')
print_top_distribution('City')

# Focusing on 'Cuisines' - it might contain multiple values separated by commas
print("\n--- Analyzing Cuisines ---")
# Count unique restaurants per cuisine entry (as it is in the column)
print_top_distribution('Cuisines')

# If we want to count individual cuisines (splitting them)
all_cuisines = df['Cuisines'].str.split(', ').explode()
top_individual_cuisines = all_cuisines.value_counts().head(10)
print("\nTop 10 Individual Cuisines (after splitting):")
print(top_individual_cuisines)

# 3. Identify top cuisines and cities with the highest number of restaurants
top_city = df['City'].value_counts().idxmax()
top_city_count = df['City'].value_counts().max()
top_cuisine = all_cuisines.value_counts().idxmax()
top_cuisine_count = all_cuisines.value_counts().max()

print(f"\nSummary:")
print(f"City with the highest number of restaurants: {top_city} ({top_city_count} restaurants)")
print(f"Most frequent cuisine: {top_cuisine} ({top_cuisine_count} occurrences)")
