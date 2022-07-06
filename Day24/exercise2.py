# Int,  Float numbers
import numpy as np

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)

numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)

num = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(num)


# numArr = numpy_float_list.astype('int').astype('str')

# 2 Dimension Array
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# 2 Dimension Array
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)


first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)


two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

result = two_dimension_array[::]
print(result)

print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)

# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)

# Numpy Zeroes
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)


# Reshape
# numpy.reshape(), numpy.flatten()
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)

# Horitzontal Stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# Generate a random float  number
random_float = np.random.random()
print(random_float)

# Generate a random float  number
random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10

random_int = np.random.randint(0, 11)
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2, 10, size=4)
print(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2, 10, size=(3, 3))
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)


# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)


four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)


# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)

for l in lst:
    print(l)


# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)


natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
num = np.linspace(1.0, 5.0, num=10)
print(num)

# not to include the last value in the interval
num = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(num)

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

ans = np.logspace(2, 4.0, num=4)
print(ans)