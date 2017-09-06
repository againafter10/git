'''
#######################
# 1) numpy version
#######################

import numpy as np
print(np.__version__)
'''

'''
############################
# 2) count the number of characters (character frequency) in a string. 
# Input: max has a dogggg
# Output: {'a': 3, ' ': 3, 'd': 1, 'g': 4, 'h': 1, 'm': 1, 'o': 1, 's': 1, 'x': 1}
############################
'''
'''
str=raw_input("String: ")
freq={}
for a in str:
    freq[a]= freq.get(a,0)+1

print freq

'''
'''
############################
# 3) convert array to numpy array
# Input: array
# Output: numpy array
############################
'''
'''
import numpy as np
a = [2,3,4,5]

print np.array(a)
'''
'''
############################
# 4) Create a 3x3 matrix with values ranging from 2 to 10
# Input: range from 2  to 10
# Output: matrix
############################
'''
'''
import numpy as np
mat =  np.arange(2, 11).reshape(3,3)
print(mat)
mat =  np.arange(2,10).reshape(2,4)
print
print(mat)
'''
'''
############################
# 5) to create a null vector of size 10 and update sixth value to 11
# Input: null vector with sixth value 11
# Output:[  0.   0.   0.   0.   0.   0.  11.   0.   0.   0.]
############################
'''
'''
import numpy as np
null_vect= np.zeros(10)
null_vect[6]=11
print null_vect
'''
'''
############################
# 6) Create a array with values ranging from 12 to 38
# Input: range for array
# Output:[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
 37]
############################
'''
'''
import numpy as np
arr = np.arange(12,38)
print arr
'''
'''
############################
# 7) reverse an array
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
 37]
# Output:[37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13
 12]
############################
'''
'''
import numpy as np
arr=np.arange(12,38)
rev_arr=arr[::-1]
print rev_arr
'''
'''
############################
# 8) 2d array with 1 on the border and 0 inside.
# Input: 
# Output:
############################
'''
'''
import numpy as np
#arr=np.zeros((5,5)) --- gives a zero filled matrix
arr = np.ones((6,6))
print arr

print("1 on the border and 0 inside in the array")
arr[1:-1,1:-1] = 0
print(arr)
'''
'''
############################
# 9) Add a border around an existing array
# Input: 
# Output:
############################
'''
'''
import numpy as np
arr = np.ones((3,3))
print("Original array:")
#print(arr)

# arr = np.pad(arr, (1,1), mode='constant', constant_values=0) //this is also correct
arr = np.pad(arr, pad_width=1, mode='constant', constant_values=10)
arr = np.pad(arr,(3,3),'maximum')
print arr

'''

'''
############################
# 10)  checkerboard pattern of 0's and 1's
# Input: 
# Output:
############################
'''
'''
import numpy as np
#x = np.ones((8,8))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)
'''
'''
import numpy as np
arr = np.zeros((5,5),dtype=str)
arr[ ::2,::2]="x"
arr[ 1::2,1::2]="0"
print arr
'''
'''
import numpy as np
arr = np.zeros((6,6),dtype=int)
#arr[ ::2,2::2]=5
#arr[3::1]=5 //lower 3 rows all 5
#arr[3::-1]=5 //upper 3 rows all 5
arr[2::-1,: :2]=5
print arr

'''

'''
############################
# 11)  create empty and full array
# Input: 
# Output:
############################
'''
'''
import numpy as np

x = np.empty((4,4))
print(x)
# Create a full array
y = np.full((4,3),6)
print(y)
y = np.full((4,3),6).reshape(2,6)
print
print(y)
'''


'''
############################
# 11) array manipulation of each element
# Input: 
# Output:
############################
'''
'''
import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)


x = np.array([1,2,3], dtype=np.float32)
#float32 = 4 bytes
#float64 = 8 bytes
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ", x.nbytes)
'''
'''
############################
# 12) array present in another array/find common in each array
# Input: 
# Output:
############################
'''
'''
import numpy as np
array1=np.array([ 32,10 ,20 ,40 ,60] )
array2=[0, 40,32]

print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))

print("Common values between two arrays:")
print(np.intersect1d(array1, array2))
print


print("unique values between two arrays:")
print(np.unique(array1, array2))
print
'''

'''
############################
# 13) repeat an array (tile)
# Input: 
# Output:
############################
'''

import numpy as np
arr=np.array([3,4,5])
print(np.tile(arr,3))

x = np.repeat(3, 4)
print(x)
x = np.array([[1,2],[3,4]])
print x
print
print(np.repeat(x, 2))

x = np.array([1,2,3,4])
print
print(np.repeat(x, 2))