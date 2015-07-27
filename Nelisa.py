import csv

file = open('Nelisa_Sales_History.csv', 'rU')
csv_file = csv.reader(file)

for row in csv_file:
	print row
