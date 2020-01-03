import numpy as np

myList = [1,2,3,4] #python list

np.array(myList) #python list to numpy array

a = np.arange(0,10) #numpy array 0 to 9 step size 1

np.zeros((5,5)) #5x5 array(matrix) of zeros

np.ones((2,4)) #2x4 matrix of ones

np.random.randint(0,100) #return random number bet. 0 and 100

np.random.randint(0,100,(5,5)) #return 5x5 matrix of uniformly distributed random ints bet. 0 and 100

np.linspace(0,10,6) #returns 6 ints linearly spaced between 0 and 10

np.linspace(0,10,101)

np.random.seed(101) #sets a seed to rng
#seed first
np.random.randint(0,100,10) # == [95 11 81 70 63 87 75  9 77 40]

arr = np.random.randint(0,100,10)
arr.max() #max of arr
arr.min() #min of arr
arr.mean() #avg or arr
arr.argmax() #index location of max in arr
arr.argmin() #index location of min in arr
arr.reshape(2,5) #reshape array

mat = np.arange(0,100).reshape(10,10)
mat[5,2]
mat[:,2] #every value in column 2
mat[2,:] #every value in row 2

mat>50 #false when not greater than 50, true greater than 50 boolean array

mat[mat>50] #return array of values in mat greater than 50

