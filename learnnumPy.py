
        #~~~~~~~Learn NumPy~~~~~~~
#NumPy is a Python library.
#It is used for working with arrays.
#It is a powerful library for numerical computations.
#It is used for scientific computing.
#It is used for data analysis, statistics, machine learning and deep learning.
#It is used for linear algebra fourier transform, and matrices.
##It is used for working with large datasets.
#NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
#NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

           #~~~~~~~Installation of NumPy~~~~~~~
#To install NumPy, you can use pip, which is a package manager for Python.
#You can install NumPy by running the following command in your terminal or command prompt:
#pip install numpy
#If you are using Anaconda, you can install NumPy by running the following command in your terminal or command prompt:
#conda install numpy
#If you are using Jupyter Notebook, you can install NumPy by running the following command in a code cell:
#!pip install numpy
#You can also install NumPy using the Anaconda Navigator, which is a graphical user interface for managing Anaconda packages.
#Once you have installed NumPy, you can import it in your Python code using the following command:
import numpy as np
#You can also import it using the following command:
from numpy import *

#Example:
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
#Output: [1 2 3 4 5]

#You can also create a NumPy array using the following command:
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#Output: [1 2 3 4 5]

             #~~~~~~~Checking NumPy Version~~~~~~~
#You can check the version of NumPy you have installed by running the following command:
print(np.__version__)
#Output: 1.21.0 (or any other version you have installed)
#This will print the version of NumPy you have installed. If you have not installed NumPy, it will raise an ImportError.

     #~~~~~~~NumPy Creating Arrays~~~~~~~
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#An ndarray is a multidimensional array object that can hold elements of the same data type.
#We can create a NumPy ndarray object by using the array() function.
#The array() function takes a list or a tuple as an argument and returns a NumPy ndarray object.

#Example:
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#Output: [1 2 3 4 5]

#We can also create a NumPy ndarray object by using the arange() function.
#The arange() function takes a start value, an end value, and a step value as arguments and returns a NumPy ndarray object.
#Example:
arr = np.arange(1, 10, 2)
print(arr)
#Output: [1 3 5 7 9]
#We can also create a NumPy ndarray object by using the linspace() function.
#The linspace() function takes a start value, an end value, and the number of elements as arguments and returns a NumPy ndarray object.
#Example:
arr = np.linspace(1, 10, 5)
print(arr)
#Output: [ 1.   3.25  5.5  7.75 10. ]

#-----1-D Arrays-----
#A 1-D array is a one-dimensional array that can hold elements of the same data type.
#We can create a 1-D array by using the array() function.
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
#Output: [1 2 3 4 5]

#---2-D Arrays---
#A 2-D array is a two-dimensional array that can hold elements of the same data type.
#We can create a 2-D array by using the array() function.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
#Output:
# [[1 2 3]
# [4 5 6]]

#---3-D Arrays---
#A 3-D array is a three-dimensional array that can hold elements of the same data type.
#We can create a 3-D array by using the array() function.
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)
#Output:
# [[[1 2]
#  [3 4]]
#  [[5 6]
#  [7 8]]]

#-----multi-dimensional arrays-----
#A multi-dimensional array is an array that can hold elements of the same data type in multiple dimensions.
#We can create a multi-dimensional array by using the array() function.
arr_multi = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(arr_multi)
#Output:
# [[[ 1  2]
#  [ 3  4]]
#  [[ 5  6]
#  [ 7  8]]
#  [[ 9 10]
#  [11 12]]]

#-----NumPy Array Indexing
#We can access elements of a NumPy array using indexing.
#Indexing in NumPy arrays is similar to indexing in Python lists.
#We can access elements of a NumPy array using the index of the element.
#Example:
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Output: 1
print(arr[1])  # Output: 2
print(arr[2])  # Output: 3
print(arr[3])  # Output: 4
print(arr[4])  # Output: 5
#We can also access elements of a NumPy array using negative indexing.
print(arr[-1])  # Output: 5
print(arr[-2])  # Output: 4
print(arr[-3])  # Output: 3
print(arr[-4])  # Output: 2
print(arr[-5])  # Output: 1
#We can also access elements of a NumPy array using slicing.
print(arr[1:4])  # Output: [2 3 4]
print(arr[:3])   # Output: [1 2 3]
print(arr[2:])   # Output: [3 4 5]
print(arr[-3:-1])  # Output: [3 4]

