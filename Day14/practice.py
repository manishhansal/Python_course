from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Manish', 'Bikram', 'Suresh', 'Madan']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)


countries_list = map(lambda x : x.upper(), countries)
print(list(countries_list))

land_country = filter(lambda x : 'land' in x, countries)
print(list(land_country))

six_letter = filter(lambda x : len(x) == 6, countries)
print(list(six_letter))

six_and_more = filter(lambda x : len(x) >= 6, countries)
print(list(six_and_more))

e_letter = list(filter(lambda x : x[0] == 'E', countries))
print(e_letter)

even_num = reduce(lambda z,a : z + a, list(map(lambda y : y + 1, list(filter(lambda x : x % 2 == 0, numbers)))))
print(even_num)