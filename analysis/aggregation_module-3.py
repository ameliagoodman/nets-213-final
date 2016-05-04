import sys
import csv

def mk_int(s):
    s = s.strip()
    return int(s) if s else 0

attributes = ['intelligence', 'humor','wealth', 'physicalattractiveness', 
'socialstatus', 'health', 'emotionalsensitivity', 'affability']

country_attributes = ['intelligencecountry', 'humorcountry', 'wealthcountry', 
'physicalattractivenesscountry', 'socialstatuscountry', 'healthcountry', 
'emotionalsensitivitycountry', 'affabilitycountry']

pictures_m = ['middleeasternw', 'middleeasternwcountry', 'africanw', 'africanwcountry', 'americanw', 'americanwcountry', 'eastasianw', 'eastasianwcountry', 'southasianw', 'southasianwcountry']
pictures_w = ['southasianm', 'southasianmcountry', 'eastasianm', 'eastasianmcountry', 'americanm', 'americanmcountry', 'africanm', 'africanmcountry', 'middleeasternm', 'middleeasternmcountry']

all_attributes = attributes + country_attributes + pictures_m + pictures_w

count_attract_male = 0
count_attract_female = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row['orientation'] == "Men" :
        count_attract_male += 1
    else :
        count_attract_female += 1


usa = {}
count_usa = 0

india = {}
count_india = 0

hkg = {}
count_hkg = 0

nigeria = {}
count_nigeria = 0

turkey = {}
count_turkey = 0

egypt = {}
count_egypt = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["what_country_do_you_live_in"] == "USA" :
        for x in all_attributes :
            if x in usa :
                usa[x] += mk_int(row[x])
            else :
                usa[x] = mk_int(row[x])
        count_usa += 1
    if row["what_country_do_you_live_in"] == "India" :
        for x in all_attributes :
            if x in india :
                india[x] += mk_int(row[x])
            else :
                india[x] = mk_int(row[x])
        count_india += 1
    if row["what_country_do_you_live_in"] == "Hong Kong" :
        for x in all_attributes :
            if x in hkg :
                hkg[x] += mk_int(row[x])
            else :
                hkg[x] = mk_int(row[x])
        count_hkg += 1
    if row["what_country_do_you_live_in"] == "Turkey" :
        for x in all_attributes :
            if x in turkey :
                turkey[x] += mk_int(row[x])
            else :
                turkey[x] = mk_int(row[x])
        count_turkey += 1
    if row["what_country_do_you_live_in"] == "Nigeria" :
        for x in all_attributes :
            if x in nigeria :
                nigeria[x] += mk_int(row[x])
            else :
                nigeria[x] = mk_int(row[x])
        count_nigeria += 1
    if row["what_country_do_you_live_in"] == "Egypt" :
        for x in all_attributes :
            if x in egypt :
                egypt[x] += mk_int(row[x])
            else :
                egypt[x] = mk_int(row[x])
        count_egypt += 1

for x in all_attributes :
    if len(usa) > 0 :
        if x in pictures_w : 
            usa[x] = usa[x]/float(count_attract_female)
        elif x in pictures_m :
            usa[x] = usa[x]/float(count_attract_male)
        else :
            usa[x] = usa[x]/float(count_usa)
    if len(india) > 0 :
        if x in pictures_w : 
            india[x] = india[x]/float(count_attract_female)
        elif x in pictures_m :
            india[x] = india[x]/float(count_attract_male)
        else :
            india[x] = india[x]/float(count_india)
    if len(hkg) > 0 :
        if x in pictures_w : 
            hkg[x] = hkg[x]/float(count_attract_female)
        elif x in pictures_m :
            hkg[x] = hkg[x]/float(count_attract_male)
        else :
            hkg[x] = hkg[x]/float(count_hkg)
    if len(turkey) > 0 :
        if x in pictures_w : 
            turkey[x] = turkey[x]/float(count_attract_female)
        elif x in pictures_m :
            turkey[x] = turkey[x]/float(count_attract_male)
        else :
            turkey[x] = turkey[x]/float(count_turkey)
    if len(nigeria) > 0 :
        if x in pictures_w : 
            nigeria[x] = nigeria[x]/float(count_attract_female)
        elif x in pictures_m :
            nigeria[x] = nigeria[x]/float(count_attract_male)
        else :
            nigeria[x] = nigeria[x]/float(count_nigeria)
    if len(egypt) > 0 :   
        if x in pictures_w : 
            egypt[x] = egypt[x]/float(count_attract_female)
        elif x in pictures_m :
            egypt[x] = egypt[x]/float(count_attract_male)
        else :
            egypt[x] = egypt[x]/float(count_egypt)

