num = int(input("Please enter a number : "))

x = 0 

for i in range(1, num+1):
    while not (num % i): 
        x += 1
        break 

if num == 0 or num == 1 or x >= 3 : 
    print(num, "is not a prime number.")
else :
    print(num, "is a prime number.")