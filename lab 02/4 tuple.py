#to create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#to access tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#to update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#update with + operator
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#unpacking packed tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #num of variables = values in the tuple

print(green)
print(yellow)
print(red)

#asterisk in the end
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#asterisks isn't in the end
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#loop through tuples (same as with lists)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #through index
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple): #while loop
  print(thistuple[i])
  i = i + 1

#to join tuples (same as lists)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)