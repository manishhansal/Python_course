numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

new_list = [x for x in numbers if x <= 0]
print(new_list)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [
    numbers for row in list_of_lists for numbers in row for numbers in numbers]
# print(flatten_list)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_lst = [list(item) for row in countries for item in row]
# print(flatten_lst)

names = [[('Manish', 'Kumar')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
strig_cont = [(item[0] + " " + item[1]) for row in names for item in row]
print(strig_cont)


countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

gogo_dict = [({'country': item[0], 'city': item[1]})
             for row in countries for item in row]
# print(gogo_dict)
