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
        fitness(queenpos[i],board)
       
        print(queenpos[i])
        tostring()
        print()
        
    print(queenpos)





def fitness(bb,board):
    fitness =[]
    
    for i in range(len(bb)):
        clash = 0
        for j in range(len(bb)):
            value = bb[i]
            if value == bb[j] and i != j:
               # print(value, bb[i])
                clash +=1
        #print(clash)  
        fitness.append(clash)     
    
    for i in range(len(bb)):
        a = i 
        b= len(bb) 
        clashe2=0
      #  print(a,"jj")
        value = bb[i]-1
        while a< 0 or b > 7:
           if board[a][b] == 'F':
               clashe2 +=1
           a -=1
           b +=1
        print(clashe2)


       
               
    print(fitness)


def fitness1(bb,board):
    for i in range(len(bb)):
        value = bb[i]
        print(board[value-1][i])
        if  board[value-1][i] == 'Q':
            for j in range(len(bb)):
                board
    




def fillboard(array):
    for i in range(8):
        for j in range(8):
            if i+1 == array[j]:
               board[i][j]= 'F'
             #  print(i,j)







board =[]
queenpos = []
makeboard(board)
#tostring()
print()
populationgen()
