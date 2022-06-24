def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(3, 2))

def area_of_circle(radius):
    return 3.14 * radius * radius
print(area_of_circle(5))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(2,3,5))

def convert_celcius_fahrenheit(celcius):
    fahrenheit = (celcius * (9 / 5)) + 32
    return fahrenheit
print(convert_celcius_fahrenheit(32))

def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        return 'Autumn'
    elif month == 'December' or month == 'January' or month == 'February':
        return 'Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        return 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        return 'Summer'
    else:
        return('Enter valid month.')
print(check_season('January'))

def print_list(lts):
    for item in lts:
        print(item)
print_list([1, 2, 3, 4])

def reverse_list(lts):
    count = len(lts) - 1
    reverse = []
    while count >= 0:
        reverse.append(lts[count])
        count = count - 1
    return reverse
print(reverse_list([5, 4, 3, 2, 1]))
print(reverse_list(['A', 'B', 'C', 'D']))

def capitalize_list_items(list):
    cap = []
    for char in list:
        cap.append(char.upper())
    return cap
print(capitalize_list_items(['a', 'b', 'c', 'd']))

def add_item(list, char):
    new_list = []
    for item in list:
        new_list.append(item)
    new_list.append(char)
    return new_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

def remove_item(list, char):
    list.remove(char)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 1:
            sum = sum + i
    return sum
print(sum_of_odds(10))

def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum
print(sum_of_even(10))

def even_and_odds(num):
    even = 0
    odd = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print(f'The number of odds are {odd}.')
    print(f'The number of evens are {even}.')
even_and_odds(100)

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
print(factorial(5))

def is_Prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_Prime(6))

def is_all_unique(list):
    lst = []
    for i in list:
        if not i in lst:
            lst.append(i)
        else:
            return False
    return True

print(is_all_unique([1, 2, 3, 4, 5, 1]))

def is_same_data_types(list):
    i = 0
    while i < len(list) - 1:
        if type(list[i]) != type(list[i+1]):
            return False
        else:
            i = i + 1
    return True
    

print(is_same_data_types([1, 2, 3, 4, "manish"]))

    