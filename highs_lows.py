# Import csv module
import csv

# Store the download file in a variable, open the variable as f read it
# and use the next() to the first line of the downloaded file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Removed print(header_row) in exchange of print(ind, col_header)
	# for more detail. enumerate gives the index of each item.
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	
