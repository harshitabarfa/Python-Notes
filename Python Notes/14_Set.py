# SEt : Set are used to store multiple items in a single variable.

a={"Harshii", "Mayuri" , "Raksha", "Yogita", "Naman"}
# print(a)

# Length
# print(len(a))

# Type()
# print(type (a))

# Access set items
# for x in a:
#   print(x)

# print("banana" in a)
# print("banana" not in a)


# Add items
# a.add("orange")
# print(a)

# b = {"pineapple", "mango", "papaya"}
# a.update(b)
# print(a)

# Remove items
# a.remove("Naman")
# print(a)

# a.discard("Harshii")
# print(a)

# x = a.pop()
# print(x)
# print(a)

# a.clear()
# print(a)

# del a
# print(a)

# Loops in sets
# for i in a:
#   print(i)

# Join sets
b = {1, 2, 3, "Harshii"}
# c = a.union(b)
# print(c)

# c = a | b
# print(c)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1 | set2 | set3 |set4
# print(myset)

# Update
# a.update(b)
# print(a)

# Intersection
# c = a.intersection(b) # Keep only the duplicates
# print(c)

# c = a & b
# print(c)

# Keep all items from set1 that are not in set2:
# c = a.difference(b)
# print(c)

# c = a - b
# print(c)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# c = a.symmetric_difference(b)
# print(c)

# c = a ^ b
# print(c)

# a.symmetric_difference_update(b)
# print(a)




# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	         Shortcut	       Description
# add()	 	                           Adds an element to the set
# clear()	 	                       Removes all the elements from the set
# copy()	 	                       Returns a copy of the set
# difference()	         -	           Returns a set containing the difference between two or more sets
# difference_update()	 -=	           Removes the items in this set that are also included in another, specified set
# discard()	 	                       Remove the specified item
# intersection()	     &	           Returns a set, that is the intersection of two other sets
# intersection_update()	 &=	           Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                   Returns whether two sets have a intersection or not
# issubset()	         <=	           Returns whether another set contains this set or not
#  	                     <	           Returns whether all items in this set is present in other, specified set(s)
# issuperset()	         >=	           Returns whether this set contains another set or not
#  	                     >	           Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                           Removes an element from the set
# remove()	 	                       Removes the specified element
# symmetric_difference() ^	           Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	 ^=	   Inserts the symmetric differences from this set and another
# union()	             |	           Return a set containing the union of sets
# update()	             |=	           Update the set with the union of this set and others