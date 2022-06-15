
age = 21
height = 5.3
complex_number = 1 + 1j

# Area of triangle
triangle_base = input('Enter base: ')
triangle_height = input('Enter height: ')
area_of_triangle = 0.5 * int(triangle_base) * int(triangle_height)
print('The area of the triangle is', int(area_of_triangle))

# Perimeter of triangle
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
print('The perimeter of the triangle is', perimeter_of_triangle)

# Area and perimeter of rectangle
length = input('Enter length: ')
width = input('Enter width: ')
area_of_rectangle = int(length) * int(width)
perimeter_of_rectangle = 2 * (int(length) + int(width))
print('Area of rectangle is', area_of_rectangle)
print('Perimeter of rectangle is', perimeter_of_rectangle)

# Area and circumference of a circle
radius = input('Enter radius: ')
area_of_circle = 3.14 * (int(radius) ** 2)
circum_of_circle = 2 * 3.14 * int(radius)
print('Area of a circle is', area_of_circle)
print('Circumference of a circle is', circum_of_circle)


# Calculate the slopes
x_intercept = 5
y_intercept = 2
#slope = 

length_of_python = len('python')
length_of_dragon = len('dragon')
print(not length_of_python == length_of_dragon)

on_in_python = 'on' in 'python'
on_in_dragon = 'on' in 'dragon'
print(on_in_python and on_in_dragon)

print('jargon' in 'I hope this course is not full of jargon')

print(not (on_in_python and on_in_dragon))

string = 'python'
string_length = len(string)
int_to_float = float(string_length)
float_to_string = str(int_to_float)
print(float_to_string)

num = 4
even_or_not = num % 2 == 0
print('Even or not', num, even_or_not)

floor_division = 7 // 3
value = int(2.7)
print(floor_division == value)

print(type('10') == type(10))
print(int('9.8') == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
weekly_earning = int(hours) * int(rate_per_hour)
print('Your weekly earning is', weekly_earning)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = input('Enter number of years you have lived: ')
lived = int(number_of_years) * 365 * 24 * 60 * 60
print('You have lived for', lived, 'seconds')


print('''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
''')