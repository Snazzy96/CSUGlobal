import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Convert CRS_DEP_TIME to datetime
data["CRS_DEP_TIME"] = pd.to_datetime(data["CRS_DEP_TIME"], format="%I:%M %p", errors="coerce")

# Pivot table to aggregate departure delays by day of week and hour
departure_delays = data.pivot_table(index="DAY_OF_WEEK", columns=data["CRS_DEP_TIME"].dt.hour, values="DEP_DELAY_NEW", aggfunc="mean")

# Create a heatmap of departure delays
sns.heatmap(departure_delays, cmap="coolwarm", annot=True, fmt=".1f", cbar=True)
plt.xlabel("Hour")
plt.ylabel("Day of Week")
plt.title("Departure Delays by Day of Week and Hour")

plt.show()
