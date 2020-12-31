import random

# List of correct choices
choices = ["rock", "paper", "scissors"]
correct = False
print(chr(27) + "[2J") # This clears the console
print("Rock, Paper, Scissors - Game")
print("Coded by nooney >:)")
print("------------------------------")
print("\nPlease input your choice.")
while correct == False:
    computerchoice = random.choice(choices)
    rawuserchoice = input("Available options - Rock; Paper; Scissors: ")
    userchoice = rawuserchoice.lower()
    print("\nYou chose: " + rawuserchoice)
    if userchoice not in choices:
        print("\nOops! This choice does not seem to be correct. Please try again!")
    else:
        correct = True
print("The computer chose: " + computerchoice)

while userchoice == computerchoice:
    if userchoice == "scissors":
        print("Your scissors were cancelled out by the computer's scissors!")
        print("Please make another choice.")
    else:
        print("Your " + userchoice + " was canceled out by the computer's " + computerchoice + "!")
        print("Please make another choice.")
    while True:
        rawuserchoice = input("Available options - Rock; Paper; Scissors: ")
        userchoice = rawuserchoice.lower()
        print("\nYou chose: " + rawuserchoice)
        if userchoice not in choices:
            print("\nOops! This choice does not seem to be correct. Please try again!")
        else: break
    computerchoice = random.choice(choices)
    print("The computer chose: " + computerchoice)

if userchoice == "rock" and computerchoice == "paper":
    print("Your rock was beaten by the computer's paper!")
    print("You lost.")
elif userchoice == "scissors" and computerchoice == "rock":
    print("Your scissors were beaten by the computer's rock!")
    print("You lost.")
elif userchoice == "paper" and computerchoice == "scissors":
    print("Your paper was beaten by the computer's scissors!")
    print("You lost.")
else:
    if computerchoice == "scissors":
        print("The computer's scissors were beaten by your " + userchoice + "!")
        print("You win!")
    else:
        print("The computer's " + computerchoice + " was beaten by your " + userchoice + "!")
        print("You win!")
        