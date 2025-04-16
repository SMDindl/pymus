import datetime

# Print from log file, odd is start date, even is end date
# 1108296000
with open("log.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        start_date = datetime.datetime.fromtimestamp(int(lines[i].strip()))
        end_date = datetime.datetime.fromtimestamp(int(lines[i+1].strip()))
        print(f"Start date: {start_date}, End date: {end_date}")

