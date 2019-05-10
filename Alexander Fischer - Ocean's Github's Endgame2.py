import csv

items = {}

averages = {}
with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    print("Wiebelord......")
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
        units = float(row[8])
        try:
            items[item_type]["profits"] += profit
            items[item_type]["units"] += units
        except KeyError:
            items[item_type] = {}
            averages[item_type] = {}
            items[item_type]["profits"] = profit
            items[item_type]["units"] = units

        for item in items.items():
            averages[item]["average"] = profit / units
for key, item in items.items():
    print(key, end=": ")
    print("${:,}".format(round(item["profits"], 2)))
    print()
print(items)
