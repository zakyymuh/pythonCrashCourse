print("** What is 7 to the power of 4?**")
print(7**4)

print("** Split this string:**   s = 'Hi there Sam!' **into a list. **")
s = "Hi there Sam!"
print(s.split())

print("** Given the variables:** \n        planet = 'Earth'\n         diameter = 12742\n    ** Use .format() to print the following string: ** \n The diameter of Earth is 12742 kilometers.")
planet = "Earth"
diameter = 12742
print("THe diamter of {} is {} killometer".format(planet, diameter))

print("** Given this nested list, use indexing to grab the word 'hello' **")
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])
print("Create a function that grabs the email website domain from a string in the form: ** user@domain.com\n")
domain = "user@domain.com"
def getDomain(dom):
  lst = dom.split("@")
  print(lst[1])

getDomain(domain)

print("Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.\n")
def findDog(dogStatement):
  listOfString = dogStatement.split()
  for item in listOfString:
    if(item == "dog" or item == "DOG"):
      return True
  return False

if(findDog("Is there any dog here?")):
  print("Yes")
else:
  print("Nope")

print("Lambda function exercise")
seq = ['soup','dog','salad','cat','great']

filterseq = list(filter(lambda x: x[0] == "s", seq))
print(filterseq)

### Final Problem
print("**You are driving a little too fast, and a police officer stops you. Write a function")
print('to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".') 
print('If your speed is 60 or less, the result is "No Ticket". If speed is between 61 ')
print('and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all ');
print("cases. **")

def caught_speeding(speed, is_birthday):
  if(is_birthday):
    speed = speed - 5

  if(speed > 60 and speed <= 80):
    return "Small Ticket"
  elif (speed > 80):
    return "Big Ticket"
  else:
    return "No Ticket"
  

print(caught_speeding(65, True))
print(caught_speeding(67, False))
print(caught_speeding(88, False))