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

pictures_w = ['middleeasternw', 'middleeasternwcountry', 'africanw', 'africanwcountry', 'americanw', 'americanwcountry', 'eastasianw', 'eastasianwcountry', 'southasianw', 'southasianwcountry']
pictures_m = ['southasianm', 'southasianmcountry', 'eastasianm', 'eastasianmcountry', 'americanm', 'americanmcountry', 'africanm', 'africanmcountry', 'middleeasternm', 'middleeasternmcountry']

all_attributes = attributes + country_attributes + pictures_m + pictures_w

east_asian_count_attract_male = 0
south_asian_count_attract_male = 0
black_count_attract_male = 0
white_count_attract_male = 0
middle_eastern_count_attract_male = 0
latino_hispanic_count_attract_male = 0
east_asian_count_attract_female = 0
south_asian_count_attract_female = 0
black_count_attract_female = 0
white_count_attract_female = 0
middle_eastern_count_attract_female = 0
latino_hispanic_count_attract_female = 0

usa_count_attract_male = 0
egypt_count_attract_male = 0
nigeria_count_attract_male = 0
turkey_count_attract_male = 0
hkg_count_attract_male = 0
india_count_attract_male = 0
usa_count_attract_female = 0
egypt_count_attract_female = 0
nigeria_count_attract_female = 0
turkey_count_attract_female = 0
hkg_count_attract_female = 0
india_count_attract_female = 0

one_count_attract_male = 0
two_count_attract_male = 0
three_count_attract_male = 0
four_count_attract_male = 0
five_count_attract_male = 0
six_count_attract_male = 0
one_count_attract_female = 0
two_count_attract_female = 0
three_count_attract_female = 0
four_count_attract_female = 0
five_count_attract_female = 0
six_count_attract_female = 0

