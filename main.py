import random

NEWLINE = '\n'


def generateGrid():
    """
    Generates a grid according to the grid size
    Each row will have 10 cells i.e there would be 10 columns
    """
    tempList = []
    tempGrid = []
    for i in range(gridSize, 0, -1):
        tempList.append(i)
        if str(i)[-1] == '1':
            tempGrid.append(tempList)
            tempList = []

    for i in range(len(tempGrid)):
        if i % 2 == 1:
            tempGrid[i].reverse()
        for j in tempGrid[i]:
            grid.append(j)


def printGrid(argList):
    """
    Prints the grid
    :param argList: a list containing the grid
    """
    count = 0
    for i in argList:
        if count == 10:
            print(NEWLINE)
            count = 0
        print(' %3d ' % i, end=" ")
        count += 1
    print(NEWLINE)


def appendForbidden(value):
    """
    Adds value to the forbidden list which contains coordinates where snakes and ladders cannot be generated
    :param value: coordinate to be added to the foribidden list
    """
    forbiddenList.append(value)


def isForbidden(value):
    """
    Check if value is in the forbidden list which contains coordinates where snakes and ladders cannot be generated
    :param value: presence to be checked the foribidden list
    :return: true if value is present otherwise return false
    """
    if value in forbiddenList:
        return True
    else:
        return False


def generateSnakesandLadders():
    """
    generates snakes and ladders for the game
    """
    for i in range(maxSnakesCount + maxLaddersCount):
        tempList = []
        while True:
            coordinate = random.randint(1, gridSize)
            if (len(tempList) == 0 and isForbidden(coordinate) == False) or \
                    (len(tempList) == 1 and coordinate > tempList[0] and isForbidden(coordinate) == False):
                tempList.append(coordinate)
                appendForbidden(coordinate)
                if len(tempList) == 2:
                    break
        if i % 2 == 0:
            snakesList.append(tempList)
        else:
            laddersList.append(tempList)


if __name__ == '__main__':
    gridSize = 100
    diceMinValue = 1
    diceMaxValue = 6
    maxSnakesCount = 4
    maxLaddersCount = 4

    grid = []
    snakesList = []
    laddersList = []
    forbiddenList = []

    generateGrid()
    printGrid(grid)

    generateSnakesandLadders()

    print(snakesList)
    print(laddersList)

    # making the game
    player1 = 1
    player2 = 1
    chanceCounter = 0
    while True:
        if chanceCounter > 100:
            print("too many chances")
            break

        dice_value = random.randint(diceMinValue, diceMaxValue)
        if chanceCounter % 2 == 0:
            print("player1", end=" ")
            player1 += dice_value
            if player1 == gridSize:
                print("player 1 wins")
                break
            elif player1 > gridSize:
                player1 -= dice_value
                print("too high")
            else:
                # check snakes and ladder
                for i in snakesList:
                    if player1 == i[1]:
                        player1 = i[0]
                        break
                for i in laddersList:
                    if player1 == i[0]:
                        player1 = i[1]
                        break

        else:
            print("player2", end=" ")
            player2 += dice_value
            if player2 == gridSize:
                print("player 2 wins")
                break
            elif player2 > gridSize:
                player2 -= dice_value
                print("too high")
            else:
                # check snakes and ladder
                for i in snakesList:
                    if player2 == i[1]:
                        player2 = i[0]
                        break
                for i in laddersList:
                    if player2 == i[0]:
                        player2 = i[1]
                        break
        print("d", dice_value, player1, player2)
        chanceCounter += 1

# for the snakes and ladders generation its better to use a list for the randomit and keep reducing the options of the list
# randomint in snakes and ladders generation is the belived reason for the never ending program

# keep track of snake bites and ladder climbs and moves in total

# first complete the program with only randomints and no user interaction
# then a seperate version with full user interaction

# use proper class structure

# have different folders for each version and maybe in the projects main allow user to choose
# maintain different versions of this - (A) one fully automated (full reliation on random functions),
# (B) one with full user play turn by turn and fixed snakes and ladders,
# (C) one with full user play turn by turn and changing snakes and ladders (reliation on random)
# (D) linked list or other data structure implementation
# (E) graph implmentation from CSE 102


######## for snakes and ladders generation
#
# import random
#
# # initializing list
# test_list = [1, 4, 5, 2, 7]
#
# # printing original list
# print("Original list is : " + str(test_list))
#
# count = 0
# f = []
# # using random.choice() to
# # get a random number
# while test_list:
#     random_num = random.choice(test_list)
#     # printing random number
#     print("Random selected number is : " + str(random_num))
#     f.append(random_num)
#     test_list.remove(random_num)
#
# print(f)

