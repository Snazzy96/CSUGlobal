import tkinter as tk
from datetime import datetime
import pytz
import easygui

def update_times():
    for i, tz in enumerate(selected_timezones):
        now = datetime.now(pytz.timezone(tz))
        time_string = now.strftime('%H:%M:%S')  # Only display the current time
        labels[i][1].config(text=time_string)
    root.after(1000, update_times)  # update every 1000ms (1 second)

if __name__ == "__main__":
    selected_timezones = easygui.multchoicebox(msg="What time zones do you want to display? (choose up to 3)",
                                               choices=pytz.all_timezones)
    if len(selected_timezones) > 3:
        print("Please select no more than 3 timezones.")
    else:
        root = tk.Tk()
        root.title("World Clock")
        root.geometry("600x200")  # You can adjust the window size here

        labels = []
        for i, tz in enumerate(selected_timezones):
            label_tz = tk.Label(root, text=tz, font=("Helvetica", 14))  # Adjust font type and size here
            label_tz.grid(row=0, column=i)  # Position the timezone label at the top

            label_time = tk.Label(root, font=("Helvetica", 14))  
            label_time.grid(row=1, column=i)  # Position the time label below the timezone label

            labels.append((label_tz, label_time))

        update_times()
        root.mainloop()
