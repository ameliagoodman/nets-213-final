import sys
import csv

#output = csv.writer(open('aggregated_data.csv', 'w'))
#headers = ['country', 'aattributes...']
attributes = ['intelligence', 'intelligence-country', 'humor','humor-country', 
'wealth', 'wealth-country', 'physical-attractiveness', 'physical-attractiveness-country', 
'social-status', 'social-status-country', 'health', 'health-country', 'emotional-sensitivity', 
'emotional-sensitivity-country', 'affability', 'affability-country']
#output.writerow(headers)

usa = {}
usa_general = {}
count_usa = 0

india = {}
india_general = {}
count_india = 0

japan = {}
japan_general = {}
count_japan = 0

egypt = {}
egypt_general = {}
count_egypt = 0

germany {}
germany_general = {}
count_germany = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["country"] is "USA" :
        for x in attributes :
            usa[x] += int(row[x])
        count_usa++
    if row["country"] is "IND" :
        for x in attributes :
            india[x] += int(row[x])
        count_india++
    if row["country"] is "JPN" :
        for x in attributes :
            japan[x] += int(row[x])
        count_japan++
    if row["country"] is "GER" :
        for x in attributes :
            ger[x] += int(row[x])
        count_germany++
    if row["country"] is "EGY" :
        for x in attributes :
            egypt[x] += int(row[x])
        count_egypt++
        
for x in attributes :
    usa[x] = usa[x]/float(count_usa)
    india[x] = india[x]/float(count_india)
    japan[x] = japan[x]/float(count_japan)
    germany[x] = germany[x]/float(count_germany)
    egypt[x] = egypt[x]/float(count_egypt)

print "USA Aggregated Scores"
for x in attributes :
    print x, ": ", usa[x]

print "IND Aggregated Scores"
for x in attributes :
    print x, ": ", india[x]

print "JPN Aggregated Scores"
for x in attributes :
    print x, ": ", japan[x]

print "GER Aggregated Scores"
for x in attributes :
    print x, ": ", germany[x]

print "EGY Aggregated Scores"
for x in attributes :
    print x, ": ", egypt[x]
