import sys
import csv

output = csv.writer(open('quality_controlled_data.csv', 'w'))
headers = ['put', 'all', 'csv', 'headers', 'here']
output.writerow(headers)

for row in csv.DictReader(open(sys.argv[1])) :
    if row["put affability header here"] is "2" :
        r = [row["put"], row["all"], row['csv'], row['headers'], row['here']]
        output.writerow(r)
