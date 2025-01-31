#to create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
#set is unordered, so it will appear in a random order

#duplicates are ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#False=0, True=1 (duplicates)

#to get a length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#to access an item, we need to use for loops
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#we can't change an item in a set once its created

#to add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#to remove an item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #if item doesn't exists, it will raise an error
print(thisset) 


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #if item doesn't exists, it won't raise an error
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #random item gets removed
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear() #empties the set
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset #deletes the set completely
print(thisset)

#to join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #we can change "union" to "|", but it allows join a set only to other sets
print(set3)

#changes the original set 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection ("&" to work only with sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#difference ("-" to work only with sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) #difference_update may be used

print(set3)

#symmetric difference ("^" to work only with sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2) #symmetric_difference_update

print(set3) #that are not presented in both sets

