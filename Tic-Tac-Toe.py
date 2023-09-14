"""
Developed by: Masiat Hasin Rodoshi
ID: 19201089
Section: 02
"""
board = """
         |         |
    1    |    2    |    3
         |         |
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
         |         |
    4    |    5    |    6
         |         |
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
         |         |
    7    |    8    |    9
         |         |
"""

from random import randint
import time

side = ""
move= 0
cMove = 0
pMoves = []
comMoves = []
totMoves = []
playRound = 1
endGame = False
winProbCount = 0
largestIndex = 0
smallest = 0
winProbCountCom = 0
largestIndexCom = 0
smallestCom = 1
winningMoves = [[1,2,3],[3,1,2],[2,3,1],[4,5,6],[5,6,4],[4,6,5],[7,8,9],[8,9,7],[7,9,8],[1,4,7],[4,7,1],[1,7,4],[2,5,8],[5,8,2],[2,8,5],[3,6,9],[6,9,3],[3,9,6],[1,5,9],[5,9,1],[1,9,5],[3,5,7],[5,7,3],[3,7,5]]
winProbability = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
winProbabilityCom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def comIsThinking():
    time.sleep(randint(1,2))
    print()
def selectAlternate(val):
    cMove1 = set[val]
    if cMove1 in totMoves:
        cMove1 = randint(1,9)
        while cMove1 in totMoves:
            cMove1 = randint(1,9)
        else:
            cMove1 = set[val]
    return cMove1

print("Tic-Tac-Toe!\n\nDeveloped By: Masiat Hasin Rodoshi\nID:19201089\nSection:02\n\nPress ENTER to start!")
input()
print("Choose a side\nO or X")

while (side not in ['O', 'X']):
    side = input("--> ")
    if (side == "O" or side=="X"):
        print("You've chosen", side)
    else:
        print("Invalid input. Please try again.")
if side == 'O':
    cSide = 'X'
else:
    cSide = 'O'

print(board)
for i in range(0, 5, 1):
    print("Place "+side+" anywhere empty on the board from 1-9")
    while (str(move) not in ['1','2','3','4','5','6','7','8','9']):
        move = input("--> ")
        if (str(move) not in ['1','2','3','4','5','6','7','8','9']):
            print("Character not allowed. Please enter 1-9")
    while (int(move) in totMoves):
        print("Box has already been marked.")
        move = input("--> ")
    pMoves.append(int(move))
    totMoves.append(int(move))
    board = board.replace(move, side)
    print("==========\nRound:",playRound,"\n==========")
    print(board)
    print("Your move:\nYou placed",side,"on position", move)
    for i in range (0, len(winningMoves), 1):
        set = winningMoves[i]
        if set[0] in pMoves and set[1] in pMoves and set[2] in pMoves:
            print('You have won the game!')
            endGame = True
            break
    if endGame==True:
        break
    if len(totMoves)>=9:
        print("Draw!")
        endGame = True
        break
    print("Computer is thinking of a move...")
    comIsThinking()
    #If any moves have been made already
    if (len(pMoves)>1):
        #Computer tries to win
        smallestCom = 1
        largestIndexCom=0
        setCom=0
        for i in range (0, len(winningMoves), 1):
            setCom = winningMoves[i]
            for j in range(0, 3):
                if setCom[j] in comMoves:
                    winProbCountCom +=1
            winProbabilityCom[i]=winProbCountCom
            winProbCountCom = 0
        for i in range (0, len(winningMoves), 1):
            tempSetCom = (winningMoves[i])
            if winProbabilityCom[i]>smallest and (tempSetCom[0] not in pMoves and tempSetCom[1] not in pMoves and tempSetCom[2] not in pMoves ):
                smallestCom = winProbabilityCom[i]
                largestIndexCom = i
        setCom = winningMoves[largestIndexCom]

        if (setCom[0] in comMoves and setCom[1] in comMoves):
            cMove = selectAlternate(2)
        elif (setCom[0] in comMoves and setCom[2] in comMoves):
            cMove = selectAlternate(1)
        elif (setCom[1] in comMoves and setCom[2] in comMoves):
            cMove = selectAlternate(0)
        else:
            pass
        if (cMove in totMoves):
            if cMove in totMoves:
                cMove = randint(1,9)
                while cMove in totMoves:
                    cMove = randint(1,9)

        #computer tries to prevent player from winning
        smallest = 0
        largestIndex=0
        set=0
        for i in range (0, len(winningMoves), 1):
            set = winningMoves[i]
            for j in range(0, 3):
                if set[j] in pMoves:
                    winProbCount +=1
            winProbability[i]=winProbCount
            winProbCount = 0
        for i in range (0, len(winningMoves), 1):
            tempSet = (winningMoves[i])
            if winProbability[i]>smallest and (tempSet[0] not in comMoves and tempSet[1] not in comMoves and tempSet[2] not in comMoves ):
                smallest = winProbability[i]
                largestIndex = i
        set = winningMoves[largestIndex]
        if (set[0] in pMoves and set[1] in pMoves):
            cMove = selectAlternate(2)
        elif (set[0] in pMoves and set[2] in pMoves):
            cMove = selectAlternate(1)
        elif (set[1] in pMoves and set[2] in pMoves):
            cMove = selectAlternate(0)
        else:
            pass
        if (cMove in totMoves):
            if cMove in totMoves:
                cMove = randint(1,9)
                while cMove in totMoves:
                    cMove = randint(1,9)
    #If it's a new game with no moves yet
    else:
        cMove = randint(1,9)
        while cMove in totMoves:
            cMove = randint(1,9)
    if len(totMoves)>=9:
        print("Draw!")
        endGame = True
        break
    comMoves.append(cMove)
    totMoves.append(cMove)
    board = board.replace(str(cMove), cSide)
    print(board)
    for i in range (0, len(winningMoves), 1):
        set = winningMoves[i]
        if set[0] in comMoves and set[1] in comMoves and set[2] in comMoves:
            print('Computer has won the game!')
            endGame = True
            break
    if endGame==True:
        break
    print("Computer's move:\n"+cSide+" on position",cMove)
    move=0
    moveCalc = 0
    playRound +=1


