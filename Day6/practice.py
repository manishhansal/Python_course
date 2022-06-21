my_empty_tuple = ()
sisters = ('Reena', 'Meena', 'Sima')
brothers = ('Vikram', 'Ankit', 'Abhishek')
brothers_and_sisters = sisters + brothers
print(brothers_and_sisters)
lts = list(brothers_and_sisters);
lts.insert(0,'Mr. Shah')
lts.insert(1,'Mrs. Devi')
print(lts)

father, mother, *siblings = lts
print(father)
print(mother)
print(siblings)

fruits = ('Mango', 'Apple')
vegetables = ('Tomato', 'Potato', 'Cauliflower')
animal_products = ('Milk', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lts = list(food_stuff_tp)
mid = len(food_stuff_lts)//2
print(food_stuff_lts[mid:mid+1])
print(food_stuff_lts[:3])
print(food_stuff_lts[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
