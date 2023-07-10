import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alexh\OneDrive\Desktop\SouthWest Data.csv", dtype={"CANCELLATION REASON": "object"}, low_memory=False)

# Filter the data for January 2023
data["YEAR"] = pd.to_datetime(data["YEAR"], format="%Y")
data = data[data["YEAR"].dt.year == 2023]

# Count the occurrences of cancellation reasons
cancellation_counts = data["CANCELLATION REASON"].value_counts()

# Create a bar plot of cancellation reasons
ax = sns.barplot(x=cancellation_counts.index, y=cancellation_counts.values)
plt.xlabel("Cancellation Reason")
plt.ylabel("Count")
plt.title("Cancellation Reasons")

# Add number labels to the bars
for i, count in enumerate(cancellation_counts.values):
    ax.text(i, count, str(count), ha='center', va='bottom')

plt.show()