print "ATTRIBUTE SCORES by Country"
print "USA Aggregated Scores"
print "Number of USA = ", count_usa
for x in all_attributes :
    if len(usa) > 0 :
        print x, ": ", usa[x]
print '\n'

print "India Aggregated Scores"
print "Number of India = ", count_india
for x in all_attributes :
    if len(india) > 0 :
        print x, ": ", india[x]
print '\n'

print "Hong Kong Aggregated Scores"
print "Number of Hong Kong = ", count_hkg
for x in all_attributes :
    if len(hkg) > 0 :
        print x, ": ", hkg[x]
print '\n'

print "Turkey Aggregated Scores"
print "Number of Turkey = ", count_turkey
for x in all_attributes :
    if len(turkey) > 0 :
        print x, ": ", turkey[x]
print '\n'

print "Nigeria Aggregated Scores"
print "Number of Nigeria = ", count_nigeria
for x in all_attributes :
    if len(nigeria) > 0 :    
        print x, ": ", nigeria[x]
print '\n'

print "Egypt Aggregated Scores"
print "Number of Egypt = ", count_egypt
for x in all_attributes :
    if len(egypt) > 0 :    
        print x, ": ", egypt[x]
print '\n'

print '\n'



print "***ATTRIBUTE SCORES by ETHNICITY***"


east_asian = {}
count_east_asian = 0

south_asian = {}
count_south_asian = 0

black = {}
count_black = 0

latino_hispanic = {}
count_latino_hispanic = 0

middle_eastern = {}
count_middle_eastern = 0

white = {}
count_white = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["your_ethnicity"] == "East Asian" :
        for x in all_attributes :
            if x in east_asian :
                east_asian[x] += mk_int(row[x])
            else :
                east_asian[x] = mk_int(row[x])
        count_east_asian += 1
    if row["your_ethnicity"] == "South Asian" :
        for x in all_attributes :
            if x in south_asian :
                south_asian[x] += mk_int(row[x])
            else :
                south_asian[x] = mk_int(row[x])
        count_south_asian += 1
    if row["your_ethnicity"] == "Black" :
        for x in all_attributes :
            if x in black :
                black[x] += mk_int(row[x])
            else :
                black[x] = mk_int(row[x])
        count_black += 1
    if row["your_ethnicity"] == "Latino/Hispanic" :
        for x in all_attributes :
            if x in latino_hispanic :
                latino_hispanic[x] += mk_int(row[x])
            else :
                latino_hispanic[x] = mk_int(row[x])
        count_latino_hispanic += 1
    if row["your_ethnicity"] == "Middle Eastern" :
        for x in all_attributes :
            if x in middle_eastern :
                middle_eastern[x] += mk_int(row[x])
            else :
                middle_eastern[x] = mk_int(row[x])
        count_middle_eastern += 1
    if row["your_ethnicity"] == "White" :
        for x in all_attributes :
            if x in white :
                white[x] += mk_int(row[x])
            else :
                white[x] = mk_int(row[x])
        count_white += 1


for x in all_attributes :
    if len(east_asian) > 0 :
        if x in pictures_w : 
            east_asian[x] = east_asian[x]/float(count_attract_female)
        elif x in pictures_m :
            east_asian[x] = east_asian[x]/float(count_attract_male)
        else :
            east_asian[x] = east_asian[x]/float(count_east_asian)
    if len(south_asian) > 0 :
        if x in pictures_w : 
            south_asian[x] = south_asian[x]/float(count_attract_female)
        elif x in pictures_m :
            south_asian[x] = south_asian[x]/float(count_attract_male)
        else :
            south_asian[x] = south_asian[x]/float(count_south_asian)
    if len(black) > 0 :
        if x in pictures_w : 
            black[x] = black[x]/float(count_attract_female)
        elif x in pictures_m :
            black[x] = black[x]/float(count_attract_male)
        else :
            black[x] = black[x]/float(count_black)
    if len(latino_hispanic) > 0 :
        if x in pictures_w : 
            latino_hispanic[x] = latino_hispanic[x]/float(count_attract_female)
        elif x in pictures_m :
            latino_hispanic[x] = latino_hispanic[x]/float(count_attract_male)
        else :
            latino_hispanic[x] = latino_hispanic[x]/float(count_latino_hispanic)
    if len(middle_eastern) > 0 : 
        if x in pictures_w : 
            middle_eastern[x] = middle_eastern[x]/float(count_attract_female)
        elif x in pictures_m :
            middle_eastern[x] = middle_eastern[x]/float(count_attract_male)
        else :
            middle_eastern[x] = middle_eastern[x]/float(count_middle_eastern)
    if len(white) > 0 :   
        if x in pictures_w : 
            white[x] = white[x]/float(count_attract_female)
        elif x in pictures_m :
            white[x] = white[x]/float(count_attract_male)
        else :
            white[x] = white[x]/float(count_white)


