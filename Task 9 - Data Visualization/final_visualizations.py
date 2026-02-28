import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the engineered dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Final_Engineered_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Data Visualization Task ---")

# Set aesthetic style
sns.set_theme(style="whitegrid")

# 1. Distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], kde=True, bins=20, color='royalblue')
plt.title('Overall Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.savefig('viz_rating_distribution.png')

# 2. Rating Categories Bar Plot
# Re-categorizing for visualization
def categorize(r):
    if r == 0: return 'Unrated'
    if r < 2.5: return 'Poor'
    if r < 3.5: return 'Average'
    if r < 4.5: return 'Good'
    return 'Excellent'
df['Category'] = df['Aggregate rating'].apply(categorize)
category_order = ['Unrated', 'Poor', 'Average', 'Good', 'Excellent']

plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=df, order=category_order, palette='viridis')
plt.title('Count of Restaurants by Rating Category')
plt.savefig('viz_rating_categories.png')

# 3. Average Rating by City (Top 15)
top_cities = df['City'].value_counts().head(15).index
city_avg_rating = df[df['City'].isin(top_cities)].groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(x='Aggregate rating', y='City', data=city_avg_rating, palette='coolwarm')
plt.title('Average Rating by City (Top 15 by Volume)')
plt.savefig('viz_city_rating_comparison.png')

# 4. Target Variable vs Key Features
# Votes vs Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Aggregate rating', data=df, alpha=0.3, color='darkorange')
plt.title('Relationship: Votes vs Aggregate Rating')
plt.savefig('viz_votes_vs_rating.png')

# Price Range vs Rating (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Aggregate rating', data=df, palette='Set2')
plt.title('Rating Distribution across Price Ranges')
plt.savefig('viz_price_vs_rating_box.png')

# 5. Correlation Heatmap
numerical_cols = ['Aggregate rating', 'Votes', 'Average Cost for two', 'Price range', 
                  'Has Table booking', 'Has Online delivery', 'Restaurant Name Length', 
                  'Cuisine Count', 'Cost per Person']
corr_matrix = df[numerical_cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='RdBu', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap: Features vs Aggregate Rating')
plt.savefig('viz_correlation_heatmap.png')

print("Final Visualizations saved:")
print("- viz_rating_distribution.png")
print("- viz_rating_categories.png")
print("- viz_city_rating_comparison.png")
print("- viz_votes_vs_rating.png")
print("- viz_price_vs_rating_box.png")
print("- viz_correlation_heatmap.png")
