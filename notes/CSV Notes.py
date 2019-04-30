import csv
import os

def validate(num: str):
    first_num = int(num[0])
    if not length_check(num):
        return False
    if first_num % 3 == 0 and first_num % 2 == 0:
        return True
    return False


def length_check(num: str):
    new_num = len(num)
    if new_num == 16:
        return True
    else:
        print("Not all are 16 numbers.")
        return False


def reverse_it(string):
    return string[::-1]

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

reverse_it("pizaa")
with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        print(reverse_it("Jacajkal;djflaksjfdk"))
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("ok")
def validate_card_number(num: str):
    ????

print(validate_card_number("1234567890123456"))