from random import randint

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

print("welcome to rock, paper, scissors game\n")
player = input("your choice: ").lower()

print("computer choose: "+computer)

if(player == computer):
    print("this is a tie")
elif(player == "rock" and computer == "paper"):
    print("computer wins")
elif(player == "paper" and computer == "scissors"):
    print("computer wins")
elif(player == "scissors" and computer == "rock"):
    print("computer wins")
elif(computer == "rock" and player == "paper"):
    print("you won, yepee!")
elif(computer == "paper" and player == "scissors"):
    print("you won, yepee!")
elif(computer == "scissors" and player == "rock"):
    print("you won, yepee!")

