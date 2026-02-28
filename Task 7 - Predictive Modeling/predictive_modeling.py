import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load the engineered dataset
file_path = "c:\\Users\\yashw\\Downloads\\Cognifyz\\Final_Engineered_Dataset.csv"
df = pd.read_csv(file_path)

print("--- Predictive Modeling ---")

# 1. Feature Selection
# We exclude features that are directly derived from the target or are purely ID-based/categorical with too many levels
# We'll use numerical and binary features
features = [
    'Country Code', 'Longitude', 'Latitude', 'Has Table booking', 
    'Has Online delivery', 'Is delivering now', 'Price range', 
    'Votes', 'Average Cost for two', 'Restaurant Name Length', 
    'Address Length', 'Cuisine Count'
]
target = 'Aggregate rating'

X = df[features]
y = df[target]

# Check for any remaining NaNs in features (Cuisine Count might have 0s from 'Unknown')
X = X.fillna(0)

# 2. Split into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# 3. Model Training and Comparison
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = []

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train, y_train)
    
    # Prediction
    y_pred = model.predict(X_test)
    
    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        "Model": name,
        "MSE": mse,
        "MAE": mae,
        "R2 Score": r2
    })
    
    print(f"{name} Results: MSE={mse:.4f}, MAE={mae:.4f}, R2={r2:.4f}")

# 4. Compare Performance
results_df = pd.DataFrame(results)
print("\n--- Model Comparison Summary ---")
print(results_df)

# Visualize Comparison
plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y='R2 Score', data=results_df, palette='viridis')
plt.title('Model Comparison: R2 Score')
plt.ylim(0, 1)
plt.savefig('model_comparison_r2.png')

# 5. Feature Importance for the best model (typically Random Forest)
best_model = models["Random Forest"]
feature_importance = pd.Series(best_model.feature_importances_, index=features).sort_values(ascending=False)

print("\n--- Feature Importance (Random Forest) ---")
print(feature_importance)

plt.figure(figsize=(10, 6))
feature_importance.plot(kind='barh', color='teal')
plt.title('Feature Importance for Predicting Aggregate Rating')
plt.xlabel('Importance Score')
plt.savefig('feature_importance.png')

# Save Predictions vs Actual for the best model
y_pred_best = best_model.predict(X_test)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_best, alpha=0.3)
plt.plot([0, 5], [0, 5], '--r')
plt.title('Best Model: Actual vs Predicted Ratings')
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.savefig('best_model_performance.png')

print("\nAll visualizations saved (model_comparison_r2.png, feature_importance.png, best_model_performance.png)")
