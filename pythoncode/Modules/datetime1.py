from datetime import datetime
import time
import os
# Get the current date and time
current_datetime = datetime.now()
current_date = datetime.now().date()
current_time = datetime.now().time()
print("Current Date and Time:", current_datetime)
print("Current Date:", current_date)
print("Current Time:", current_time)

# start_time = datetime.now()
# os.system("sleep 20")  # Simulate a time-consuming task
# end_time = datetime.now()
# print(start_time, end_time)
# elapsed_time = start_time - end_time
# print("Elapsed Time:", elapsed_time)
cleaned_timeformat = datetime.now().strftime("%d-%m-%Y-%H-%M")

filename = f"backup-{cleaned_timeformat}.txt"
os.system(f"touch {filename}")  # Create a new file with the generated filename



