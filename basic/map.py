number = [1,2,3,4,5]

def square(num):
  return num**2

print(square(number[3]))

result = list(map(square,number))

print(result)

"""
Lamda expresiion
"""

t = lambda var:var**2

print(t(2));

result2 = list(map(lambda var:var**3, number));

print(result2)

result3 = list(filter(lambda var: var%2==0, number))

print(result3)

s = "Hello my name is Zaky"

print(s.lower())
print(s.upper())
print(s.split())

d = {"key1":"value1","key2":"value2"}
print(d);
print(d.keys())

e = [1,2,3,4,5]
print(e);
e1 = e.pop()
print(e)
print(e1)
e2 = e.pop(0)
print(e)
print(e2)
e.append("NEW")
print(e)

# Contain
print("x" in [1,2,3])
print("x" in ['x','y','z'])

# Tupple unpacking
t = [(1,2),(3,4),(5,6)]
for (a,b) in t:
  print(a)
  