humob2024

Probability Matrix Heatmap: Weekday vs Weekend

This script generates heatmaps to visualize user movement data, comparing patterns between weekdays and weekends.

Features

	•	Probability Matrix: Calculates and visualizes movement probability for weekdays and weekends.
	•	Heatmap Visualization: Displays movement differences on a 201x201 grid.
	•	Efficient Processing: Uses multiprocessing for analyzing multiple users quickly.

Usage

	•	Update the csv_file path to your dataset.
	•	Adjust user IDs and time parameters.
	•	Run to generate heatmaps highlighting movement differences.

People Flow Analysis with Stable Matrix

Analyzes people flow data using a “stable matrix” to show how the number of people changes over time, with visualizations for different percentage scenarios.

Features

	•	Data Visualization: Plots showing people flow over time.
	•	Dynamic Analysis: Adjusts analysis based on different percentage inputs.
	•	Matplotlib Integration: Clean visualizations with matplotlib.

Usage

Run best_percentage.py to generate the stable matrix analysis. Adjust percentage inputs as needed.

weekly_location_frequency_matrix.py

Creates a 7x24 matrix to show the most frequent locations for each user, segmented by day of the week and hour of the day.

Usage

Update the csv_file path, adjust user parameters, and run the script to visualize weekly movement patterns.

weekday_prediction.ipynb

Generates a 7x24 matrix to visualize user movement patterns during weekdays, showing the most frequent locations visited.

Usage

Run the notebook to analyze weekday movement data and visualize it using heatmaps.

weekend_prediction.ipynb

Predicts weekend movement patterns by identifying frequently visited locations in the morning, afternoon, and evening. Interpolates missing data for analysis.

Usage

Run the notebook to analyze and fill missing weekend data.
