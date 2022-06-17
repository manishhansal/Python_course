
my_list = list()

my_num_list = [1, 2, 3, 4, 5, 6]
print(len(my_num_list))

one,two,three,four,five,six = my_num_list
print(one, four, six)

mixed_data_types = ['Manish', 21, 5.3, False, {"country":"India", "city": "motihari"}]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))

it_companies[0] = 'Wipro'
print(it_companies)

it_companies.append('Infosis')
it_companies.insert(4, 'Siemens')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

string = '# '.join(it_companies)
print(string)

print('Jio' in it_companies)
print('IBM' in it_companies)
print(it_companies.sort())
print(it_companies.reverse())
print(it_companies[0:3])
print(it_companies[-4:-1])
print(it_companies[5])
it_companies.remove(it_companies[0])
it_companies.remove(it_companies[len(it_companies)-1])
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
full_stack = join.copy()
full_stack.insert(5,'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0], ages[-1])


first,second,three,*scandic = ['India', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first)
print(second)
print(three)
print(scandic)

