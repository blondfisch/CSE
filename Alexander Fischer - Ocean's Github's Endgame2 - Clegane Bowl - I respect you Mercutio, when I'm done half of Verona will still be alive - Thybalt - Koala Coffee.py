import csv

items = {}

averages = {}
with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    high_total = 0
    high_total_key = "wiebe"
    print("Wiebelord......")
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
        units_sold = float(row[8])
        unit_cost = row[10]
        unit_price = row[9]
        try:
            items[item_type] += profit
        except KeyError:
            items[item_type] = profit

        for item in items.items():
            averages[item_type] = profit / units_sold
print("Total Profit")
for key, item in items.items():
    if item > high_total:
        high_total = item
        high_total_key = key
    print(key, end=": ")
    print("${:,}".format(round(item, 2)))
    print()
print("Profit per unit")
print()
for key, item in averages.items():
    print(key, end=": ")
    print("${:,}".format(round(item, 2)))
    print()
print("The Keep the Koala Chlamydiah Community asks that investors specialize in %s because it provides the largest "
      "amount of profit for the community." % high_total_key)
