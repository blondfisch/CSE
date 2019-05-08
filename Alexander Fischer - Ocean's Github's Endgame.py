import csv
office_counter = 0
house_counter = 0
beverage_counter = 0
cosmetics_counter = 0
meat_counter = 0
personal_counter = 0
fruits_counter = 0
baby_counter = 0
snacks_counter = 0
cereal_counter = 0
vegecounter = 0
clothes_counter = 0


def cosmetic_count(string, counter):
    if "Cosmetics" in string:
        counter += 1
    return True


def meat_count(string, counter):
    if "Meat" in string:
        counter += 1
    return True


def personal_count(string, counter):
    if "Personal Care" in string:
        counter += 1
    return True


def beverage_count(string, counter):
    if "Beverages" in string:
        counter += 1
    return True


def fruits_count(string, counter):
    if "Fruits" in string:
        counter += 1
    return True


def baby_count(string, counter):
    if "Baby Food" in string:
        counter += 1
    return True


def snacks_count(string, counter):
    if "Snacks" in string:
        counter += 1
    return True


def cereal_count(string, counter):
    if "Cereal" in string:
        counter += 1
        return True


def clothes_count(string, counter):
    if "Cereal" in string:
        counter += 1
    return True


def office_count(string, counter):
    if "Office" in string:
        counter += 1
        return True


def house_count(string, counter):
    if "Household" in string:
        counter += 1
        return True


def vege_count(string, counter):
    global vegecounter
    if "Vegetables" in string:
        counter += 1
        return True


def name_counter(string):
    if vege_count(string, vegecounter):
        print(vegecounter)
    elif house_count(string, house_counter):
        print(house_counter)
    elif office_count(string, office_counter):
        print(office_counter)
    elif clothes_count(string, clothes_counter):
        print(clothes_counter)
    cereal_count(string, cereal_counter)
    snacks_count(string, snacks_counter)
    baby_count(string, baby_counter)
    fruits_count(string, fruits_counter)
    beverage_count(string, beverage_counter)
    personal_count(string, personal_counter)
    meat_count(string, meat_counter)
    cosmetic_count(string, cosmetics_counter)


with open("Sales Records.csv", "r") as old_csv:
    with open("SalesFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[2]
            writer.writerow(row)
            print(old_number)
            print(name_counter(old_number))


print("Veges: %d" % vegecounter)
print("Cosmetics: %d" % cosmetics_counter)
print("Meat: %d" % meat_counter)
print("Personal: %d" % personal_counter)
print("Snacks: %d" % snacks_counter)
print("House: %d" % house_counter)
print("Fruits: %d" % fruits_counter)
print("Office: %d" % office_counter)
print("Baby: %d" % baby_counter)
print("Beverage: %d" % beverage_counter)
print("Clothes: %d" % clothes_counter)
print("Cereal: %d" % cereal_counter)