#Access 2-D Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[0, 0])  # Output: 1
print(arr_2d[0, 1])  # Output: 2
print(arr_2d[0, 2])  # Output: 3
print(arr_2d[1, 0])  # Output: 4
print(arr_2d[1, 1])  # Output: 5
print(arr_2d[1, 2])  # Output: 6
print(arr_2d[0])  # Output: [1 2 3]
print(arr_2d[1])  # Output: [4 5 6]
#We can also access elements of a 2-D array using slicing.
print(arr_2d[0, 1:3])  # Output: [2 3]
print(arr_2d[1, :])  # Output: [4 5 6]
print(arr_2d[:, 1])  # Output: [2 5]
#We can also access elements of a 2-D array using negative indexing.
print(arr_2d[-1, -1])  # Output: 6
print(arr_2d[-1, -2])  # Output: 5
print(arr_2d[-2, -1])  # Output: 3


#Access 3-D Arrays
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d[0, 0, 0])  # Output: 1
print(arr_3d[0, 0, 1])  # Output: 2
print(arr_3d[0, 1, 0])  # Output: 3
print(arr_3d[0, 1, 1])  # Output: 4
print(arr_3d[1, 0, 0])  # Output: 5
print(arr_3d[1, 0, 1])  # Output: 6
print(arr_3d[1, 1, 0])  # Output: 7
print(arr_3d[1, 1, 1])  # Output: 8
#We can also access elements of a 3-D array using slicing.
print(arr_3d[0, 0, :])  # Output: [1 2]
print(arr_3d[1, 1, :])  # Output: [7 8]
#We can also access elements of a 3-D array using negative indexing.
print(arr_3d[-1, -1, -1])  # Output: 8
print(arr_3d[-1, -1, -2])  # Output: 7
#We can also access elements of a 3-D array using slicing.
print(arr_3d[:, 0, 0])  # Output: [1 5]
print(arr_3d[:, 1, 1])  # Output: [4 8]


   #~~~~~~~NumPy Array Attributes~~~~~~~
#NumPy arrays have several attributes that provide information about the array.
#These attributes can be accessed using the dot notation.
#Example:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)
print(arr.ndim)   # Output: 2
print(arr.size)   # Output: 6
print(arr.dtype)  # Output: int64 (or any other data type)
print(arr.itemsize)  # Output: 8 (or any other size in bytes)
print(arr.nbytes)  # Output: 48 (or any other size in bytes)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
# Output: [2 3 4 5]
print(arr[1:5:2])
# Output: [2 4]
print(arr[::2])
# Output: [1 3 5 7]
print(arr[::-1])
# Output: [7 6 5 4 3 2 1]


 #~~~~~~~Slicing 2-D Arrays~~~~~~~
#We can slice 2-D arrays in a similar way to slicing 1-D arrays.
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0:2, 1:3])
# Output: [[2 3]
#          [5 6]]
print(arr_2d[1:, :2])
# Output: [[4 5]
#          [7 8]]
print(arr_2d[:, 1])
# Output: [2 5 8]
print(arr_2d[1, :])
# Output: [4 5 6]
#We can also slice 2-D arrays using negative indexing.
print(arr_2d[-1, -1])  # Output: 9
print(arr_2d[-1, -2])  # Output: 8
print(arr_2d[-2:, -2:])  # Output: [[5 6]
#          [8 9]]
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
# Output: [3 8]
print(arr[1, 2:4])
# Output: [8 9]
print(arr[0:2, 1:4])
# Output: [[2 3 4]
#          [7 8 9]]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
# Output: [[2 3 4]
#          [7 8 9]]
print(arr[1:, 2:])
# Output: [[ 8  9 10]
#          [11 12 13]]
print(arr[:, 1])
# Output: [ 2  7]
print(arr[1, :])
# Output: [ 6  7  8  9 10]

         #~~~~~~~NumPy Data Types~~~~~~
