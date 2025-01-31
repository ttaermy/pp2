#simple loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#through a string
for x in "banana":
  print(x)

#break -- exit 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range
for x in range(2, 6):
  print(x)


#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#pass
for x in [0, 1, 2]:
  pass