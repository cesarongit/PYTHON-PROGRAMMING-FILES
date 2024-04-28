n = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
next_number = 0
count = 1
10
while(count <= n):
   print(next_number, end=" ")
   count += 1
   num1 = num2
   num2 = next_number
   next_number = num1 + num2
   t_number = num1 + num2