#Data Types in Python
#Python has several built-in data types, such as int, float, str, list, tuple, set, and dict.
#Data Types in NumPy
#NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

#NumPy Data Types
#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )

#We can check the data type of a NumPy array using the dtype attribute.
#Example:
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # Output: int64 (or any other data type)

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
# Output: int64 (or any other data type)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
# Output: <U6 (or any other data type)

arr = np.array([1.0, 2.0, 3.0, 4.0])
print(arr.dtype)
# Output: float64 (or any other data type)

#Creating Arrays With a Defined Data Type
#We can create a NumPy array with a defined data type using the dtype parameter.
arr = np.array([1, 2, 3, 4], dtype='float64')
print(arr.dtype)
# Output: float64 (or any other data type)
arr = np.array([1, 2, 3, 4], dtype='int32')
print(arr.dtype)
# Output: int32 (or any other data type)
arr = np.array([1, 2, 3, 4], dtype='complex64')
print(arr.dtype)
# Output: complex64 (or any other data type)

#NumPy Array Shape
#The shape of a NumPy array is the number of elements in each dimension.
#We can check the shape of a NumPy array using the shape attribute.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)
#We can also check the shape of a NumPy array using the ndim attribute.
print(arr.ndim)  # Output: 2
#We can also check the size of a NumPy array using the size attribute.
print(arr.size)  # Output: 6

