# Dictionaries are used to store data values in key:value pairs.

a = {
  "Name": "Harshita",
  "Age": 18,
  "Birth year": 2005,
  "Nick name" : ["Dinku", "Harshii"]
}
# print(a)
# print(a["Name"])
# print(len(a))
# print(type (a))
# print(a.keys())

# a["Subject"] = "BCA"
# a.update({"Subject": "BCA"})
# print(a)

# print(a.values())

# a["Birth year"] = 2006
# a.update({"Birth year": 2006})
# print(a)

# Get a list of the key:value pairs
# x = a.items()
# print(x)

# if "Nick name" in a:
#   print("Yes")

# a.pop("Name")
# print(a)

# a.popitem()
# print(a)

# del a["Age"]
# print(a)

# del a
# print(a)

# a.clear()
# print(a)

# for x in a:
#   print(x)

# for x in a:
#   print(a[x])

# for x in a.values():
#   print(x)

# for x in a.keys():
#   print(x)

# for x, y in a.items():
#   print(x, y)

# b = a.copy()
# print(b)

# b = dict(a)
# print(b)

# myfamily = {
#   "child1" : {
#     "name" : "Harshita",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Vanshika",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Raksha",
#     "year" : 2011
#   }
# }
# print(myfamily)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)
# print(myfamily["child2"]["name"])
# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])




# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	   Description
# clear()	   Removes all the elements from the dictionary
# copy()	   Returns a copy of the dictionary
# fromkeys()   Returns a dictionary with the specified keys and value
# get()	       Returns the value of the specified key
# items()	   Returns a list containing a tuple for each key value pair
# keys()	   Returns a list containing the dictionary's keys
# pop()	       Removes the element with the specified key
# popitem()	   Removes the last inserted key-value pair
# setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	   Updates the dictionary with the specified key-value pairs
# values()	   Returns a list of all the values in the dictionary