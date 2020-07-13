# Fibonacci Numbers

a, b= 0, 1

fibo_nums = []

for i in range(0,10):
    
    t = a + b
    
    a = b
    
    fibo_nums.append(a)
    
    b=t 
    
print(fibo_nums)