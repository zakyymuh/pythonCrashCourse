import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[1][1])
print(arr[2])
print(arr[2,1])
print(arr[1:,1:])
print(arr[arr % 3 == 0])
new2d_arr = np.arange(50).reshape(10,5)
print(new2d_arr)
print(new2d_arr[new2d_arr % 2 == 0].reshape(5,5))

# Numpy Operations
print("-- Numpy Operations")
arr = np.arange(0, 11)
print(arr)
print(arr + arr)
print(arr - arr)
print(arr * 20)
print(np.sqrt(arr))
print(np.exp(arr))