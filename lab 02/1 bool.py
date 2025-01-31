#true or false
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#with bool those will return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#with bool those will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#functions to return bool
def myFunction() :
  return True

print(myFunction())

#to answer ques
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")