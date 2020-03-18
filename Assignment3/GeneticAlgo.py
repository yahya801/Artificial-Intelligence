import random


def makeboard(board):
   
   board.clear()
   for i in range(8):
        board.append([0 for i in range(0,8)])

def tostring():
    for row in board:
            for val in row:
                print(val, end=" ")
            print()


def populationgen():
    for i in range(0,8):
        queenpos.append([random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)])
        makeboard(board)
        fillboard(queenpos[i])
        fitness = fitnesscalc(queenpos[i],board)
        population.append((fitness,queenpos[i]))
      #  print(population)
        print('fitness =',fitness)
        tostring()
        print()
    population.sort()
    print(population)   

def RWS():
    a = random.randint(0,7)
    b = random.randint(0,7)
    p1F,p1 = population[a]
    p2F,p2 = population[b]
    print(p1F,p1)
    print(p2F,p2)
    
    


       
               
  #  print(fitness)
def fitnesscalc(array,board):
    # Row Clash
    clash = []
    for i in range(len(array)):
        c = 0
        value = array[i]
        for j in range(len(array)):
            if board[value-1][j] =='F':
                if i != j:
                    c+=1
        clash.append(c)
    #Diagonal Clash
        #right up
        row = value-1
        column = i
        for j in range(len(array)):
            if row > 0 and column < 7:
                if row+1 != value:
                   if board[row][column]=='F':
                       clash[i] = clash[i]+1  
            row-=1
            column+=1   
    #   #right down
        row = value-1
        column = i
        for j in range(len(array)):
            if row < 7 and column < 7:
                if row+1 != value:
                   if board[row][column]=='F':
                       clash[i] = clash[i]+1  
            row+=1
            column+=1 
        #left down
        row = value-1
        column = i
        for j in range(len(array)):
            if row < 7 and column > 0:
                if row+1 != value:
                   if board[row][column]=='F':
                       clash[i] = clash[i]+1  
            row+=1
            column-=1 
        #left up
        row = value-1
        column = i
        for j in range(len(array)):
            if row > 0 and column > 0:
                if row+1 != value:
                   if board[row][column]=='F':
                       clash[i] = clash[i]+1  
            row-=1
            column-=1 
    print(clash) 
    fitness = 0
    for k in range(len(clash)):
        if clash[k] == 0:
            fitness+=1
    return fitness


def roulwheel():
    sum = 0
    fitt= 0
    for i in range(len(population)):
       fit,c = population[i]
       sum+= fit
    for i in range(len(population)):
       fit,chr = population[i]
       fitness = round((fit/sum) ,2)
       fitt +=fitness
       probabilities.append(fitt)
    print(probabilities)
  #  while len(parents) <= 1:
    for i in range(0,2):
        r = round(random.random(),2)
        print(r)
        for j in range(len(population)):
            fit,chr = population[j]
            if r <= probabilities[j] and len(parents) <  2:
                probabilities[j] = -1
               
                parents.append(list(chr))
                break
            else:
                j-=1
        print(probabilities)
    return parents

def crossover():
    offspring1=[]
    offspring2=[]
    parent1 = parents[0]
    parent2= parents[1]
   # print(parent1,parent2)\
    for i in range(len(parent1)):
        if i < 4:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i]) 
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i]) 
    return offspring1,offspring2


def mutation(array):
  
   # print(offspringbin)

    r = random.randint(0,7)
    print(r)
    ranint = bin(array[r])
    print(ranint,'ran')
    if (len(ranint) == 3):
        templist = list(ranint)
        print(templist)
        if templist[2] == '1':
            templist[2] = '0'
        else:
            templist[2] = '1'
        ranint = ''.join(templist)   
        print(ranint,"HHHH")
        ranint = int(ranint,2)
        print(ranint)





        
           
 
                      





    
       
   

            
          
    





            
      







def fillboard(array):
    for i in range(8):
        for j in range(8):
            if i+1 == array[j]:
               board[i][j]= 'F'
             #  print(i,j)






population =[]
parents=[]
probabilities=[]
board =[]
queenpos = []
makeboard(board)
#tostring()
print()
populationgen()
RWS()
print(roulwheel())
offspring1,offspring2 =crossover()
mutation(offspring1)
