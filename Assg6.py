n = int(input("Please enter a number: "))
prime_nums=[]
for x in range(2,n + 1):
    for y in range(2,x):
        if (x % y) == 0:
            break
    else:
        prime_nums.append(x)
print(prime_nums)