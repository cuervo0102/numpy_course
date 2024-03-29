import numpy as np
from script1 import a

# All 0s Matrix
zero_array = np.zeros((2, 3))
print(zero_array)

# All 1s Matrix
one_array = np.ones((2, 3), dtype='int32')
print(one_array)
print(one_array.itemsize)

# Any other number
number_array = np.full((2, 2), 88.5, dtype='float32')
print(number_array)

# Any other number(full_like)
test_array = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])


#Random decimal numbers
print(np.random.rand(5,1000))

#Random Integer values
#2 is the upper bound for the random integers
print(np.random.randint(2, size=(3,3)))
print(np.random.randint(7,8, size=(3,3)))



#Identity 
print(np.identity(6))

#Repeated value
arr = np.array([6,8])
repeated_array = np.repeat(arr, 6, axis=0)
print(repeated_array)

#testing 
f_array = np.ones((5, 5))
z = np.zeros((3, 3))
z[1,1] = 9
f_array[1:4,1:4] = z
print(f_array)
