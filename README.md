# humob2024
Probability Matrix Heatmap: Weekday vs Weekend

This script generates probability heatmaps to visualize user movement data, comparing patterns between weekdays and weekends.

Features

	•	Probability Matrix: Calculates and plots movement probability for different time periods (weekdays vs weekends).
	•	Heatmap Visualization: Visualizes the difference in movement patterns using a 201x201 grid.
	•	Efficient Processing: Utilizes multiprocessing for fast analysis of multiple users.

Usage

	•	Update the csv_file path to your dataset.
	•	Adjust user IDs and time parameters in the script.
	•	Run to generate heatmaps that highlight movement differences between weekdays and weekends.
 
People Flow Analysis with Stable Matrix

This repository contains Python code for analyzing and visualizing people flow data using a concept called the “stable matrix.” The primary goal of the project is to understand how the number of people changes across different hours of the day, with dynamic visualizations generated for different percentage scenarios.

Features

	•	Data Visualization: Plots showing the number of people over time (hourly), based on the provided stable matrix data.
	•	Dynamic Analysis: The stable matrix is analyzed for different percentage scenarios, with results dynamically labeled for better understanding.
	•	Matplotlib Integration: Clean visual representations using matplotlib for plotting the data.

Requirements

	•	Python 3.x
	•	Matplotlib

Usage

Run the best_percentage.py to generate the plots for the stable matrix analysis. You can adjust the percentages as needed for different visual outputs.

weekly_location_frequency_matrix.py
Description:

This script analyzes user movement data from a city (e.g., “CityD”) and creates a 7x24 matrix representing the most frequent locations for each user, segmented by day of the week and hour of the day. The resulting matrix visualizes location frequency patterns for a given user over a week, with heatmaps generated to display the data.

weekday_prediction.ipynb
Description:

This script analyzes user movement data from a city (e.g., “CityD”) and creates a 7x24 matrix representing the most frequent locations for each user, segmented by day of the week and hour of the day. The resulting matrix visualizes location frequency patterns for a given user over a week, with heatmaps generated to display the data.

weekend_prediction.ipynb
Description:

This notebook predicts weekend movement patterns by identifying frequently visited locations at different times of the day (morning, afternoon, and evening). It interpolates missing location data and saves the results for further analysis.
