# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
other_it_companies = {'Wipro', 'Infosis', 'Mindtree'}
it_companies.update(other_it_companies)
print(it_companies)

it_companies.remove('Amazon')
print(it_companies)

# What is the difference between remove and discard?

join_A_and_B = A.union(B)
print(join_A_and_B)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
B.update(A)
print(A.symmetric_difference(B))
A.clear()
print(A)

st = set(age)
print(len(st) > len(age), len(st) < len(age), len(st), len(age))

str1 = "I am a teacher and I love to inspire and teach people"
lst = str1.split()
print(len(lst))
lst_st = set(lst)
print(lst_st, len(lst_st))