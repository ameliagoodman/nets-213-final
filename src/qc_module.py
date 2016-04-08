import sys
import csv

output = csv.writer(open('quality_controlled_data.csv', 'w'))
headers = ['country', 'gender', 'age', 'ethnicity', 'intelligence', 'intelligence-country', 'humor', 'humor-country', 'wealth',	'wealth-country',
           'physical-attractiveness', 'physical-attractiveness-country', 'social-status', 'social-status-country', 'sex', 'sex-country',
           'emotional-sensitivity', 'emotional-sensitivity-country', 'affability', 'affability-country', 'south-asian-m', 'south-asian-m-country',
           'east-asian-m', 'east-asian-m-country', 'american-m', 'american-m-country', 'african-m', 'african-m-country', 'middle-eastern-m',
           'middle-eastern-m-country',	'middle-eastern-w', 'middle-eastern-w-country',	'african-w', 'african-w-country', 'american-w',
           'american-w-country', 'east-asian-w', 'east-asian-w-country','south-asian-w', 'south-asian-w-country']
output.writerow(headers)

for row in csv.DictReader(open(sys.argv[1])) :
    if row["affability"] is "2" and row["affability-country"] is 3 :
        r = [row['country'], row['gender'], row['age'], row['ethnicity'], row['intelligence'], row['intelligence-country'], row['humor'], row['humor-country'], row['wealth'],
             row['wealth-country'], row['physical-attractiveness'], row['physical-attractiveness-country'], row['social-status'], row['social-status-country'], row['sex', row['sex-country'],
          row['emotional-sensitivity'], row['emotional-sensitivity-country'], row['affability'], row['affability-country'], row['south-asian-m'], row['south-asian-m-country'],
           row['east-asian-m', row['east-asian-m-country'], row['american-m'], row['american-m-country'], row['african-m'], row['african-m-country'], row['middle-eastern-m'],
           row['middle-eastern-m-country'], row['middle-eastern-w'], row['middle-eastern-w-country'],	row['african-w'], row['african-w-country'], row['american-w'],
           row['american-w-country'], row['east-asian-w'], row['east-asian-w-country'], row['south-asian-w'], row['south-asian-w-country']]
        output.writerow(r)
