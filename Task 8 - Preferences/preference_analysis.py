import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Customer Preference Analysis ---")

# Since one restaurant can have multiple cuisines, we split them for a more granular analysis
df_exploded = df.copy()
df_exploded['Cuisines'] = df_exploded['Cuisines'].str.split(', ')
df_exploded = df_exploded.explode('Cuisines')

# 1. Relationship between Cuisine and Rating
print("\n--- Average Rating per Cuisine (Top 10) ---")
cuisine_ratings = df_exploded.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print(cuisine_ratings.head(10))

# 2. Most Popular Cuisines based on Votes
print("\n--- Most Popular Cuisines (Total Votes) ---")
cuisine_popularity = df_exploded.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)
print(cuisine_popularity.head(10))

# 3. Specific Cuisines with High Ratings vs Popularity
# Combine the metrics to see if highly rated ones are also popular
cuisine_stats = df_exploded.groupby('Cuisines').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum',
    'Restaurant ID': 'count'
}).rename(columns={'Restaurant ID': 'Restaurant Count'})

# Filter for cuisines with at least 50 restaurants to avoid small-sample bias
significant_cuisines = cuisine_stats[cuisine_stats['Restaurant Count'] >= 50].sort_values(by='Aggregate rating', ascending=False)
print("\n--- Top Rated Cuisines (with at least 50 restaurants) ---")
print(significant_cuisines.head(10))

# Visualizations
plt.figure(figsize=(12, 6))
cuisine_popularity.head(15).plot(kind='bar', color='coral')
plt.title('Top 15 Most Popular Cuisines by Total Votes')
plt.ylabel('Total Votes')
plt.savefig('cuisine_popularity_votes.png')

plt.figure(figsize=(12, 6))
significant_cuisines['Aggregate rating'].head(15).plot(kind='bar', color='mediumseagreen')
plt.title('Top 15 Highest Rated Cuisines (min 50 restaurants)')
plt.ylabel('Average Rating')
plt.ylim(0, 5)
plt.savefig('top_rated_cuisines.png')

print("\nVisualizations saved: 'cuisine_popularity_votes.png' and 'top_rated_cuisines.png'")