male_count_attract_male = 0
female_count_attract_male = 0
not_listed_count_attract_male = 0
male_count_attract_female = 0
female_count_attract_female = 0
not_listed_count_attract_female = 0
    

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
        if row['orientation'] == "Men" :
            usa_count_attract_male += 1
        else :
            usa_count_attract_female += 1
        count_usa += 1
    if row["what_country_do_you_live_in"] == "India" :
        for x in all_attributes :
            if x in india :
                india[x] += mk_int(row[x])
            else :
                india[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            india_count_attract_male += 1
        else :
            india_count_attract_female += 1
        count_india += 1
    if row["what_country_do_you_live_in"] == "Hong Kong" :
        for x in all_attributes :
            if x in hkg :
                hkg[x] += mk_int(row[x])
            else :
                hkg[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            hkg_count_attract_male += 1
        else :
            hkg_count_attract_female += 1
        count_hkg += 1
    if row["what_country_do_you_live_in"] == "Turkey" :
        for x in all_attributes :
            if x in turkey :
                turkey[x] += mk_int(row[x])
            else :
                turkey[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            turkey_count_attract_male += 1
        else :
            turkey_count_attract_female += 1
        count_turkey += 1
    if row["what_country_do_you_live_in"] == "Nigeria" :
        for x in all_attributes :
            if x in nigeria :
                nigeria[x] += mk_int(row[x])
            else :
                nigeria[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            nigeria_count_attract_male += 1
        else :
            nigeria_count_attract_female += 1
        count_nigeria += 1
    if row["what_country_do_you_live_in"] == "Egypt" :
        for x in all_attributes :
            if x in egypt :
                egypt[x] += mk_int(row[x])
            else :
                egypt[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            egypt_count_attract_male += 1
        else :
            egypt_count_attract_female += 1
        count_egypt += 1

# divide to find averages
for x in all_attributes :
    if len(usa) > 0 :
        if x in pictures_w : 
            if usa_count_attract_female > 0 :
                usa[x] = usa[x]/float(usa_count_attract_female)
        elif x in pictures_m :
            if usa_count_attract_male > 0 :
                usa[x] = usa[x]/float(usa_count_attract_male)
        else :
            usa[x] = usa[x]/float(count_usa)
    if len(india) > 0 :
        if x in pictures_w : 
            if india_count_attract_female > 0 :
                india[x] = india[x]/float(india_count_attract_female)
        elif x in pictures_m :
            if india_count_attract_male > 0 :
                india[x] = india[x]/float(india_count_attract_male)
        else :
            india[x] = india[x]/float(count_india)
    if len(hkg) > 0 :
        if x in pictures_w : 
            if hkg_count_attract_female > 0 :
                hkg[x] = hkg[x]/float(hkg_count_attract_female)
        elif x in pictures_m :
            if hkg_count_attract_male > 0 :
                hkg[x] = hkg[x]/float(hkg_count_attract_male)
        else :
            hkg[x] = hkg[x]/float(count_hkg)
    if len(turkey) > 0 :
        if x in pictures_w : 
            if turkey_count_attract_female > 0 :
                turkey[x] = turkey[x]/float(turkey_count_attract_female)
        elif x in pictures_m :
            if turkey_count_attract_male > 0 :
                turkey[x] = turkey[x]/float(turkey_count_attract_male)
        else :
            turkey[x] = turkey[x]/float(count_turkey)
    if len(nigeria) > 0 :
        if x in pictures_w : 
            if nigeria_count_attract_female > 0 :
                nigeria[x] = nigeria[x]/float(nigeria_count_attract_female)
        elif x in pictures_m :
            if nigeria_count_attract_male > 0 :
                nigeria[x] = nigeria[x]/float(nigeria_count_attract_male)
        else :
            nigeria[x] = nigeria[x]/float(count_nigeria)
    if len(egypt) > 0 :   
        if x in pictures_w : 
            if egypt_count_attract_female > 0 :
                egypt[x] = egypt[x]/float(egypt_count_attract_female)
        elif x in pictures_m :
            if egypt_count_attract_male > 0 :
                egypt[x] = egypt[x]/float(egypt_count_attract_male)
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
        if row['orientation'] == "Men" :
            east_asian_count_attract_male += 1
        else :
            east_asian_count_attract_female += 1
        count_east_asian += 1
    if row["your_ethnicity"] == "South Asian" :
        for x in all_attributes :
            if x in south_asian :
                south_asian[x] += mk_int(row[x])
            else :
                south_asian[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            south_asian_count_attract_male += 1
        else :
            south_asian_count_attract_female += 1
        count_south_asian += 1
    if row["your_ethnicity"] == "Black" :
        for x in all_attributes :
            if x in black :
                black[x] += mk_int(row[x])
            else :
                black[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            black_count_attract_male += 1
        else :
            black_count_attract_female += 1
        count_black += 1
    if row["your_ethnicity"] == "Latino/Hispanic" :
        for x in all_attributes :
            if x in latino_hispanic :
                latino_hispanic[x] += mk_int(row[x])
            else :
                latino_hispanic[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            latino_hispanic_count_attract_male += 1
        else :
            latino_hispanic_count_attract_female += 1
        count_latino_hispanic += 1
    if row["your_ethnicity"] == "Middle Eastern" :
        for x in all_attributes :
            if x in middle_eastern :
                middle_eastern[x] += mk_int(row[x])
            else :
                middle_eastern[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            middle_eastern_count_attract_male += 1
        else :
            middle_eastern_count_attract_female += 1
        count_middle_eastern += 1
    if row["your_ethnicity"] == "White" :
        for x in all_attributes :
            if x in white :
                white[x] += mk_int(row[x])
            else :
                white[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            white_count_attract_male += 1
        else :
            white_count_attract_female += 1
        count_white += 1


for x in all_attributes :
    if len(east_asian) > 0 :
        if x in pictures_w : 
            if east_asian_count_attract_female > 0 :
                east_asian[x] = east_asian[x]/float(east_asian_count_attract_female)
        elif x in pictures_m :
            if east_asian_count_attract_male > 0 :
                east_asian[x] = east_asian[x]/float(east_asian_count_attract_male)
        else :
            east_asian[x] = east_asian[x]/float(count_east_asian)
    if len(south_asian) > 0 :
        if x in pictures_w : 
            if south_asian_count_attract_female > 0 :
                south_asian[x] = south_asian[x]/float(south_asian_count_attract_female)
        elif x in pictures_m :
            if south_asian_count_attract_male > 0 :
                south_asian[x] = south_asian[x]/float(south_asian_count_attract_male)
        else :
            south_asian[x] = south_asian[x]/float(count_south_asian)
    if len(black) > 0 :
        if x in pictures_w : 
            if black_count_attract_female > 0 :
                black[x] = black[x]/float(black_count_attract_female)
        elif x in pictures_m :
            if black_count_attract_male > 0 :
                black[x] = black[x]/float(black_count_attract_male)
        else :
            black[x] = black[x]/float(count_black)
    if len(latino_hispanic) > 0 :
        if x in pictures_w : 
            if latino_hispanic_count_attract_female > 0 :
                latino_hispanic[x] = latino_hispanic[x]/float(latino_hispanic_count_attract_female)
        elif x in pictures_m :
            if latino_hispanic_count_attract_male > 0 :
                latino_hispanic[x] = latino_hispanic[x]/float(latino_hispanic_count_attract_male)
        else :
            latino_hispanic[x] = latino_hispanic[x]/float(count_latino_hispanic)
    if len(middle_eastern) > 0 : 
        if x in pictures_w : 
            if middle_eastern_count_attract_female > 0 :
                middle_eastern[x] = middle_eastern[x]/float(middle_eastern_count_attract_female)
        elif x in pictures_m :
            if middle_eastern_count_attract_male > 0 :
                middle_eastern[x] = middle_eastern[x]/float(middle_eastern_count_attract_male)
        else :
            middle_eastern[x] = middle_eastern[x]/float(count_middle_eastern)
    if len(white) > 0 :   
        if x in pictures_w : 
            if white_count_attract_female > 0 :
                white[x] = white[x]/float(white_count_attract_female)
        elif x in pictures_m :
            if white_count_attract_male > 0 :
                white[x] = white[x]/float(white_count_attract_male)
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
        if row['orientation'] == "Men" :
            one_count_attract_male += 1
        else :
            one_count_attract_female += 1
        count_one += 1
    if row["age"] == "18-24" :
        for x in all_attributes :
            if x in two :
                two[x] += mk_int(row[x])
            else :
                two[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            two_count_attract_male += 1
        else :
            two_count_attract_female += 1
        count_two += 1
    if row["age"] == "25-30" :
        for x in all_attributes :
            if x in three :
                three[x] += mk_int(row[x])
            else :
                three[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            three_count_attract_male += 1
        else :
            three_count_attract_female += 1
        count_three += 1
    if row["age"] == "31-45" :
        for x in all_attributes :
            if x in four :
                four[x] += mk_int(row[x])
            else :
                four[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            four_count_attract_male += 1
        else :
            four_count_attract_female += 1
        count_four += 1
    if row["age"] == "46-60" :
        for x in all_attributes :
            if x in five :
                five[x] += mk_int(row[x])
            else :
                five[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            five_count_attract_male += 1
        else :
            five_count_attract_female += 1
        count_five += 1
    if row["age"] == "61+" :
        for x in all_attributes :
            if x in six :
                six[x] += mk_int(row[x])
            else :
                six[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            six_count_attract_male += 1
        else :
            six_count_attract_female += 1
        count_six += 1

for x in all_attributes :
    if len(one) > 0 :
        if x in pictures_w : 
            if one_count_attract_female > 0 :
                one[x] = one[x]/float(one_count_attract_female)
        elif x in pictures_m :
            if one_count_attract_male > 0 :
                one[x] = one[x]/float(one_count_attract_male)
        else :
            one[x] = one[x]/float(count_one)
    if len(two) > 0 :
        if x in pictures_w : 
            if two_count_attract_female > 0 :
                two[x] = two[x]/float(two_count_attract_female)
        elif x in pictures_m :
            if two_count_attract_male > 0 :
                two[x] = two[x]/float(two_count_attract_male)
        else :
            two[x] = two[x]/float(count_two)
    if len(three) > 0 :
        if x in pictures_w : 
            if three_count_attract_female > 0 :
                three[x] = three[x]/float(three_count_attract_female)
        elif x in pictures_m :
            if three_count_attract_male > 0 :
                three[x] = three[x]/float(three_count_attract_male)
        else :
            three[x] = three[x]/float(count_three)
    if len(four) > 0 :
        if x in pictures_w : 
            if four_count_attract_female > 0 :
                four[x] = four[x]/float(four_count_attract_female)
        elif x in pictures_m :
            if four_count_attract_male > 0 :
                four[x] = four[x]/float(four_count_attract_male)
        else :
            four[x] = four[x]/float(count_four)
    if len(five) > 0 : 
        if x in pictures_w : 
            if five_count_attract_female > 0 :
                five[x] = five[x]/float(five_count_attract_female)
        elif x in pictures_m :
            if five_count_attract_male > 0 :
                five[x] = five[x]/float(five_count_attract_male)
        else :
            five[x] = five[x]/float(count_five)
    if len(six) > 0 :
        if x in pictures_w : 
            if six_count_attract_female > 0 :
                six[x] = six[x]/float(six_count_attract_female)
        elif x in pictures_m :
            if six_count_attract_male > 0 :
                six[x] = six[x]/float(six_count_attract_male)
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
        if row['orientation'] == "Men" :
            male_count_attract_male += 1
        else :
            male_count_attract_female += 1
        count_male += 1
    if row["yourgender"] == "Female" :
        for x in all_attributes :
            if x in female :
                female[x] += mk_int(row[x])
            else :
                female[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            female_count_attract_male += 1
        else :
            female_count_attract_female += 1
        count_female += 1
    if row["yourgender"] == "Not listed" :
        for x in all_attributes :
            if x in not_listed :
                not_listed[x] += mk_int(row[x])
            else :
                not_listed[x] = mk_int(row[x])
        if row['orientation'] == "Men" :
            not_listed_count_attract_male += 1
        else :
            not_listed_count_attract_female += 1
        count_not_listed += 1

for x in all_attributes :
    if len(male) > 0 :
        if x in pictures_w : 
            if male_count_attract_female > 0 :
                male[x] = male[x]/float(male_count_attract_female)
        elif x in pictures_m :
            if male_count_attract_male > 0 :
                male[x] = male[x]/float(male_count_attract_male)
        else :
            male[x] = male[x]/float(count_male)
    if len(female) > 0 :
        if x in pictures_w : 
            if female_count_attract_female > 0 :
                female[x] = female[x]/float(female_count_attract_female)
        elif x in pictures_m :
            if female_count_attract_male > 0 :
                female[x] = female[x]/float(female_count_attract_male)
        else :
            female[x] = female[x]/float(count_female)
    if len(not_listed) > 0 :
        if x in pictures_w : 
            if not_listed_count_attract_female > 0 :
                not_listed[x] = not_listed[x]/float(not_listed_count_attract_female)
        elif x in pictures_m :
            if not_listed_count_attract_male > 0 :
                not_listed[x] = not_listed[x]/float(not_listed_count_attract_male)
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

"""
add = {}
count_total = 0
for row in csv.DictReader(open(sys.argv[1])) :
    for x in attributes :
        if x in add :
            add[x] += int(row[x])
        else :
            add[x] = int(row[x])
    for y in country_attributes :
        if y in add :
            add[y] += int(row[y])
        else :
            add[y] = int(row[y])
    count_total += 1

for x in add :
    add[x] = add[x]/(float(count_total))

for x in add :
    print x, ": ", add[x]
"""







