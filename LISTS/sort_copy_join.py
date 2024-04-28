thislis = ["Orange", "mango", "kiwi", "pineapple", "banana"]
thislis.sort()
print(thislis)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= 1) #true
print(thislist)


def myfunc(n): #customization in the sort
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislis.sort(key= str.lower)
print(thislis) #it makes case insensitive sort

thislis.reverse()
print(thislis,"\n")


#copy
mylist = thislis.copy()
print(mylist)
print(thislis)

#join
list3 = mylist+ thislis
print(list3)