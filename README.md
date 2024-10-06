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

This script predicts user commuting patterns by identifying home and work locations, filling missing location data for specific time periods.

## weekend_prediction.ipynb
For regular individuals, we predict their locations by identifying commuting patterns and filling in the most frequent locations for morning, afternoon, and evening.
For irregular individuals, we use an “activity circle” strategy to predict locations based on nearby frequent and close locations within 30 grids of their home.
