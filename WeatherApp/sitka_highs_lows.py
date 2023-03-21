import csv #from python standard library 
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'WeatherApp/data/sitka_weather_2018_simple.csv'
with open(filename) as f: #'with' statement is used to ensure file is closed properly after it is used. 
    reader = csv.reader(f) #reader object - think of this as the body of the text
    header_row = next(reader) #'next' retrieves the next line in the file - in this case, the headers
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

    for index, column_header in enumerate(header_row): #enumerate returns both the index of each item and the value
        print(index, column_header)
        
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots() 
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #alpha arguement controls colors transparency 

# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #draws dates diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()