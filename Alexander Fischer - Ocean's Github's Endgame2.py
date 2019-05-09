import csv

items = {}


with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
        try:
            items[item_type] += profit
        except KeyError:
            items[item_type] = profit

for key, item in items.items():
    print(key, end=": ")
    print("${:,}".format(round(item, 2)))
