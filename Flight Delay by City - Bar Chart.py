import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Calculate average delay by city
avg_delay_by_city = data.groupby("ORIGIN_CITY_NAME")["DEP_DELAY_NEW"].mean().reset_index()

# Sort cities by average delay in ascending order
avg_delay_by_city.sort_values("DEP_DELAY_NEW", inplace=True)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(avg_delay_by_city["ORIGIN_CITY_NAME"], avg_delay_by_city["DEP_DELAY_NEW"])
plt.xlabel("City")
plt.ylabel("Average Departure Delay (minutes)")
plt.title("Average Departure Delay by City")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
