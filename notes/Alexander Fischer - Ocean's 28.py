import csv
print("Welcome to the heist. Remember, there's always someone watching")


def drop_digit(string):
    final_digit = string[15]
    dropped = string[0:15]
    return dropped


def reverse_it(string):
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
    my_list = []
    number_list = list(string)
    for i in range(len(number_list)):
        if i % 2 == 0:
            i = int(number_list[i])
            new_num = i * 2
            if new_num > 9:
                new_num -= 9
            my_list.append(new_num)
    return my_list


print(multiply("603"))


def addition(num):
    numlist = 0
    templist = num
    templist = list(templist)
    for i in range(len(templist)):
        integ = int(templist[i])
        numlist += integ
    return numlist


def modulus(string, last_digit):
    string = string % 10
    if string == last_digit:
        return True
    else:
        return False


def validate_number(start_num):
    if length_check(start_num):
        drop_digit(start_num)
        reverse_it(dropped)
        multiply(reversed_num)
        addition(my_list)
        if modulus(numlist, final_digit):
            return True
        else:
            return False


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("writing the file for wiebelord")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            if validate_number(old_number) is True:
                writer.writerow(row)
