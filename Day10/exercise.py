# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# #prints from 0 to 4

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)


# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


person = {
    'first_name':'Manish',
    'last_name':'Kumar',
    'age':25,
    'country':'India',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')