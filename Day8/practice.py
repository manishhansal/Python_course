dog = {}
dog = {
    'name' : 'Liaka',
    'color' : 'Black',
    'breed' : 'German Sepherd',
    'legs' : 4,
    'age' : 10
}

student = {
    'first_name' : 'Manish',
    'last_name' : 'Kumar',
    'gender' : 'Male',
    'age' : 21,
    'marital_status' : False,
    'skills' : ['HTML', 'CSS', 'JavaScript', 'Python', 'React', 'Redux', 'Bootstrap', 'Node'],
    'country' : 'India',
    'city' : 'Motihari',
    'address' : {'village' : 'Rohatas', 'pincode' : '213211'}
}

print(len(student))
print(type(student.get('skills')))

student['skills'].append('Express')
print(student.get('skills'))

keys = student.keys()
values = student.values()
print(keys)
print(values)

print(student.items())

del student['marital_status']
print(student)

del student
print(student)