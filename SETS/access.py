#Set items are unordered, unchangeable, and do not allow duplicate values.
#you cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value
#is present in a set, by using the in keyword.

thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)

print("banana" in thisset) #check
