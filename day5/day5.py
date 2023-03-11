###################
# Day 5 exercises #
###################

#-------#
# Scipy #
#-------#

from scipy import linalg
import numpy as np

# Define a matrix A
 A = np.matrix(np.arange(1,10).reshape(3,3))

# Define a vector b
b = np.arange(1,4)

# Solve the linear system of equations A x = b
x = linalg.solve(A, b)

# Check that your solution is correct by plugging it into the equation
np.dot(A, x) == b
	# Get output True, False, True but comparing the output of np.dot(A,x) and b show that they are the same

# Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)
B = np.matrix(np.random.random(9).reshape(3,3))
x = linalg.solve(A, B)
np.dot(A, x) == b

# Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eg_val, eg_vect = linalg.eig(A)
print(eg_val); print(eg_vect)

# Calculate the inverse, determinant of A
linalg.det(A) #find determinant
np.dot(A, linalg.inv(A)) # calculate and check the inverse and check it

# Calculate the norm of A with different orders
linalg.norm(A, "fro")
linalg.norm(A, "nuc")

#------------------#
# Scipy statistics #
#------------------#

from scipy import stats
import numpy as np

# Test if two sets of (independent) random data comes from the same distribution
var1 = stats.norm.rvs(size=1000)
var2 = stats.norm.rvs(size=1000)

stats.ttest_ind(var1,var2)
