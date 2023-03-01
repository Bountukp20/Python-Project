hi_hi = input("hello world")
name = input("what is you name: ")
age = int(input("how old are you: "))
score = float(input("what did you score: "))

if(name == "*" or name == ""):
    print("invalid input in name field")
if(age <= 17):
    print("please you should be above 17 years")
if(score < 12):
    print("you failed")
if(score > 25):
    print("you passed")
else:
    print(name)
    print(age)
    print("your score is "+str(score))
    print("everything looks good")