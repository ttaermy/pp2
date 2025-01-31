#to create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#print the number of items
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#print an item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#print the last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#print the range/negative range (also possible by leaving begin/end value)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#checking the existence of the item
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#to change item values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #u may alsp change a range of items
print(thislist)

#num of new values may not be equal to num of values that are being replaced
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #items will move accordingly

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) 

#insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#add another list(tuple, set, etc.) to a list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#to remove
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #if items >1 it removes the first occurrence
print(thislist)

#to remove specifies index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #if the index isn't specified, it removes the last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #del also can delete the entire list
print(thislist)

#to empty the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#loop through the list (for)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension (shortest for looping through lists)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#loop in one line
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The syntax -- newlist = [expression for item in iterable if condition == True]
#"if" may be omitted

#expressions
newlist = [x.upper() for x in fruits] #uppercase

newlist = [x if x != "banana" else "orange" for x in fruits]

#to sort
thislist = [100, 50, 65, 82, 23] 
thislist.sort() #it also may sort alphabetically
print(thislist)

#to sort in a descending order 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sort with a function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #key = function
print(thislist)

#"sort" is case sensitive (capital > lower case letters)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # sort(key = str.lower) for case-insensitive sort function
print(thislist)

#to reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#to copy the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #"copy" func
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #"list" func
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #":" operator
print(mylist)

#to join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)