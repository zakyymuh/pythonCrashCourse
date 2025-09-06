import numpy as np
import pandas as pd

my_label = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index = my_label))
print(pd.Series(my_data, my_label))
pd.Series(d)
print(d)

series1 = pd.Series([1,2,3,4],["JPN","IDN","MAY","SGD"])
print(series1)
series2 = pd.Series([1,2,5,7],["BRN","IDN","MAY","SGD"])
print(series2)
print(series1+series2)