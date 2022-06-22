age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

age = input('Enter your age: ')

if int(age) > 21:
    if (int(age) - 21) > 1:
        print(f'You are {int(age) - 21} years older than me.')
    else:
        print(f'You are {int(age) - 21} year older than me.')
elif int(age) < 21:
    if (21 - int(age)) > 1:
        print(f'I am {21 - int(age)} years older than you.')
    else:
        print(f'I am {21 - int(age)} year older than you.')
else:
    print('We both are of same age.')

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

grade = int(input('Enter your score: '))

if grade >= 80 and grade <= 100:
    print('Your grade is A.')
elif grade >= 70 and grade <= 79:
    print('Your grade is B.')
elif grade >= 60 and grade <= 69:
    print('Your grade is C.')
elif grade >= 50 and grade <= 59:
    print('Your grade is D.')
elif grade >= 0 and grade <= 49:
    print('Your grade is F.')
else:
    print('Score should be between 0 to 100.')

month = input('Enter a month: ')

if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter.')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer.')
else:
    print('Enter valid month.')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit name: ')

if not fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print(f'{fruit} already exists in the list.')

person = {
    'first_name' : 'Manish',
    'last_name' : 'Kumar',
    'age' : 21,
    'country' : 'India',
    'is_married' : False,
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {'street' : 'Space Street', 'pincode' : '213211'}
}

first_name = person.get('first_name')
last_name = person.get('last_name')
country = person.get('country')
if (person.get('is_married') == False) and (person.get('country') == 'India'):
    print(f'{first_name} {last_name} lives in {country}. He is not married.')
if 'skills' in person:
    skills_lst = person['skills']
    print(skills_lst[2:3])

if ('JavaScript' in person['skills']) and ('React' in person['skills']):
    print('He is frontend developer.')
elif ('Node' in person['skills']) and ('Python' in person['skills']) and ('MongoDB' in person['skills']):
    print('He is backend developer.')
elif ('Node' in person['skills']) and ('React' in person['skills']) and ('MongoDB' in person['skills']):
    print('He is fullstack developer.')
