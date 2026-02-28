# Restaurant Data Analysis: Project Classification

This document classifies all scripts, results, and visualizations generated during the project into their respective tasks.

---

## [Task 1 - Data Exploration and Preprocessing](./Task%201%20-%20Preprocessing/)
**Objective**: Explore dataset dimensions, handle missing values, and encode basic binary features.
- **Scripts**: `exploration.py`, `preprocessing.py`
- **Results**: `task1_results.txt`
- **Data**: `Preprocessed_Dataset.csv`
- **Visuals**: `rating_distribution.png`

## [Task 2 - Descriptive Analysis](./Task%202%20-%20Descriptive%20Analysis/)
**Objective**: Calculate statistical measures and analyze distributions of categorical variables (City, Country, Cuisine).
- **Scripts**: `descriptive_analysis.py`
- **Results**: `task2_results.txt`

## [Task 3 - Geospatial Analysis](./Task%203%20-%20Geospatial/)
**Objective**: Visualize restaurant locations on maps and analyze regional rating variances.
- **Scripts**: `geospatial_analysis.py`
- **Results**: `task3_results.txt`
- **Visuals**: `restaurant_locations.png`, `city_distribution.png`, `restaurant_heatmap.html` (Interactive)

## [Task 4 - Table Booking and Online Delivery](./Task%204%20-%20Services/)
**Objective**: Analyze the impact of service offerings (booking/delivery) on aggregate ratings.
- **Scripts**: `service_analysis.py`
- **Results**: `task4_results.txt`
- **Visuals**: `rating_vs_booking.png`, `online_delivery_by_price.png`

## [Task 5 - Price Range Analysis](./Task%205%20-%20Price%20Analysis/)
**Objective**: Investigate the relationship between price tiers and customer ratings.
- **Scripts**: `price_analysis.py`
- **Results**: `task5_results.txt`
- **Visuals**: `rating_by_price_range.png`, `rating_by_color.png`

## [Task 6 - Feature Engineering](./Task%206%20-%20Feature%20Engineering/)
**Objective**: Extract new features like text lengths, cuisine counts, and derive normalized cost metrics.
- **Scripts**: `feature_engineering.py`
- **Results**: `task6_results.txt`
- **Data**: `Final_Engineered_Dataset.csv` (Ready for ML)

## [Task 7 - Predictive Modeling](./Task%207%20-%20Predictive%20Modeling/)
**Objective**: Build and compare regression models (Linear, Decision Tree, Random Forest) to predict ratings.
- **Scripts**: `predictive_modeling.py`
- **Results**: `task7_results.txt`
- **Visuals**: `model_comparison_r2.png`, `feature_importance.png`, `best_model_performance.png`

## [Task 8 - Customer Preference Analysis](./Task%208%20-%20Preferences/)
**Objective**: Identify popular and high-rated cuisines based on customer engagement and volume.
- **Scripts**: `preference_analysis.py`
- **Results**: `task8_results.txt`
- **Visuals**: `cuisine_popularity_votes.png`, `top_rated_cuisines.png`

## [Task 9 - Data Visualization](./Task%209%20-%20Data%20Visualization/)
**Objective**: Create consolidated project visualizations for distribution, regional comparison, and attribute correlation.
- **Scripts**: `final_visualizations.py`
- **Results**: `task9_results.txt`
- **Visuals**: `viz_correlation_heatmap.png`, `viz_price_vs_rating_box.png`, `viz_votes_vs_rating.png`, etc.
