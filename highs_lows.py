# Import csv module and matplotlib module
from matplotlib import pyplot as plt

import csv

# Store the download file in a variable, open the variable as f read it
# and use the next() to the first line of the downloaded file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	
# Getting high temperatures. As before created the empty dictionary,
# iterated through the items, used the variable high to retrive the
# interger format and then appened the high variable to the emapty
# dictionary.
	highs = []
	for row in reader:
		high = int(row[5])
		highs.append(high)
		
	print(highs)
	
# Using pyplot to plot the data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Formatting plot to include title, x and y lables, and tick parameters.
plt.title('Daily high temperatures for the year 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

