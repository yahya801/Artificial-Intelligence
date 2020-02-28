

import random


def boardmaking(size,board):
   for i in range(size):
        board.append([0 for i in range(size)])
       

def tostring():
    for row in board:
            for val in row:
                print(val, end=" ")
            print()

def populationgeneration():
    populationsize = random.randint(1,8)
    population = []
    print(populationsize)
    
    for i in range(1,populationsize+1):
        population.append(i)
    
    for i in range(len(population)):
    #   a = population.index()

        population[i] = i+1, [random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)]  
        
      
   # population[1] =random.randint(1,8),random.randint(1,8)}
    print(population)
    



board =[]
boardmaking(8,board)
tostring()
populationgeneration()