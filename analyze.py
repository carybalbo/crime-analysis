import csv
from collections import defaultdict

data = []
with open('/data/Crime_records.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

robbery_cases = []
for row in data:
    if row['Crime_Type'] == 'Robbery':
        d = row['Date_Reported']
        y_split = d.split('-')
        y = y_split[0]
        yr = int(y)
        if 2016 <= yr <= 2021:
            robbery_cases.append(row)

ages = []
for row in robbery_cases:
    ag = int(row['Suspect_Age'])
    ages.append(ag)
avg_age = sum(ages) / len(ages)

location_counts = {}
for row in robbery_cases:
    loc_key = row['Location']
    if loc_key in location_counts:
        val = location_counts[loc_key]
        val = val + 1
        location_counts[loc_key]] = val
    else:
        location_counts[loc_key]] = 1

items = list(location_counts.items())
sorted_items = sorted(items, key=lambda pair: pair[1]], reverse=True)):

for pair in sorted_items:
    loc = pair[0]
    cnt = pair[1]
    print('  ' + loc + ': ' + str(cnt) + ' cases')

max_loc = None
max_count = 0
for pair in sorted_items:
    cnt = pair[1]
    if cnt > max_count:
        max_count = cnt
        max_loc = pair[0]

print()
print('Robbery occurred most frequently at: ' + max_loc)
print('Count: ' + str(max_count) + ' cases')