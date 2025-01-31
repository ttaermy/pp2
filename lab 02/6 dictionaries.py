#to create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#dict() constructor to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Duplicate values will overwrite existing values

#length
print(len(thisdict))

#to access an item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x = thisdict.get("model") -- a get method may be added
print(thisdict["brand"])

#to get a list of keys/values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
#x = thisdict.values()

print(x)

#to return each item as tuples in a list
x = thisdict.items()

#to check
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#to change 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#thisdict.update({"year": 2020})

#to add
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
#thisdict.update({"color": "red"})
print(thisdict)


#to remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #the item with the specified key name
#thisdict.popitem() -- the last inserted item
#del thisdict["model"] -- works as pop()
print(thisdict)

#del -- may delete a dict
#thisdict.clear() -- empties a dict

#loops
for x in thisdict: #thisdict.keys/values/items()
  print(x)

for x in thisdict:
  print(thisdict[x])

#to copy dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
#mydict = dict(thisdict)
print(mydict)


#NESTED DICT
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = { #one dict that will contain the other dicts
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#to access an item
print(myfamily["child2"]["name"])

#to loop through
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])