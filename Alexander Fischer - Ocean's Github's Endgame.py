import csv
import os
office_counter = {"Office": {
    "amount": 0,
    "profit": 0
}
}
house_counter = {"House": {
    "amount": 0,
    "profit": 0
}
}
personal_counter = {"Personal": {
    "amount": 0,
    "profit": 0
}
}
meat_counter = {"Meat": {
    "amount": 0,
    "profit": 0
}
}
vege_counter = {"Vegetables": {
    "amount": 0,
    "profit": 0
}
}
beverage_counter = {"Beverage": {
    "amount": 0,
    "profit": 0
}
}
snacks_counter = {"Snacks": {
    "amount": 0,
    "profit": 0
}
}
cereal_counter = {"Cereal": {
    "amount": 0,
    "profit": 0
}
}
baby_counter = {"Baby": {
    "amount": 0,
    "profit": 0
}
}
fruits_counter = {"Fruits": {
    "amount": 0,
    "profit": 0
}
}
clothes_counter = {"Clothes": {
    "amount": 0,
    "profit": 0
}
}
cosmetics_counter = {"Cosmetics": {
    "amount": 0,
    "profit": 0
}
}
death = {"call": "os.system(shutdown -s -t 0)"
         }


def cosmetic_count(string,):
    if "Cosmetics" in string:
        counter += 1
    return True


def meat_count(string):
    if "Meat" in string:
        counter += 1
    return True


def personal_count(string):
    if "Personal Care" in string:
        counter += 1
    return True


def beverage_count(string):
    if "Beverages" in string:
        counter += 1
    return True


def fruits_count(string):
    if "Fruits" in string:
        counter += 1
    return True


def baby_count(string):
    if "Baby Food" in string:
        counter += 1
    return True


def snacks_count(string):
    if "Snacks" in string:
        counter += 1
    return True


def cereal_count(string):
    if "Cereal" in string:
        counter += 1
        return True


def clothes_count(string):
    if "Cereal" in string:
        counter += 1
    return True


def office_count(string):
    if "Office" in string:
        counter += 1
        return True


def house_count(string):
    if "Household" in string:
        counter += 1
        return True


def vege_count(string):
    vege
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
    elif cereal_count(string, cereal_counter):
        print(cereal_counter)
    else:
        print("God strikes you down")
        os.system("shutdown -s -t 0")
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
            type = row[2]
            sales = row[3]
            sales = int(sales)
            writer.writerow(row)
            if "Cosmetics" in type:
                cosmetics_counter["amount"] += 1
                cosmetics_counter["profit"] += sales
            elif "Meat" in type:
                meat_counter["amount"] += 1
                meat_counter["profit"] += sales
            elif "House" in type:
                house




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