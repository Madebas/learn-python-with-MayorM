
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
