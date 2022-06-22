# syntax
st = {}
# or
st = set()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# We can join two sets using the union() or update() method.

# Union This method returns a new set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Intersection returns a set of items which are in both the sets. See the example

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}