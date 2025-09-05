print(1+1)
print(2-1)
print(3*5)
print(1+3*4+3)
print(2 ** 3)
print(1/3)

var = 3
print(var)

x = 2
y = 3
print(x ** y)

x = x+x
print(x)

name_of_common_var_on_python = 100
print(name_of_common_var_on_python)
# this one is comment

name = 'miy'
age = 27
print("my name is {} and my age is {}".format(name, age))

name
print(name)

print("my name is {one}, and age is {two}. more of {one}".format(one=name, two=age))

s = "abcdefghijklmnopqrstuvwxyz"
print(s[21])
print(s[3:])
print(s[:7])
print(s[0])

number = [1,2,3]
number.append(4)
text = ['a','b','c','d','e','f']
print(number, text, number[2])

print(text[2])

print(text[1:3])
text[5] = "NEW"
print(text)
nest = [number, [1,2,3]]
print(nest[1][2])

obj = {'key1':'value1', 'key2':'value2'}
print(obj)
print(obj['key2'])

print("Tupple")
t = (1,2,3,4,5)
print(t)
# t[2] = 3;
t2 = ([1,2,3,4,5,6,6,6])
print(t2)

print("Unique Elements")
ue = {1,1,2,3,4,5,6,6}
print(ue)
print("Set element")
setVar = set([1,2,2,1,2,3,4,5,5,4])
print(setVar)
s = {1,2,3,4}
s.add(8)
print(s)

print("Comparison")
print(1 < 2)
print(1 == 2)
print(1 <= 2)
print("ey" == "hey")
print(("ey" == "ey") and ("bro" == "bro"))
print(("ey" == "ey") or ("bray" == "bro"))

if(1 < 2):
  print("yes, 1 < 2")

if(1 == 2):
  print("yes, its true")
elif(1 == 1):
  print("yes, 1 = 1")
else:
  print("no, its false")


print("sequence")
seq = [1,2,3,4,5]
for item in seq:
  print("the item is {}".format(item))

i = 3
while i <= 5:
  print("the item is? {}".format(i))
  i = i + 1

for x in range(0,1):
  print(x)

x = [1,2,3,4,5]
b = []
for num in x:
  b.append(num**2)

print(b)

print([num**2 for num in range(0,5)])