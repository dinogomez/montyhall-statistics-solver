"""
MONTY HALL PROBLEM PROJECT
11:00 4/4/20
Wizerd
accomplished
4:44pm 4/4/20

rewritten
5:30 6/3/20
"""
import os
from random import *
gamelist = []
choiceCounter = 0
hostdoor = 0
wincounter = 0
losecounter = 0


def generate():
    # list for generation
    # limits list to size 3
    zlist = []
    i = 0
    # 0counter
    z = 0
    # 1counter
    y = 0
    while i < 3:
        value = randint(0, 1)
        # checks if 0 is existing
        if value == 0 and z == 0:
            gamelist.append(value)

            z = 1
        # checks 0 duplication
        elif value == 0 and z > 0:
            continue
        # catch 1 duplication
        elif value == 1 and y < 2:
            gamelist.append(value)

            y += 1
        # ensures 0 generation
        elif value == 1 and y == 2:
            gamelist.append(int(0))

        i += 1
    return zlist


"""
#generation_test
a = 0
while a < 10:
	print("Generation: " + str(a+1))
	print(generate())
	a+=1
	if gamelist[x] == int(1) and x!=indexchoice and gamelist[x]!=0:
print("Opening Door: " + str(gamelist[x]))
"""


def choicegenerate():
    value = randint(1, 3)
    return value


def uidoor(choice):

    if choice == 1:
        print("")
        xlist = ["1", "*", "*"]
        for x in range(len(xlist)):
            print("|  " + xlist[x] + "  |  ", end="")
        print(" ", end="\n")
        choiceCounter = 1
    elif choice == 2:
        print("")
        xlist = ["*", "1", "*"]
        for x in range(len(xlist)):
            print("|  " + xlist[x] + "  |  ", end="")
        print(" ", end="\n")
        choiceCounter = 2

    elif choice == 3:
        print("")
        xlist = ["*", "*", "1"]
        for x in range(len(xlist)):
            print("|  " + xlist[x] + "  |  ", end="")
        print(" ", end="\n")
        choiceCounter = 3


def hostchoose(choice):

    indexchoice = gamelist[choice-1]
    print("choice: " + str(indexchoice))
    x = 0
    hostdoor = 0
    for x in range(len(gamelist)):
        if choice-1 == x:
            continue
        if gamelist[x] == 1 and x != choice-1:
            print("*Host Chooses to open Door#" + str(x+1))
            uidoor(x+1)
            return x
            break


def clear():
    gamelist.clear()


def menu():

    # generate game choices
    generate()

    print("---------------------------")
    print("Gamelist:", end="")
    print(gamelist)

    print("\n\t MONTY HALL GAME")
    xlist = ["*", "*", "*"]
    print("")
    for x in range(len(xlist)):

        print("|  " + xlist[x] + "  |  ", end="")
    print(" ", end="\n")

    # generate autochoice
    choice = choicegenerate()

    print("\nPlayer: Choosing Door#" + str(choice))
    hostdoor = hostchoose(choice)
    print("\nHost: Do you want to change Doors?")
    print("Player: Yes")
    print("Host opens final door: " + str(choice))
    x = 0
    for x in range(len(gamelist)):
        if gamelist[choice-1] == int(1):
            print("\nSTATUS:Win")
            clear()
            os.system('cls')  # For Windows
            return True
            break
        else:
            print("\nSTATUS:Lose")
            clear()
            os.system('cls')  # For Windows
            return False
            break


x =0
print("\n\tMONTY HALL GAME GENERATOR")
y = input("How many games do you want to generate? ")
z = int(y)
while x < z:

    status = menu()
    if status == True:
        wincounter += 1
        print("    MONTY HALL PROBLEM")
        print("\t @Wizerd")
        print("\tSTATISTICS")
        print("\tGame: " + str(x+1))
        print("---------------------------")
        print("\tWins: " + str(wincounter))
        print("\tLose: " + str(losecounter))
        print("\n\tWin%--" + str(round(wincounter/(wincounter+losecounter)*100, 2)) +
              "% \n\tLose%-"+str(round(losecounter/(wincounter+losecounter)*100, 2))+"%")

    else:
        losecounter += 1
        print("    MONTY HALL PROBLEM")
        print("\t @Wizerd")
        print("\tSTATISTICS")
        print("\tGame: " + str(x+1))
        print("---------------------------")
        print("\tWins: " + str(wincounter))
        print("\tLose: " + str(losecounter))
        print("\n\tWin%--" + str(round(wincounter/(wincounter+losecounter)*100, 2)) +
              "% \n\tLose%-"+str(round(losecounter/(wincounter+losecounter)*100, 2))+"%")
    x += 1

input()
