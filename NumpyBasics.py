#Library for Numpy:
import numpy as np

#Convert List to Numpy ARRAY:
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5],float)

#SHAPE gives dimension length of Numpy array:
my_1D_array = np.array([1, 2, 3, 4, 5])
print (my_1D_array.shape)    #(5,) -> 5 rows and 0 columns

my_2D_array = np.array([[1, 2],[3, 4],[6,5]])
print (my_2D_array.shape )    #(3, 2) -> 3 rows and 2 columns 


#SHAPE Changes the Original Array into desired form:
change_array = np.array([1,2,3,4,5,6])
change_array.shape = (3, 2)


#RESHAPE gives new form of array without changing the original Array:

my_array = np.array([1,2,3,4,5,6])
new_arr=np.reshape(my_array,(3,2))

#TRANSPOSE of Numpy Array:
my_array = np.array([[1,2,3], [4,5,6]])
new_arr=np.transpose(my_array)

#FLATTEN changes the multi-dimensional array into 1D array  
my_array = np.array([[1,2,3], [4,5,6]])
new_arr=my_array.flatten()

#CONCATENATE is used to join 2 or more arrays.
array_1 = np.array([[1,2,3],[0,0,0]])
array_2 = np.array([[0,0,0],[7,8,9]])

new_arr=np.concatenate((array_1, array_2), axis = 1)  # Axis is used to determine along which axis to join. By default is 0 (X-axis) 

#ZEROS creates an array of given dimension with zeros
new_arr=np.zeros((1,2))              #Default type is float
#Output : [[ 0.  0.]] 
new_arr=np.zeros((1,2), dtype = np.int) #Type changes to int
#Output : [[0 0]]

#ONES creates an array of given dimension with ones
new_arr=np.ones((1,2))              #Default type is float
    #Output : [[ 0.  0.]] 
new_arr=np.ones((1,2), dtype = np.int) #Type changes to int
    #Output : [[0 0]]

#IDENTITY creates Identity Matrix of given dimensions
new_arr=np.identity(3) #3 is for  dimension 3 X 3
'''Output
[[ 1.  0.  0.]
[ 0.  1.  0.]
[ 0.  0.  1.]]'''


#EYE to create array with 1's in any diagonal
new_arr=np.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.
'''#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
[ 0.  0.  1.  0.  0.  0.  0.]
[ 0.  0.  0.  1.  0.  0.  0.]
[ 0.  0.  0.  0.  1.  0.  0.]
[ 0.  0.  0.  0.  0.  1.  0.]
[ 0.  0.  0.  0.  0.  0.  1.]
[ 0.  0.  0.  0.  0.  0.  0.]
[ 0.  0.  0.  0.  0.  0.  0.]]'''

new_arr=np.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

#Basic Mathematical Operations on 2 Numpy Arrays:
a = np.array([1,2,3,4], float)
b = np.array([5,6,7,8], float)

print (a + b)                    #[  6.   8.  10.  12.]
print (np.add(a, b))             #[  6.   8.  10.  12.]

print (a - b )                #[-4. -4. -4. -4.]
print (np.subtract(a, b))     #[-4. -4. -4. -4.]

print (a * b)                  #[  5.  12.  21.  32.]
print (np.multiply(a, b)  )    #[  5.  12.  21.  32.]

print (a / b)                  #[ 0.2         0.33333333  0.42857143  0.5       ]
print (np.divide(a, b) )       #[ 0.2         0.33333333  0.42857143  0.5       ]

#Use // for Integer Division

print (a % b)                  #[ 1.  2.  3.  4.]
print (np.mod(a, b))           #[ 1.  2.  3.  4.]

print (a**b )                  #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print (np.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]


#DOT return dot product of 2 Numpy arrays:
A = np.array([ 1, 2 ])
B = np.array([ 3, 4 ])

print (np.dot(A, B))     #Output : 11


#CROSS returns cross product of 2 Numpy arrays:
A = np.array([ 1, 2 ])
B = np.array([ 3, 4 ])

print (np.cross(A, B))  #Output : -2

#FLOOR returns floor of given Numpy array:
my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print (np.floor(my_array))       #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

#CEIL return ceil value of Numpy array:
my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print (np.ceil(my_array) )        #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

#RINT rounds to nearest Integer:
my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print (np.rint(my_array) )         #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]