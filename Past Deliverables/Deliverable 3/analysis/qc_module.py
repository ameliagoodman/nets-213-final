import sys
import csv

output = csv.writer(open('quality_controlled_data.csv', 'w'))
headers = ['country', 'gender', 'age', 'ethnicity', 'orientation', 'intelligence', 'intelligencecountry', 'humor', 'humorcountry', 'wealth', 'wealthcountry', 'physicalattractiveness', 'physicalattractivenesscountry', 'socialstatus', 'socialstatuscountry', 'health', 'healthcountry', 'emotionalsensitivity', 'emotionalsensitivitycountry', 'affability', 'affabilitycountry', 'southasianm', 'southasianmcountry','eastasianm', 'eastasianmcountry', 'americanm', 'americanmcountry', 'africanm', 'africanmcountry', 'middleeasternm','middleeasternmcountry',	'middleeasternw', 'middleeasternwcountry',	'africanw', 'africanwcountry', 'americanw','americanwcountry', 'eastasianw', 'eastasianwcountry','southasianw', 'southasianwcountry']
output.writerow(headers)
count = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["affability"] is "2" and row["affabilitycountry"] is "2" and row['health'] is "3" and row['healthcountry'] is "3" :
		r = [row['what_country_do_you_live_in'], row['yourgender'], row['age'], row['your_ethnicity'], row['orientation'], row['intelligence'], row['intelligencecountry'], row['humor'], row['humorcountry'], row['wealth'], row['wealthcountry'], row['physicalattractiveness'], row['physicalattractivenesscountry'], row['socialstatus'], row['socialstatuscountry'], row['health'], row['healthcountry'],row['emotionalsensitivity'], row['emotionalsensitivitycountry'], row['affability'], row['affabilitycountry'], row['southasianm'], row['southasianmcountry'],row['eastasianm'], row['eastasianmcountry'], row['americanm'], row['americanmcountry'], row['africanm'], row['africanmcountry'], row['middleeasternm'],row['middleeasternmcountry'], row['middleeasternw'], row['middleeasternwcountry'],	row['africanw'], row['africanwcountry'], row['americanw'],row['americanwcountry'], row['eastasianw'], row['eastasianwcountry'], row['southasianw'], row['southasianwcountry']]
		output.writerow(r)
		count += 1
print count