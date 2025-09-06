#### Import NumPy as np
import numpy as np

print(np.zeros(10))
print(np.ones(10))
print(np.ones(10) * 5)
print(np.arange(10,51))
print(np.arange(10,51,2))
print(np.arange(0,9).reshape(3,3))
print(np.eye(3))
# random 0 to 1
print(np.random.rand(1))

print(np.random.randn(5,5))

print(np.linspace(0,1,100).reshape(10,10))
print(np.linspace(0,1,20))

arr = np.arange(1,26).reshape(5,5)
print(arr)
print(arr[2:,1:])
print(arr[3,4])
print(arr[:3,1:2])
print(arr[4:,0:])
print("----")
print(arr[3:,:])
print(np.sum(arr))
print(np.std(arr))
print(sum(arr))