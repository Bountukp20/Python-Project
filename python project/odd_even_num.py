print("Hello world");
num1 = int(input("what number are you thinking of: "))

if(num1 % 2 == 0):
    print(str(num1)+" is an even number")
else:
    print(str(num1)+" is an odd number");
if(num1 < 1 or num1 > 1000):
    print("The number must not be lower than 1, and not higher than 1000");