#importing the os module
import os

#to get the current working directory
directory = os.getcwd()

# print('directory', directory)

# f = open('./Day19/example.txt')
# print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

# with open('./Day19/example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# with open('./Day19/example.txt', 'a') as f:
#     f.write('This text has to be appended at the end.')

# with open('./Day19/example.txt', 'w') as f:
#     f.write('This text will be written in a newly created file.')

# import os
# if os.path.exists('./Day19/example.txt'):
#     os.remove('./Day19/example.txt')
# else:
#     print('The file does not exist')
    
# dictionary
person_dct= {
    "name":"Manish",
    "country":"India",
    "city":"Bihar",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Manish', 'country': 'India', 'city': 'Bihar', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Manish",
    "country":"India",
    "city":"Bihar",
    "skills":["JavaScrip", "React","Python"]
}'''


# Changing JSON to Dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.

import json
# JSON
person_json = '''{
    "name":"Manish",
    "country":"India",
    "city":"Bihar",
    "skills":["JavaScrip", "React","Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.
# python dictionary
person = {
    "name":"Manish",
    "country":"India",
    "city":"Bihar",
    "skills":["JavaScrip", "React","Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
# print(type(person_json))
# print(person_json)


# with open('./Day19/example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)
    

import csv
with open('./Day19/example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
    

# import xlrd
# excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

import xml.etree.ElementTree as ET
tree = ET.parse('./Day19/example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)