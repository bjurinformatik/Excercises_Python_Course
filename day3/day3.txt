###################
# Day 3 exercises #
###################

#----------------------#
# Class of inheritance #
#----------------------#

#Create file classroom.py

#Terminal commands to get output from Student class
from classroom import Student
me = Student("Josefin", "Bjurling", "Genetics")
me.printNameSubject()

#Terminal commands to get output from Teacher class
from classroom import Teacher
teacher = Teacher("Filipe", "Maia", "Python course")
teacher.printTeacherCourse()

#----------------#
# Numpy exercise #
#----------------#

import numpy as np

# Create a null vector of size 10 but the fifth value which is 1
null_array = np.zeros(10)
null_array[4] = 1

# Create a vector with values ranging from 10 to 49
ranging_values = np.arange(10,50)

# Reverse a vector (first element becomes last)
reversed_values = ranging_values[::-1]

# Create a 3x3 matrix with values ranging from 0 to 8
test_matrix = np.matrix(np.arange(0,9).reshape(3,3))

# Find indices of non-zero elements from [1,2,0,0,4,0]
a = [1,2,0,0,4,0]
np_a = np.array(a)
b = np_a > 0
np_a[b]

# Create a random vector of size 30 and find the mean value
np_random = np.random.random((30))
np.mean(np_random)

# Create a 2d array with 1 on the border and 0 inside
np_2D = np.zeros((4,3))
np_2D[:,[0,2]] = 1
np_2D[[0,3],] = 1

# Create a 8x8 matrix and fill it with a checkerboard pattern
matrix_h = np.matrix(np.zeros((8,8)))
matrix_h[1::2, ::2] = 1
matrix_h[::2, 1::2] = 1

# Create a checkerboard 8x8 matrix using the tile function
array_i = np.array([[0,1], [1,0]])
matrix_i = np.tile(array_i, (4,4))

# Given a 1D array, negate all elements which are between 3 and 8, in place
arr_1D = np.arange(9)
arr_1D[4:8] = np.negative(arr_1D[4:8])

# Create a random vector of size 10 and sort it
Z = np.random.random(10)
np.sort(Z)

# Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)

# How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
Z_float = np.float32(Z)

# How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)

#--------------#
# GPU exercise #
#--------------#

# cupy outperform from size 128x128

# After setting numpy array to float32, cupy still outperform at size 128x128

