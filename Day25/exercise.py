import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)


dct = {'name':'Manish','country':'India','city':'Motihari'}
s = pd.Series(dct)
print(s)

s = pd.Series(10, index = [1, 2, 3])
print(s)

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

data = [
    ['Manish', 'India', 'Motihari'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)


data = {'Name': ['Manish', 'David', 'John'], 'Country':[
    'India', 'UK', 'Sweden'], 'City': ['Motihari', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)


data = [
    {'Name': 'Manish', 'Country': 'India', 'City': 'Motihari'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# import pandas as pd

# df = pd.read_csv('weight-height.csv')
# print(df)

#print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

#print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

#print(df.shape) # as you can see 10000 rows and three columns

#print(df.columns) #Index(['Gender', 'Height', 'Weight'], dtype='object')

#The describe() method provides a descriptive statistical values of a dataset.
#print(heights.describe()) # give statisical information about height data


data = [
    {"Name": "Manish", "Country":"India","City":"Motihari"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

weights = [74, 78, 69]
df['Weight'] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)


# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()

df['BMI'] = bmi
print(df)

df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

print(df[df['Ages'] > 120])

print(df[df['Ages'] < 120])