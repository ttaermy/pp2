#the whitespaces are vital
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b: #"if the first is false, try this"
  print("a and b are equal")
else:
  print("a is greater than b")


#short hand ifs
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#logical operators
a = 200
b = 33
c = 500
if a > b and c > a: #and/or/not
  print("Both conditions are True")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#to avoid an error if empty
a = 33
b = 200

if b > a:
  pass