import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Price Range Analysis ---")

# 1. Most common price range
most_common_price_range = df['Price range'].mode()[0]
count_most_common = df['Price range'].value_counts().max()
print(f"Most common price range: {most_common_price_range} (Count: {count_most_common})")

# 2. Average rating for each price range
avg_rating_per_price = df.groupby('Price range')['Aggregate rating'].mean()
print("\n--- Average Rating per Price Range ---")
print(avg_rating_per_price)

# 3. Identify the color representing the highest average rating among different price ranges
# First, let's find which price range has the highest average rating
highest_rating_price_range = avg_rating_per_price.idxmax()
highest_rating_value = avg_rating_per_price.max()

# Now find the most common 'Rating color' associated with this price range
# (Or just find the average rating associated with each color globally to be sure)
avg_rating_per_color = df.groupby('Rating color')['Aggregate rating'].mean().sort_values(ascending=False)
highest_rating_color = avg_rating_per_color.idxmax()
highest_rating_color_value = avg_rating_per_color.max()

print("\n--- Average Rating per Color ---")
print(avg_rating_per_color)

print(f"\nPrice range with highest average rating: {highest_rating_price_range} ({highest_rating_value:.2f})")
print(f"Color that represents the highest average rating: {highest_rating_color} ({highest_rating_color_value:.2f})")

# Visualizations
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_per_price.index, y=avg_rating_per_price.values, palette='magma')
plt.title('Average Rating by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Aggregate Rating')
plt.savefig('rating_by_price_range.png')

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_per_color.index, y=avg_rating_per_color.values, palette='viridis')
plt.title('Average Rating by Rating Color')
plt.xlabel('Rating Color')
plt.ylabel('Average Aggregate Rating')
plt.savefig('rating_by_color.png')

print("\nVisualizations saved as 'rating_by_price_range.png' and 'rating_by_color.png'")
