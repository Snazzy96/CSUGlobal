import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Calculate average departure delay by day of the week
departure_delay_by_weekday = data.groupby("DAY_OF_WEEK")["DEP_DELAY_NEW"].mean()

# Create a line plot of departure delay by day of the week
plt.figure(figsize=(8, 6))
departure_delay_by_weekday.plot(kind="line", marker="o")
plt.xlabel("Day of the Week")
plt.ylabel("Average Departure Delay (minutes)")
plt.title("Departure Delay by Day of the Week in January 2023")
plt.xticks(range(1, 8), ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
plt.tight_layout()
plt.show()