print "east_asian Aggregated Scores"
print "Number of East Asian = ", count_east_asian
for x in all_attributes :
    if len(east_asian) > 0 :
        print x, ": ", east_asian[x]
print '\n'

print "south_asian Aggregated Scores"
print "Number of South Asian = ", count_south_asian
for x in all_attributes :
    if len(south_asian) > 0 :
        print x, ": ", south_asian[x]
print '\n'

print "black Aggregated Scores"
print "Number of Black = ", count_black
for x in all_attributes :
    if len(black) > 0 :
        print x, ": ", black[x]
print '\n'

print "latino_hispanic Aggregated Scores"
print "Number of Latino/Hispanic = ", count_latino_hispanic
for x in all_attributes :
    if len(latino_hispanic) > 0 :
        print x, ": ", latino_hispanic[x]
print '\n'

print "middle_eastern Aggregated Scores"
print "Number of Middle Eastern = ", count_middle_eastern
for x in all_attributes :
    if len(middle_eastern) > 0 :    
        print x, ": ", middle_eastern[x]
print '\n'

print "white Aggregated Scores"
print "Number of White = ", count_white
for x in all_attributes :
    if len(white) > 0 :    
        print x, ": ", white[x]
print '\n'

print '\n'



print "***ATTRIBUTE SCORES by Age***"

one = {}
count_one = 0

two = {}
count_two = 0

three = {}
count_three = 0

four = {}
count_four = 0

five = {}
count_five = 0

six = {}
count_six = 0

for row in csv.DictReader(open(sys.argv[1])) :
    if row["age"] == "younger than 18" :
        for x in all_attributes :
            if x in one :
                one[x] += mk_int(row[x])
            else :
                one[x] = mk_int(row[x])
        count_one += 1
    if row["age"] == "18-24" :
        for x in all_attributes :
            if x in two :
                two[x] += mk_int(row[x])
            else :
                two[x] = mk_int(row[x])
        count_two += 1
    if row["age"] == "25-30" :
        for x in all_attributes :
            if x in three :
                three[x] += mk_int(row[x])
            else :
                three[x] = mk_int(row[x])
        count_three += 1
    if row["age"] == "31-45" :
        for x in all_attributes :
            if x in four :
                four[x] += mk_int(row[x])
            else :
                four[x] = mk_int(row[x])
        count_four += 1
    if row["age"] == "46-60" :
        for x in all_attributes :
            if x in five :
                five[x] += mk_int(row[x])
            else :
                five[x] = mk_int(row[x])
        count_five += 1
    if row["age"] == "61+" :
        for x in all_attributes :
            if x in six :
                six[x] += mk_int(row[x])
            else :
                six[x] = mk_int(row[x])
        count_six += 1

for x in all_attributes :
    if len(one) > 0 :
        if x in pictures_w : 
            one[x] = one[x]/float(count_attract_female)
        elif x in pictures_m :
            one[x] = one[x]/float(count_attract_male)
        else :
            one[x] = one[x]/float(count_one)
    if len(two) > 0 :
        if x in pictures_w : 
            two[x] = two[x]/float(count_attract_female)
        elif x in pictures_m :
            two[x] = two[x]/float(count_attract_male)
        else :
            two[x] = two[x]/float(count_two)
    if len(three) > 0 :
        if x in pictures_w : 
            three[x] = three[x]/float(count_attract_female)
        elif x in pictures_m :
            three[x] = three[x]/float(count_attract_male)
        else :
            three[x] = three[x]/float(count_three)
    if len(four) > 0 :
        if x in pictures_w : 
            four[x] = four[x]/float(count_attract_female)
        elif x in pictures_m :
            four[x] = four[x]/float(count_attract_male)
        else :
            four[x] = four[x]/float(count_four)
    if len(five) > 0 : 
        if x in pictures_w : 
            five[x] = five[x]/float(count_attract_female)
        elif x in pictures_m :
            five[x] = five[x]/float(count_attract_male)
        else :
            five[x] = five[x]/float(count_five)
    if len(six) > 0 :
        if x in pictures_w : 
            six[x] = six[x]/float(count_attract_female)
        elif x in pictures_m :
            six[x] = six[x]/float(count_attract_male)
        else :
            six[x] = six[x]/float(count_six)