#NumPy Array Reshaping
#We can reshape a NumPy array using the reshape() method.
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, 2)
print(reshaped_arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
#We can also reshape a NumPy array using the resize() method.
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.resize(3, 2)
print(arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
#We can also reshape a NumPy array using the flatten() method.
arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened_arr = arr.flatten()
print(flattened_arr)
# Output: [1 2 3 4 5 6]

#NumPy Array Iterating
#We can iterate over a NumPy array using a for loop.
arr = np.array([1, 2, 3, 4, 5])
for i in arr:
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5

#Iterating 2-D Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
for row in arr_2d:
    for i in row:
        print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
#Iterating 3-D Arrays
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for matrix in arr_3d:
    for row in matrix:
        for i in row:
            print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


#Iterating Arrays Using nditer()
arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in np.nditer(arr):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
#Iterating 2-D Arrays Using nditer()
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
for i in np.nditer(arr_2d):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
#Iterating 3-D Arrays Using nditer()
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr_3d):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

#Iterating With Different Step Size
arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in np.nditer(arr[::2, ::2]):
    print(i)
# Output:
# 1
# 5

#Enumerated Iteration Using ndenumerate()
arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, i in np.ndenumerate(arr):
    print(idx, i)
# Output:
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (1, 0) 4
# (1, 1) 5
# (1, 2) 6
#Enumerated Iteration Using ndenumerate() in 2-D Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
for idx, i in np.ndenumerate(arr_2d):
    print(idx, i)
# Output:
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (1, 0) 4
# (1, 1) 5
# (1, 2) 6

#Joining NumPy Arrays
#We can join two or more NumPy arrays using the concatenate() function.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)
# Output: [1 2 3 4 5 6]
#We can also join two or more NumPy arrays using the stack() function.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.stack((arr1, arr2))
print(arr3)
# Output:
# [[[1 2]
#  [3 4]]
#  [[5 6]
#  [7 8]]]

#NumPy Splitting Array
#We can split a NumPy array into multiple sub-arrays using the split() function.
arr = np.array([1, 2, 3, 4, 5, 6])
arr1, arr2 = np.split(arr, 2)
print(arr1)
# Output: [1 2 3]
print(arr2)
# Output: [4 5 6]

#NumPy Searching Arrays
#We can search for elements in a NumPy array using the where() function.
arr = np.array([1, 2, 3, 4, 5, 6])
indices = np.where(arr == 3)
print(indices)
# Output: (array([2]),)

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
# Output: (array([3, 5, 6]),)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
# Output: (array([1, 3, 5, 7]),)


#Search Sorted
#We can search for elements in a NumPy array using the searchsorted() function.
arr = np.array([1, 2, 3, 4, 5, 6])
index = np.searchsorted(arr, 4)
print(index)
# Output: 3

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
# Output: 1

#NumPy Sorting Arrays
#Sorting Arrays
#Sorting means putting elements in an ordered sequence.
#We can sort a NumPy array using the sort() function.
arr = np.array([3, 1, 2, 5, 4])
arr.sort()
print(arr)
# Output: [1 2 3 4 5]

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
# Output: [0 1 2 3]

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
# Output: ['apple' 'banana' 'cherry']

arr = np.array([True, False, True])

print(np.sort(arr))
# Output: [False  True  True]

#Sorting 2-D Arrays
arr_2d = np.array([[3, 1, 2], [5, 4, 6]])
arr_2d.sort(axis=1)
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

#NumPy Filter Array
#Getting some elements out of an existing array and creating a new array out of them is called filtering.
#We can filter a NumPy array using boolean indexing.
arr = np.array([1, 2, 3, 4, 5, 6])
filter_arr = arr[arr > 3]
print(filter_arr)
# Output: [4 5 6]

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
# Output: [41 43]

#Creating the Filter Array
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
# Output: [False, False, True, True]
# Output: [43 44]

#Example 2
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
# Output: [False False  True  True]
print(newarr)
# Output: [43 44]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Output: [False, True, False, True, False, True, False]
# Output: [2 4 6]

               #~~~~~NumPy Random~~~~~
#NumPy has a module called random that can be used to generate random numbers.

from numpy import random

x = random.randint(100)

print(x)
# Output: A random integer between 0 and 99
x = random.randint(100, size=(5, 5))
print(x)
# Output: A 5x5 array of random integers between 0 and 99

x = random.rand()

print(x)
# Output: A random float between 0 and 1

#Generate Random Array
x = random.rand(5, 5)
print(x)
# Output: A 5x5 array of random floats between 0 and 1
x=random.randint(100, size=(5))

print(x)
# Example: Create a NumPy array with the values [18, 29, 51, 52, 27]
arr = np.array([18, 29, 51, 52, 27])
print(arr)
# Output: [18 29 51 52 27]

#x = random.randint(100, size=(3, 5))

print(x)

[[90 99 11 30 34] 
 [66 40 63 36 37] 
 [63 35 89 51 58]]

x = random.rand(5)

print(x)
[0.9312849 0.2859845 0.7308476 0.5798060 0.2922634]

#Generate Random Number From Array
arr = np.array([1, 2, 3, 4, 5])
x = random.choice(arr)
print(x)
# Output: A random element from the array [1, 2, 3, 4, 5]
x = random.choice(arr, size=(3, 3))
print(x)
# Output: A 3x3 array of random elements from the array [1, 2, 3, 4, 5]

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
# Output: A 3x5 array of random elements from the array [3, 5, 7, 9]

    #~~~~~~Random Data Distribution~~~~~~
#NumPy has a module called random that can be used to generate random numbers from different distributions.
#We can generate random numbers from a uniform distribution using the uniform() function.
x = random.uniform(0, 1, size=(5, 5))
print(x)
# Output: A 5x5 array of random floats from a uniform distribution between 0 and 1
#A random distribution is a set of random numbers that follow a certain probability density function.
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
# Output: A 100-element array of random elements from the array [3, 5, 7, 9] with probabilities [0.1, 0.3, 0.6, 0.0]

#Random Permutations
#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#We can generate a random permutation of a NumPy array using the permutation() function.
arr = np.array([1, 2, 3, 4, 5])
x = random.permutation(arr)
print(x)
# Output: A random permutation of the array [1, 2, 3, 4, 5]
x = random.permutation(arr, 3)
print(x)
# Output: A random permutation of the first 3 elements of the array [1, 2, 3, 4, 5]
#Shuffling Arrays
#We can shuffle the elements of a NumPy array using the shuffle() function.
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
# Output: A shuffled version of the array [1, 2, 3, 4, 5]

#Generating Permutation of Arrays
arr = np.array([1, 2, 3, 4, 5])
x = random.permutation(arr)
print(x)
# Output: A random permutation of the array [1, 2, 3, 4, 5]
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
# Output: A random permutation of the array [1, 2, 3, 4, 5]

          #~~~~~~Seaborn~~~~~~~~~
#Seaborn is a Python data visualization library based on matplotlib.
#It provides a high-level interface for drawing attractive and informative statistical graphics.
#Visualize Distributions With Seaborn
#We can visualize the distribution of a dataset using the distplot() function.
import seaborn as sns
import numpy as np
# Generate random data
data = np.random.randn(1000)
# Create a distribution plot
sns.distplot(data, bins=30, kde=True, color='blue')
# Show the plot
import matplotlib.pyplot as plt
plt.show()
#Visualize Categorical Data With Seaborn
#We can visualize categorical data using the countplot() function.

#Install Seaborn.
#You can install Seaborn using pip:
#pip install seaborn
#Or if you are using Anaconda, you can install Seaborn using conda:
#conda install seaborn
#Import Matplotlib
import matplotlib.pyplot as plt
#Plotting a Displot
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()
#Plotting a Countplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot([0, 1, 2, 3, 4, 5])
plt.show()
#Plotting a Barplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
plt.show()
#Plotting a Boxplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot([0, 1, 2, 3, 4, 5])
plt.show()
#Plotting a Violinplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.violinplot([0, 1, 2, 3, 4, 5])
plt.show()
#Plotting a Heatmap
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = np.random.rand(10, 12)
sns.heatmap(data, annot=True, fmt=".1f", linewidths=.5, cmap="YlGnBu")
plt.show()

#Plotting a Displot Without the Histogram
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5], kde=True, hist=False)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()


