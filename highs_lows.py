# Import csv,matplotlib, and datetime modules.
from datetime import datetime
from matplotlib import pyplot as plt

import csv

# Store the download file in a variable, open the variable as f read it
# and use the next() to the first line of the downloaded file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	
# Getting high and low temperatures with months. As before created the
# empty dictionary, this time adding an additional dictionary for dates
# iterated through the items, used the variables high/dates to retrive
# the interger format and then appened the high/dates variable to the 
# empty dictionary.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		dates.append(current_date)
		
		high = int(row[5])
		highs.append(high)
		
		low = int(row[6])
		lows.append(low)
		
	print(highs)
	
# Using pyplot to plot the data. By adding alpha we control the 
# transparency(0 will be completelt transparent and 1 will be completely 
# opaque). Adding the fill_between() shades the region between the
# highs and lows.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Formatting plot to include title, x and y lables, and tick parameters.
# The call to fig.autofmt_xdate() drwas the labels diagonally to
# prevent overlapping.
plt.title('Monthly highs and lows temperatures for the year 2018',
    fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