print "Younger than 18 Aggregated Scores"
print "Number of Younger than 18 = ", count_one
for x in all_attributes :
    if len(one) > 0 :
        print x, ": ", one[x]
print '\n'

print "18-24 Aggregated Scores"
print "Number of 18-24 = ", count_two
for x in all_attributes :
    if len(two) > 0 :
        print x, ": ", two[x]
print '\n'

print "25-30 Aggregated Scores"
print "Number of 25-30 = ", count_three
for x in all_attributes :
    if len(three) > 0 :
        print x, ": ", three[x]
print '\n'

print "31-45 Aggregated Scores"
print "Number of 31-45 = ", count_four
for x in all_attributes :
    if len(four) > 0 :
        print x, ": ", four[x]
print '\n'

print "46-60 Aggregated Scores"
print "Number of 46-60 = ", count_five

for x in all_attributes :
    if len(five) > 0 :    
        print x, ": ", five[x]
print '\n'

print "61+ Aggregated Scores"
print "Number of 61+ = ", count_six
for x in all_attributes :
    if len(six) > 0 :    
        print x, ": ", six[x]
print '\n'

print '\n'




print "***ATTRIBUTE SCORES by Gender***"

male = {}
count_male = 0

female = {}
count_female = 0

not_listed = {}
count_not_listed = 0


for row in csv.DictReader(open(sys.argv[1])) :
    if row["yourgender"] == "Male" :
        for x in all_attributes :
            if x in male :
                male[x] += mk_int(row[x])
            else :
                male[x] = mk_int(row[x])
        count_male += 1
    if row["yourgender"] == "Female" :
        for x in all_attributes :
            if x in female :
                female[x] += mk_int(row[x])
            else :
                female[x] = mk_int(row[x])
        count_female += 1
    if row["yourgender"] == "Not listed" :
        for x in all_attributes :
            if x in not_listed :
                not_listed[x] += mk_int(row[x])
            else :
                not_listed[x] = mk_int(row[x])
        count_not_listed += 1

for x in all_attributes :
    if len(male) > 0 :
        if x in pictures_w : 
            male[x] = male[x]/float(count_attract_female)
        elif x in pictures_m :
            male[x] = male[x]/float(count_attract_male)
        else :
            male[x] = male[x]/float(count_male)
    if len(female) > 0 :
        if x in pictures_w : 
            female[x] = female[x]/float(count_attract_female)
        elif x in pictures_m :
            female[x] = female[x]/float(count_attract_male)
        else :
            female[x] = female[x]/float(count_female)
    if len(not_listed) > 0 :
        if x in pictures_w : 
            not_listed[x] = not_listed[x]/float(count_attract_female)
        elif x in pictures_m :
            not_listed[x] = not_listed[x]/float(count_attract_male)
        else :
            not_listed[x] = not_listed[x]/float(count_not_listed)


print "Male Aggregated Scores"
print "Number of Male = ", count_male
for x in all_attributes :
    if len(male) > 0 :
        print x, ": ", male[x]
print '\n'

print "Female Aggregated Scores"
print "Number of Female = ", count_female
for x in all_attributes :
    if len(female) > 0 :
        print x, ": ", female[x]
print '\n'

print "Not listed Aggregated Scores"
print "Number of Not listed = ", count_not_listed
for x in all_attributes :
    if len(not_listed) > 0 :
        print x, ": ", not_listed[x]
print '\n'
print '\n\n'

print "***ATTRIBUTE SCORES for ALL***"

tracker = {}
count_tracker = 0


for row in csv.DictReader(open(sys.argv[1])) :
    for x in attributes :
        if x in tracker :
            tracker[x] += int(row[x])
        else :
            tracker[x] = int(row[x])
    for y in country_attributes :
        if y in tracker :
            tracker[y] += int(row[y])
        else :
            tracker[y] = int(row[y])
    count_tracker += 1

all_attributes = attributes + country_attributes

for x in all_attributes :
    if len(tracker) > 0 :
        tracker[x] = tracker[x]/float(count_tracker)

print "Total Aggregated Scores"
print "Total of Responses = ", count_tracker
for x in attributes :
    print x, ": ", "%.2f" % tracker[x]
print '\n'






