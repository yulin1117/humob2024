# humob2024
## Our Results

In our initial tests, we masked data for the first 60 days and tested 1,000 users from CityC. The results were as follows:

	1.	Weekdays: Average GeoBLEU score was 0.33, and DTW was 25.68.
	2.	Weekends: Average GeoBLEU score was 0.21, and DTW was 38.70.

This placed us in 20th place in the competition.

---------------------usage---------------------------
## Probability_Matrix_Heatmap.py

This script generates heatmaps to visualize user movement data, comparing patterns between weekdays and weekends.

## People_flow_stable_matrix.py

This script analyzes people flow data using a “stable matrix” to show how the number of people changes over time, with visualizations for different percentage scenarios.

## weekly_location_frequency_matrix.py

This script creates a 7x24 matrix to show the most frequent locations for each user, segmented by day of the week and hour of the day.

## top2_location_analysis.py

This script analyzes user movement data to identify the proportion of regular users in the dataset. It calculates the top two most visited location ratios for each user and visualizes the results in a scatter plot to highlight consistent movement patterns.

## weekday_prediction.ipynb

Based on the assumption that most individuals have regular weekday patterns, we first identify their “home” location during the hours of 10 PM to 6 AM and fill missing values with this location. Next, we calculate each individual’s commuting distance using Euclidean distance and determine their commuting patterns, including commuting times and key locations (home and work).

1.Identifying commuting periods: Commuting is defined as movement with a distance of ≥ 6 grids (3000 meters).
2.Classifying commuting times: Commutes are split into morning and evening, with noon as the dividing point. We identify the top four commuting periods, limiting each commute to a maximum of two hours.

## weekend_prediction.ipynb
Using the method above to determine whether individuals are regular:

1.For regular individuals, we predict their locations by identifying commuting patterns and filling in the most frequently visited locations for morning, afternoon, and evening.
2.For irregular individuals, we apply an “activity circle” strategy to predict locations based on the most frequent and closest locations within 30 grids of their home.
