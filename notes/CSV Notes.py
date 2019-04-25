import csv

# with open("Book1.csv", "r") as old_csv:
  #  with open("MyNewFile.csv", "w", newline='') as new_csv:
   #     print("writing the file for wiebelord")
    #    reader = csv.reader(old_csv)
     #   writer = csv.writer(new_csv)
     #   for row in reader:
     #       old_number = int(row[0])
      #      new_number = old_number + 1
       #     row[0] = new_number
        #    writer.writerow(row)
            # print(old_number)

with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num % 2 == 0:
                writer.writerow(row)
print("ok")