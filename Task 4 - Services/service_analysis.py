import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Preprocessed_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Table Booking and Online Delivery Analysis ---")

# 1. Percentage of restaurants that offer table booking and online delivery
total_restaurants = len(df)
table_booking_pct = (df['Has Table booking'].sum() / total_restaurants) * 100
online_delivery_pct = (df['Has Online delivery'].sum() / total_restaurants) * 100

print(f"Percentage of restaurants with Table Booking: {table_booking_pct:.2f}%")
print(f"Percentage of restaurants with Online Delivery: {online_delivery_pct:.2f}%")

# 2. Compare average ratings of restaurants with table booking and those without
avg_rating_with_booking = df[df['Has Table booking'] == 1]['Aggregate rating'].mean()
avg_rating_without_booking = df[df['Has Table booking'] == 0]['Aggregate rating'].mean()

print("\n--- Average Ratings Comparison ---")
print(f"Average rating WITH table booking: {avg_rating_with_booking:.2f}")
print(f"Average rating WITHOUT table booking: {avg_rating_without_booking:.2f}")

# Visualize this comparison
plt.figure(figsize=(8, 6))
sns.barplot(x=['With Booking', 'Without Booking'], y=[avg_rating_with_booking, avg_rating_without_booking], palette='coolwarm')
plt.title('Average Rating: Table Booking vs No Table Booking')
plt.ylabel('Average Aggregate Rating')
plt.savefig('rating_vs_booking.png')
print("Saved bar plot as 'rating_vs_booking.png'")

# 3. Analyze availability of online delivery among different price ranges
# Group by price range and calculate the percentage of online delivery
online_delivery_by_price = df.groupby('Price range')['Has Online delivery'].mean() * 100

print("\n--- Online Delivery Availability by Price Range ---")
print(online_delivery_by_price)

# Visualize this availability
plt.figure(figsize=(10, 6))
sns.barplot(x=online_delivery_by_price.index, y=online_delivery_by_price.values, palette='viridis')
plt.title('Percentage of Online Delivery Availability by Price Range')
plt.xlabel('Price Range (1 to 4)')
plt.ylabel('Percentage with Online Delivery (%)')
plt.savefig('online_delivery_by_price.png')
print("Saved bar plot as 'online_delivery_by_price.png'")

# Additional Insight: Correlation between Online Delivery and Rating
avg_rating_with_delivery = df[df['Has Online delivery'] == 1]['Aggregate rating'].mean()
avg_rating_without_delivery = df[df['Has Online delivery'] == 0]['Aggregate rating'].mean()

print("\n--- Average Ratings: Online Delivery vs No Online Delivery ---")
print(f"Average rating WITH online delivery: {avg_rating_with_delivery:.2f}")
print(f"Average rating WITHOUT online delivery: {avg_rating_without_delivery:.2f}")
