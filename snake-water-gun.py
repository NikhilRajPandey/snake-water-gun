print("  \t\t\t Welecome to Snake , Water , Gun game\n\n")


import random

attempts= 1
your_point=0
computer_point=0
while (attempts<=10):

    lst=["snake","water","gun"]
    ran=random.choice(lst)
    print("what do you choose snake, water or gun")
    inp=input()


    if inp==ran:
        print("tie")
        print(f"you choosed {inp} and computer guess is {ran}")
        print("No body gets point\n")



    elif inp=="snake" and ran=="water":
        your_point=your_point+1
        print(f"you choosed {inp} and computer guess is {ran}")
        print("The snake drank water\n")
        print("You won this round")
        print("you get 1 point\n")


    elif inp=="water" and ran=="snake":
        computer_point = computer_point + 1
        print(f"you choosed {inp} and computer guess is {ran}")
        print("The snake drank water\n")
        print("You Lost this round")
        print("computer gets 1 point\n")

    elif inp=="water" and ran=="gun":
        print(f"you choosed {inp} and computer guess is {ran}")
        your_point = your_point + 1
        print("The gun sank in water\n")
        print("You won this round")
        print("you get 1 point\n")


    elif inp == "gun" and ran == "water":
        print(f"you choosed {inp} and computer guess is {ran}")
        computer_point = computer_point + 1
        print("The gun sank in water\n")
        print("You Lost this round")
        print("computer gets 1 point\n")



    elif inp == "gun" and ran == "snake":
        print(f"you choosed {inp} and computer guess is {ran}")
        your_point = your_point + 1
        print("The snake was shoot and he died\n")
        print("You Won this round")
        print("you get 1 point\n")

    elif inp == "snake" and ran == "gun":
        print(f"you choosed {inp} and computer guess is {ran}")
        computer_point=computer_point+1
        print("The snake was shoot and he died\n")
        print("You Lost this round")
        print("computer gets 1 point\n")

    else:
        print("invalid")




    print(10 - attempts, "no. of guesses left")
    attempts = attempts + 1

    if attempts>10:
        print("game over")

if computer_point > your_point:
    print("Computer wins and you loose")

if computer_point < your_point:
    print("you win and computer loose")

print(f"your point is {your_point} and computer point is {computer_point}")





