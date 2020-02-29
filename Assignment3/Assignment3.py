

import random


def boardmaking(size,board):
   for i in range(size):
        board.append([0 for i in range(size)])
       

def tostring():
    for row in board:
            for val in row:
                print(val, end=" ")
            print()

def populationgeneration(population):
    populationsize = 8
    
    print(populationsize)
    
    for i in range(1,populationsize+1):
        population.append(i)
    
    for i in range(len(population)):
    #   a = population.index()

        population[i] = [random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)] 
        
      
   # population[1] =random.randint(1,8),random.randint(1,8)}
    print(population)


def fillboard(size,board,no):
    for i in range(size):
        value = population[no]
        #print(value)
        for j in range(size):
           # print(i,value[j])
            if i+1 == value[j]:
               board[i][j]= 'F'



                

    



       
        

global populationsize
board =[]
size = 8
population = []
boardmaking(size,board)
tostring()
populationgeneration(population)
a= random.randint(0,7)
print(a+1)
fillboard(size,board,a)

tostring()          