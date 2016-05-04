import sys
import csv

#output = csv.writer(open('aggregated_data.csv', 'w'))
#headers = ['country', 'aattributes...']
attributes = ['intelligence', 'humor','wealth', 'physicalattractiveness', 'socialstatus', 'health', 'emotionalsensitivity', 'affability']
country_attributes = ['intelligencecountry', 'humorcountry', 'wealthcountry', 'physicalattractivenesscountry', 'socialstatuscountry', 'healthcountry', 'emotionalsensitivitycountry', 'affabilitycountry']
#output.writerow(headers)

usa = {}
usa_general = {}
count_usa = 0

india = {}
india_general = {}
count_india = 0

china = {}
china_general = {}
count_china = 0

nigeria = {}
nigeria_general = {}
count_nigeria = 0

turkey = {}
turkey_general = {}
count_turkey = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["what_country_do_you_live_in"] == "USA" :
        for x in attributes :
            if x in usa :
                usa[x] += int(row[x])
            else :
                usa[x] = int(row[x])
        count_usa += 1
    if row["what_country_do_you_live_in"] == "India" :
        for x in attributes :
            if x in india :
                india[x] += int(row[x])
            else :
                india[x] = int(row[x])
        count_india += 1
    if row["what_country_do_you_live_in"] == "China" :
        for x in attributes :
            if x in china :
                china[x] += int(row[x])
            else :
                china[x] = int(row[x])
        count_china += 1
    if row["what_country_do_you_live_in"] == "Turkey" :
        for x in attributes :
            if x in turkey :
                turkey[x] += int(row[x])
            else :
                turkey[x] = int(row[x])
        count_turkey += 1
    if row["what_country_do_you_live_in"] == "Nigeria" :
        for x in attributes :
            if x in nigeria :
                nigeria[x] += int(row[x])
            else :
                nigeria[x] = int(row[x])
        count_nigeria += 1
        
for x in attributes :
    if len(usa) > 0 :
        usa[x] = usa[x]/float(count_usa)
    if len(india) > 0 :
        india[x] = india[x]/float(count_india)
    if len(china) > 0 :
        china[x] = china[x]/float(count_china)
    if len(turkey) > 0 :
        turkey[x] = turkey[x]/float(count_turkey)
    if len(nigeria) > 0 :    
        nigeria[x] = nigeria[x]/float(count_nigeria)

print "USA Aggregated Scores"
for x in attributes :
    if len(usa) > 0 :
        print x, ": ", usa[x]
print '\n'

print "India Aggregated Scores"
for x in attributes :
    if len(india) > 0 :
        print x, ": ", india[x]
print '\n'

print "China Aggregated Scores"
for x in attributes :
    if len(china) > 0 :
        print x, ": ", china[x]
print '\n'


print "Turkey Aggregated Scores"
for x in attributes :
    if len(turkey) > 0 :
        print x, ": ", turkey[x]
print '\n'


print "Nigeria Aggregated Scores"
for x in attributes :
    if len(nigeria) > 0 :    
        print x, ": ", nigeria[x]
print '\n'

