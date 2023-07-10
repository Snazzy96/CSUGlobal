import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Create a scatter plot of delay duration vs. distance
plt.figure(figsize=(8, 6))
plt.scatter(data["DISTANCE"], data["DEP_DELAY_NEW"], alpha=0.5)
plt.xlabel("Distance")
plt.ylabel("Departure Delay (minutes)")
plt.title("Delay Duration vs. Distance")
plt.show()
