thistuple = ("apple","banana","berry")
(green,yellow,blue) = thistuple
print(green)
print(yellow)
print(blue)

#Using Asterisk*
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #in red rest of the remaining values will be assign as a list

print(green)
print(yellow)
print(red)