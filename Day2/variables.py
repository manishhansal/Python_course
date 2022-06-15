# Day2 : Python programming

from cmath import pi


first_name = 'Manish'
last_name = 'Kumar'
full_name = first_name + last_name
country = 'India'
city = 'Motihari'
age = 21
year = 2022
is_married = False
is_true = False
is_light = True
hobbies, skills = ['Coding', 'Eating'], ['JS', 'Python', 'HTML']
print(hobbies, skills)
print(full_name)

# Level2

print(type(first_name))
print(len(first_name))
print(len(first_name) < len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)


radius_of_circle = 30
area_of_circle = radius_of_circle * radius_of_circle * pi
circum_of_circle = 2 * pi * radius_of_circle
print(area_of_circle, circum_of_circle)