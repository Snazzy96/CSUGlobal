import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Group data by day of the month and count flight occurrences
daily_flight_counts = data["DAY_OF_MONTH"].value_counts().sort_index()

# Create a line plot of daily flight counts
plt.figure(figsize=(12, 6))
daily_flight_counts.plot(kind="line", marker="o")
plt.xlabel("Day of the Month")
plt.ylabel("Flight Count")
plt.title("Daily Flight Counts in January 2023")
plt.xticks(rotation=45)
plt.show()
