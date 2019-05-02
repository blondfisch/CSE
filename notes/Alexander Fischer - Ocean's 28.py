import csv
print("Welcome to the heist. Remember, there's always someone watching")


def drop_digit(string):
    global final_digit
    final_digit = string[15]
    final_digit = int(final_digit)
    global dropped
    dropped = string[0:15]
    return dropped


def reverse_it(string):
    global reversed_num
    reversed_num = string[::-1]
    return reversed_num


def length_check(num: str):
    new_num = len(num)
    if new_num == 16:
        return True
    else:
        print("Not all are 16 numbers.")
        return False

# for index in range(len(number)):
    # list_num[index] = int(list_num[index])


def multiply(string):
    global fixed_list
    fixed_list = []
    my_list = list(string)
    new_num = []
    temp = -1
    for i in range(len(string)):
        num = string[i]
        if i % 2 == 0:
            place = i
            i = int(string[place])
            num = i * 2
            if num > 9:
                num -= 9
        fixed_list.append(num)
    return fixed_list


def addition(num):
    global numlist
    numlist = 0
    templist = num
    for i in range(len(templist)):
        integ = int(templist[i])
        numlist += integ
    return numlist


def modulus(string):
    global ending
    ending = string % 10
    ending = int(ending)
    return ending


def validate_number(start_num):
    if length_check(start_num):
        drop_digit(start_num)
        reverse_it(dropped)
        multiply(reversed_num)
        addition(fixed_list)
        modulus(numlist)
        if ending == final_digit:
            "its a valid number"
            return True
        else:
            "no"
            return False


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            print(old_number)
            if not validate_number(old_number):
                writer.writerow(row)
print("ok")
