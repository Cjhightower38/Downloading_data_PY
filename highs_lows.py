# Import csv module
import csv

# Store the download file in a variable, open the variable as f read it
# and use the next() to the first line of the downloaded file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	
# Getting high temperatures. Created empty dictionary to store highs, used
# a for loop to interate through each item and then appeneded each high 
# row 5.Which we were able to see from using the enumerate()
	highs = []
	for row in reader:
		highs.append(row[5])
		
	print(highs)
