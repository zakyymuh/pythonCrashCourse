import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[2,3,4],[4,5,6]]
my_new = np.array(my_mat)
print(my_new)

my_arrange = np.arange(0, 12, 2)
print(my_arrange)
my_zero = np.zeros(5)
print(my_zero)
my_zero_mat = np.zeros((2,3))
print(my_zero_mat)
my_linspace = np.linspace(3,10,3)
print(my_linspace)
my_eye = np.eye(5)
print("-- Identity")
print(my_eye)

print("-- Random")
my_random = np.random.rand(3,3)
print(my_random)
# gausian distribution
my_randn = np.random.randn(3)
print(my_randn)
my_rand_int = np.random.randint(0, 10, 2)
print(my_rand_int)

print("-- Arange")
# reshape
my_new_arr = np.arange(25)
my_reshpae = my_new_arr.reshape(5,5)
print(my_reshpae)
print(" --- ")
print(my_randn)
print(my_randn.max())
print(my_randn.min())
print(my_randn.argmax())

print(my_reshpae.shape)
print(my_reshpae.dtype)

from numpy.random import randint
print(randint(2,10))

print("-- Array Indexing on numpy --")
arr = np.arange(0,11)
print(arr)
print(arr[0])
print(arr[0:5])
print(arr[:5])
print(arr[5:])
print("-- Brodcast Value --")
arr[0:5] = 100
print(arr)
newArr = arr[0:7]
print(newArr)
newArr[2:] = np.random.randint(88, 90)
print(newArr)
print(arr)
# phyton not copy but reference
newArr2 = arr.copy()
newArr2[:] = 199
print(newArr2)
print(arr)