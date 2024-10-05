import pandas as pd
import numpy as np

# Load the dataset
city_name = 'CityD'
df = pd.read_csv('/Users/yulin/Desktop/人流/data/'+city_name+' Challenge Data.csv')

# Step 1: Group the days into weeks (7-day cycles)
# Day 0-6 is one week, 7-13 is the second, and so on
df['day_of_week'] = (df['d'] % 7)  # 0=Sunday, 6=Saturday

# Step 2: Convert 't' into hours (each timeslot represents a 30-minute interval)
df['hour'] = df['t'] // 2  # Convert 0-47 timeslot into 0-23 hour

# Step 3: Initialize a 7x24 matrix for each user這個矩陣代表一週中每個小時的數據
def create_weekly_hour_matrix(df):
    matrix = np.zeros((7, 24))  # 7 days, 24 hours
    for day in range(7):
        for hour in range(24):
            # Filter data for specific day and hour
            day_hour_data = df[(df['day_of_week'] == day) & (df['hour'] == hour)]
            if not day_hour_data.empty:
                # Find the most frequent location (x, y combination)
                most_frequent_loc = day_hour_data.groupby(['x', 'y']).size().idxmax()
                # Calculate the occurrence ratio of the most frequent location
                top_loc_count = day_hour_data.groupby(['x', 'y']).size().max()
                total_count = len(day_hour_data)
                matrix[day, hour] = top_loc_count / total_count
            else:
                matrix[day, hour] = 0  # No data for this day/hour
    return matrix

# # Step 4: Calculate the matrix for each unique user
# unique_users = df['uid'].unique()
# user_matrices = {} #空字典，用於存儲每個使用者的矩陣

# for uid in unique_users:
#     user_data = df[df['uid'] == uid]
#     user_matrices[uid] = create_weekly_hour_matrix(user_data)


user_data = df[df['uid'] == 1]
user_matrices = create_weekly_hour_matrix(user_data)

# Example: Display the matrix for a specific user (e.g., user 0)
import matplotlib.pyplot as plt
import seaborn as sns

# uid_to_plot = 0  # Change this to view the matrix for different users
# sns.heatmap(user_matrices[uid_to_plot], annot=True, cmap="coolwarm", cbar=True)
# plt.title(f'Weekly Location Frequency Matrix for User {uid_to_plot}')
# plt.xlabel('Hour of Day')
# plt.ylabel('Day of Week (0=Sunday, 6=Saturday)')
# plt.show()

sns.heatmap(user_matrices, annot=True, cmap="Blues", cbar=True)
plt.title(city_name+'Weekly Location Frequency Matrix for User 1')
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week (0=Sunday, 6=Saturday)')
plt.show()
