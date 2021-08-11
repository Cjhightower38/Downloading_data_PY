# Import csv module
import csv

# Store the download file in a variable, open the variable as f read it
# and use the next() to the first line of the downloaded file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	
