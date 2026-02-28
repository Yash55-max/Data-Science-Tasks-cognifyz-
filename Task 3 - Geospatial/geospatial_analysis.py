import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load the preprocessed dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Geospatial Analysis ---")

# 1. Visualize locations on a coordinate scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Longitude', y='Latitude', hue='Aggregate rating', palette='viridis', alpha=0.5, s=10)
plt.title('Restaurant Locations colored by Aggregate Rating')
plt.savefig('restaurant_locations.png')
print("Saved coordinate scatter plot as 'restaurant_locations.png'")

# 2. Distribution across Cities/Countries (Top 10)
# This was partially done, but let's visualize it
plt.figure(figsize=(10, 6))
df['City'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Cities by Number of Restaurants')
plt.ylabel('Count')
plt.savefig('city_distribution.png')
print("Saved city distribution plot as 'city_distribution.png'")

# 3. Correlation between location and rating
# Simple correlation matrix for Lat, Long, and Rating
correlation_data = df[['Latitude', 'Longitude', 'Aggregate rating']]
corr_matrix = correlation_data.corr()
print("\nCorrelation Matrix (Location vs Rating):")
print(corr_matrix)

# Average rating by City (Top 10 most frequent cities)
print("\nAverage Rating in Top 10 Cities (by volume):")
top_cities = df['City'].value_counts().head(10).index
avg_rating_city = df[df['City'].isin(top_cities)].groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print(avg_rating_city)

# 4. Create an Interactive Heatmap (Sampled if too large)
# We will create a map centered around the mean lat/long
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=2)

# Add a heat map layer
# We filter out 0.0 ratings to see where the "good" ones are or keep all. Let's keep all.
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(m)

m.save('restaurant_heatmap.html')
print("Saved interactive heatmap as 'restaurant_heatmap.html'")

# Grouped Correlation Insight:
# Let's see if Latitude/Longitude ranges correlate with rating clusters
# Often, specific neighborhoods (Lat/Long clusters) have higher ratings.
# The correlation matrix shows global correlation, but local clusters are more interesting.
