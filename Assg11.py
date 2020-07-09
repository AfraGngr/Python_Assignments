number = input("Please enter a number : ")

while ("." in list(number) or "," in list(number) or "-" in list(number) or number.isnumeric()==False):
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
    break 
    
number = input("Please enter a number : ")

number_1 = set(number)

if_amstrong = sum((int(i) ** len(number_1)) for i in number_1)

if if_amstrong == int(number):
    
    print(f"{number} is an Amstrong number")

else:
    
    print(f"{number} is not an Amstrong number")