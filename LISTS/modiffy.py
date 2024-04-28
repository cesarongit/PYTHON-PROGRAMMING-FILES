thislist = ["apple", "banana", "cherry"]

thislist[1] = "mango"
print(thislist)

thislist[1:3] = "green apple","chiku"
print(thislist)

thislist[1:3] = ["green apple"] #add bracket other it will save each character separate in the string
print(thislist)
 
thislist.insert(1, "wtermelon")
print(thislist)

thislist.append("mango")
print(thislist)

vegie = ["spinach","onion"]
thislist.extend(vegie) #we can add tuples sets also in the extend
print(thislist)

thislist.remove("onion")
print(thislist)

thislist.pop(2) #if not specified it will pop the last element
print(thislist)

del thislist[0] #if not specified then entire list will be deleted
print(thislist)

thislist.clear() #list will present but contents will be deleted
print(thislist)