#Normal (Gaussian) Distribution
#It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.

#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

#Use the random.normal() method to get a Normal Data Distribution.

#It has three parameters:

#loc - (Mean) where the peak of the bell exists.

#scale - (Standard Deviation) how flat the graph distribution should be.

#size - The shape of the returned array.

Example:
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)
# Output: A 2x3 array of random numbers from a normal distribution with mean 1 and standard deviation 2
#Example 2
x = random.normal(loc=0, scale=1, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from a normal distribution with mean 0 and standard deviation 1

#Visualization of Normal Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()


#Binomial Distribution
#It is a discrete probability distribution that describes the number of successes in 
# a fixed number of independent Bernoulli trials, each with the same probability of success.
#It has three parameters:
#n - The number of trials.
#p - The probability of success in each trial.
#size - The shape of the returned array.

from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
# Output: An array of 10 random numbers from a binomial distribution with 10 trials and probability of success 0.5
#Example 2
x = random.binomial(n=20, p=0.3, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from a binomial distribution with 20 trials and probability of success 0.3

#Visualization of Binomial Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a binomial distribution
data = np.random.binomial(n=10, p=0.5, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.binomial(n=10, p=0.5, size=1000), kind="kde")
plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()


#Poisson Distribution
#It is a discrete probability distribution that describes the number 
# of events occurring in a fixed interval of time or space, given a known average rate of occurrence.
#It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
#It has two parameters:
#lam - The average rate of occurrence (lambda). rate or known number of occurrences e.g. 2 for above problem.
#size - The shape of the returned array.

from numpy import random
x = random.poisson(lam=2, size=10)
print(x)
# Output: An array of 10 random numbers from a Poisson distribution with an average rate of occurrence of 2
#Example 2
x = random.poisson(lam=5, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from a Poisson distribution with an average rate of occurrence of 5

from numpy import random

x = random.poisson(lam=2, size=10)

print(x)
# Output: An array of 10 random numbers from a Poisson distribution with an average rate of occurrence of 2
#Visualization of Poisson Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a Poisson distribution
data = np.random.poisson(lam=2, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam=2, size=1000), kind="kde")
plt.show()

 #Uniform Distribution
#It is a continuous probability distribution where all outcomes are equally likely within a specified range.
#Used to describe probability where every event has equal chances of occuring.
#e.g. Rolling a dice, every number has equal chances of occuring.
#It has three parameters:
#low - The lower bound of the distribution.
#high - The upper bound of the distribution.
#size - The shape of the returned array.

from numpy import random
x = random.uniform(low=0, high=10, size=10)
print(x)
# Output: An array of 10 random numbers from a uniform distribution between 0 and 10
#Example 2
x = random.uniform(low=0, high=1, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from a uniform distribution between 0 and 1


#Difference Between Normal and Binomial Distribution
#Normal Distribution:
# - Continuous distribution.
# - Describes the distribution of a continuous random variable.
# - Characterized by its mean and standard deviation.
# - The probability density function is bell-shaped.
# - Examples: Heights, weights, test scores.
#Binomial Distribution:
# - Discrete distribution.
# - Describes the distribution of a discrete random variable.
# - Characterized by the number of trials and the probability of success.
# - The probability mass function is defined for a fixed number of trials.
# - Examples: Number of heads in coin tosses, number of successes in a series of trials.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()


#Difference Between Normal and Poisson Distribution
#Normal Distribution:
# - Continuous distribution.
# - Describes the distribution of a continuous random variable.
# - Characterized by its mean and standard deviation.
# - The probability density function is bell-shaped.
# - Examples: Heights, weights, test scores.
#Poisson Distribution:
# - Discrete distribution.
# - Describes the distribution of a discrete random variable.
# - Characterized by the average rate of occurrence (lambda).
# - The probability mass function is defined for a fixed interval of time or space.
# - Examples: Number of events in a fixed time period, number of arrivals at a service center.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "poisson": random.poisson(lam=5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#Difference Between Binomial and Poisson Distribution
#Binomial Distribution:
# - Discrete distribution.
# - Describes the distribution of a discrete random variable.
# - Characterized by the number of trials and the probability of success.
# - The probability mass function is defined for a fixed number of trials.
# - Examples: Number of heads in coin tosses, number of successes in a series of trials.
#Poisson Distribution:
# - Discrete distribution.
# - Describes the distribution of a discrete random variable.
# - Characterized by the average rate of occurrence (lambda).
# - The probability mass function is defined for a fixed interval of time or space.
# - Examples: Number of events in a fixed time period, number of arrivals at a service center.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "binomial": random.binomial(n=10, p=0.5, size=1000),
  "poisson": random.poisson(lam=5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#Logistic Distribution
#It is a continuous probability distribution that describes the distribution of a continuous random variable.
#It is similar to the normal distribution but has heavier tails.
#Used extensively in machine learning in logistic regression, neural networks etc
#It has three parameters:
#loc - mean, where the peak is. Default 0.
#scale - standard deviation, how flat the graph distribution should be. Default 1.
#size - The shape of the returned array.

from numpy import random
x = random.logistic(loc=0, scale=1, size=10)
print(x)

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

# Output: A 2x3 array of random numbers from a logistic distribution with mean 1 and standard deviation 2

#Visualization of Logistic Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a logistic distribution
data = np.random.logistic(loc=0, scale=1, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.logistic(loc=0, scale=1, size=1000), kind="kde")
plt.show()

#Difference Between Logistic and Normal Distribution
#Logistic Distribution:
# - Continuous distribution.
# - Describes the distribution of a continuous random variable.
# - Characterized by its mean and standard deviation.
# - The probability density function has heavier tails than the normal distribution.
# - Examples: Logistic regression, neural networks.
#Normal Distribution:
# - Continuous distribution.
# - Describes the distribution of a continuous random variable.
# - Characterized by its mean and standard deviation.
# - The probability density function is bell-shaped.
# - Examples: Heights, weights, test scores.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "logistic": random.logistic(loc=0, scale=1, size=1000),
  "normal": random.normal(loc=0, scale=1, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#Multinomial Distribution
#It is a generalization of the binomial distribution for more than two outcomes.e.g. Blood type of a population, dice roll outcome.
#It describes the distribution of a discrete random variable with multiple categories.
#It has three parameters:
#n - The number of trials.
#pvals - The probabilities of each category.  (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#size - The shape of the returned array.

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)
# Output: An array of counts for each category in a multinomial distribution with 6 trials and equal probabilities for each category

#Example 2
x = random.multinomial(n=10, pvals=[0.2, 0.3, 0.5], size=(3, 4))
print(x)
# Output: A 3x4 array of counts for each category in a multinomial distribution with 10 trials and probabilities [0.2, 0.3, 0.5]

#Visualization of Multinomial Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a multinomial distribution
data = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

#Exponential Distribution
#It is a continuous probability distribution that describes the time between events in a Poisson process.
#It is often used to model the time until an event occurs, such as the time until a customer arrives at a service center.
#It has two parameters:
#scale - The scale parameter (1/lambda), which is the inverse of the average rate of occurrence.
#size - The shape of the returned array.

from numpy import random
x = random.exponential(scale=1, size=10)
print(x)
# Output: An array of 10 random numbers from an exponential distribution with scale 1
#Example 2
x = random.exponential(scale=2, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from an exponential distribution with scale 2

#Visualization of Exponential Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from an exponential distribution
data = np.random.exponential(scale=1, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()

#Relation Between Poisson and Exponential Distribution
#Poisson Distribution:
# - Discrete distribution.
# - Describes the number of events occurring in a fixed interval of time or space.
# - Characterized by the average rate of occurrence (lambda).
# - Examples: Number of events in a fixed time period, number of arrivals at a service center.
#Exponential Distribution:
# - Continuous distribution.
# - Describes the time between events in a Poisson process.
# - Characterized by the scale parameter (1/lambda).
# - Examples: Time until an event occurs, time until a customer arrives at a service center.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "poisson": random.poisson(lam=5, size=1000),
  "exponential": random.exponential(scale=1/5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#Chi Square Distribution
#It is a continuous probability distribution that describes the distribution of the sum of the squares of k independent standard normal random variables.
#It is often used in hypothesis testing, particularly in the context of goodness-of-fit tests and tests of independence.
#It has two parameter:
#df - The degrees of freedom, which is the number of independent standard normal random variables.
#size - The shape of the returned array.

from numpy import random
x = random.chisquare(df=2, size=10)
print(x)
# Output: An array of 10 random numbers from a chi-square distribution with 2 degrees of freedom
#Example 2
x = random.chisquare(df=5, size=(3, 4))
print(x)
# Output: A 3x4 array of random numbers from a chi-square distribution with 5 degrees of freedom

#Visualization of Chi Square Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data from a chi-square distribution
data = np.random.chisquare(df=2, size=1000)
# Create a distribution plot
sns.displot(data, bins=30, kde=True, color='blue')
# Show the plot
plt.show()


#Rayleigh Distribution
#Rayleigh distribution is used in signal processing.
#It has two parameters:

#scale - (standard deviation) decides how flat the distribution will be default 1.0).
#size - The shape of the returned array.
#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:
from numpy import random
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

#Visualization of Rayleigh Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()

#Pareto Distribution
#Pareto Distribution
#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
#It has two parameter:
#a - shape parameter.
#size - The shape of the returned array.
#Draw out a sample for pareto distribution with shape of 2 with size 2x3:

from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)
#Visualization of Pareto Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))
plt.show()

