import pandas as pd
data1 = pd.read_csv('data/raw_analyst_ratings.csv')

#Check the structure of the data
data1.head()
len(data1)

#Data Processing
# Convert 'date' from string to datetime object and filter out invalid dates
data1['date'] = pd.to_datetime(data1['date'], errors='coerce')
data1 = data1.dropna(subset=['date'])
 # Verify the number of rows in the dataset after removing entries with invalid dates
len(data1)



# 2. Count the number of articles per publisher
articles_per_publisher = data1['publisher'].value_counts()
print("\nNumber of Articles Per Publisher:")
print(articles_per_publisher)

# 3. Analyze the publication dates to see trends over time
## Remove timezone information from the 'date' column
data1['date'] = data1['date'].dt.tz_localize(None)
print(data1['date'].head())

# Extract day of the week
data1['day_of_week'] = data1['date'].dt.day_name()
print(data1[['date', 'day_of_week']].head())
#This code extracts the month-year period from the datetime column, removing any timezone information
data1['month_year'] = data1['date'].dt.to_period('M')
print(data1[['date', 'month_year']].head())
# Extract day of the week and month-year for analysis
data1['day_of_week'] = data1['date'].dt.day_name()
data1['month_year'] = data1['date'].dt.to_period('M')
print(data1[['date', 'day_of_week', 'month_year']].head())
# This code calculates the total number of articles published on each day of the week.
articles_per_day = data1['day_of_week'].value_counts()
print("\nNumber of Articles Published Per Day of the Week:")
print(articles_per_day)

# Calculate the number of articles published for each month and year
articles_per_month_year = data1['month_year'].value_counts().sort_index()
print("\nNumber of Articles Published Per Month-Year:")
print(articles_per_month_year)

import matplotlib.pyplot as plt

# This code converts the 'month_year' index to a datetime format to enable accurate time series plotting.
articles_per_month_year.index = articles_per_month_year.index.to_timestamp()

# This code generates a time series line plot to visualize the number of articles published each month

plt.figure(figsize=(12, 6))
plt.plot(articles_per_month_year.index, articles_per_month_year.values, marker='o', linestyle='-', color='skyblue')
plt.title('Number of Articles Published Over Time (Month-Year)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Articles', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot 
plt.savefig('articles_published_over_time.png', format='png', dpi=300)  

# Show the plot
plt.show()