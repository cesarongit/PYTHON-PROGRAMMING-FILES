import random
import math
print("********Welcome to the Guess the Number game*********\n")
up = int(input("Guess the upper bound: "))
low = int(input("Guess the lower bound: "))

x = random.randint(low,up) 
round = round(math.log(up - low + 1, 2 ))

print("\nYou have ",round," chances to guess the number")
print("Start Guessing now: ")

count = 0

while(count<round):
    count += 1
    val = int(input("Enter the number: "))
    if(val==x):
        print("Congratulations, you have guessed the number in ",count," try")
        break
    elif(val<x):
        print("You guessed the small value")
    elif(val>x):
        print("You guessed the large value")
        
    print("\nChances left: ",round-count)

if(count>=round):
    print("Guessing limit has been reached\n","Better luck next time...!!!")
    print("The number was ",x)