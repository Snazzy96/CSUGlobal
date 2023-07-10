import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Create a violin plot of arrival delays by day of the week
plt.figure(figsize=(8, 6))
sns.violinplot(x="DAY_OF_WEEK", y="ARR_DELAY_NEW", data=data)
plt.xlabel("Day of the Week")
plt.ylabel("Arrival Delay (minutes)")
plt.title("Arrival Delays by Day of Week")
plt.show()
