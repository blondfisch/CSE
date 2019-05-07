import csv


with open("Sales Records.csv", "r") as old_csv:
    with open("SalesFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[2]
            print(old_number)
