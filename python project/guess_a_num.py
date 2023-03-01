import random
guess_a_num = random.randrange(1, 50)
# print(guess_a_num)
count_num = int(input("Guess a number between 1 and 50: "))
count = 0
count_limit = 5
count += 1

while guess_a_num != count_num:
    if(count_num > guess_a_num):
        print("Guess lower. Try again")
        count_num = int(input("Guess a number between 1 and 50: "))
        count += 1
    else:
        if((count_num < guess_a_num)):
            print("Guess higher. Try again")
            count_num = int(input("Guess a number between 1 and 50: "));
            count += 1
if(count_num == guess_a_num):
    print("Good job, you guessed the number correctly")
    if(count == 1):
        print("Your number of guesses is " + str(count) + " guess")
    else:
        print("Your number of guesses are " + str(count) + " guesses")
