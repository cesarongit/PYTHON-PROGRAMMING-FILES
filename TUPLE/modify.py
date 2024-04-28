#we know that we cannot chang the tuple directly,
#however we can do this by changing into list, edit list, and again back into tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple,"\n")
x = list(thistuple)
x[1] = "pineapple"
thistuple = tuple(x)
print(thistuple)
print(type(thistuple),"\n")

#similarly to update add remove etc
#also we can add the tuples as similarly as list
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)