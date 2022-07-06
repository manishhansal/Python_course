import numpy as np
# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)

print('First row: ', np_list[0])
print('Second row: ', np_list[1])


print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])


np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
## min, max, mean, median, sd
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)


print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

rand2 = np.random.randn(2,2)
print(rand2)

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))


# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)
# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23


### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1


new_list = [ x + 2 for x in range(0, 11)]


np_arr = np.array(range(0, 11))
np_arr + 2


temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

# plt.plot(temp,pressure)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()

# To draw the Gaussian normal distribution using numpy. As you can see below, the numpy can generate random numbers. To create random sample, we need the mean(mu), sigma(standard deviation), mumber of data points.

# mu = 28
# sigma = 15
# samples = 100000

# x = np.random.normal(mu, sigma, samples)
# ax = sns.distplot(x);
# ax.set(xlabel="x", ylabel='y')
# plt.show()