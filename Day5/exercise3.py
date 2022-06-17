#To add item to the end of an existing list we use the method append().
# syntax
lst = list()
item = 1
lst.append(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

#We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
# syntax
index = 0
lst = ['item1', 'item2']
lst.insert(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

#The remove method removes a specified item from a list
# syntax
lst = ['item1', 'item2']
lst.remove(item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

#The pop() method removes the specified index, (or the last item if index is not specified):
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

#The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

#The clear() method empties the list:
# syntax
lst = ['item1', 'item2']
lst.clear()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []