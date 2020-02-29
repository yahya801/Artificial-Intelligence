import random


def makeboard(board):
   
   board.clear()
   for i in range(0,8):
        board.append([0 for i in range(0,8)])

def tostring():
    for row in board:
            for val in row:
                print(val, end=" ")
            print()


def populationgen():
    for i in range(0,2):
        queenpos.append([random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)])
        makeboard(board)
        fillboard(queenpos[i])
       
        print(queenpos[i])
        tostring()
        print()
        
    print(queenpos)






def fillboard(array):
    for i in range(8):
        for j in range(8):
            if i+1 == array[j]:
               board[i][j]= 'Q'







board =[]
queenpos = []
makeboard(board)
#tostring()
print()
populationgen()
