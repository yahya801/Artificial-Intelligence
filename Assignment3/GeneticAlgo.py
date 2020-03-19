import random



def makeboard(board):

    board.clear()
    for i in range(8):
        board.append([0 for i in range(0, 8)])


def tostring():
    for row in board:
        for val in row:
            print(val, end=" ")
        print()


def populationgen():
    population.clear()
    for i in range(0, 8):
        queenpos.append([random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(
            1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)])
        makeboard(board)
        fillboard(queenpos[i])
        fitness = fitnesscalc(queenpos[i], board)
        population.append((fitness, queenpos[i]))
    population.sort()
   # print(population,'generation')


def fitnesscalc(array, board):
    # Row Clash
    clash = []
    for i in range(len(array)):
        c = 0
        value = array[i]
        for j in range(len(array)):
            if board[value-1][j] == 'F':
                if i != j:
                    c += 1
        clash.append(c)
    # Diagonal Clash
        # right up
        row = value-1
        column = i
        for j in range(len(array)):
            if row > 0 and column < 7:
                if row+1 != value:
                    if board[row][column] == 'F':
                        clash[i] = clash[i]+1
            row -= 1
            column += 1
    #   #right down
        row = value-1
        column = i
        for j in range(len(array)):
            if row < 7 and column < 7:
                if row+1 != value:
                    if board[row][column] == 'F':
                        clash[i] = clash[i]+1
            row += 1
            column += 1
        # left down
        row = value-1
        column = i
        for j in range(len(array)):
            if row < 7 and column > 0:
                if row+1 != value:
                    if board[row][column] == 'F':
                        clash[i] = clash[i]+1
            row += 1
            column -= 1
        # left up
        row = value-1
        column = i
        for j in range(len(array)):
            if row > 0 and column > 0:
                if row+1 != value:
                    if board[row][column] == 'F':
                        clash[i] = clash[i]+1
            row -= 1
            column -= 1

    fitness = 0
    for k in range(len(clash)):
        if clash[k] == 0:
            fitness += 1
    return fitness


def roulwheel():
    parents.clear()
    probabilities.clear()

    sum = 0
    fitt = 0
   # print(range(len(population)),'range')

    for i in range(len(population)):

        fit, c = population[i]
        sum += fit

    for i in range(len(population)):
        fit, chr = population[i]
        fitness = round((fit/sum), 2)

        fitt += fitness
        probabilities.append(fitt)

    p1 = random.choice(probabilities)
    for i in range(len(probabilities)):
        if (p1 == probabilities[i]):
          #  print(i,'i')
            fit, chr = population[i]
            parents.append(list(chr))
            break

    p2 = random.choice(probabilities)
    while(p2 == p1):
        p2 = random.choice(probabilities)
    for i in range(len(probabilities)):
        if (p2 == probabilities[i]):
            fit, chr = population[i]
            parents.append(list(chr))
            break


def crossover():
    offspring1 = []
    offspring2 = []
    parent1 = parents[0]
    parent2 = parents[1]
    for i in range(len(parent1)):
        if i < 4:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])
    return offspring1, offspring2


def mutation(array):
    child = []
    for i in range(0, 2):
        r = random.randint(0, 7)

        ranint = bin(array[r])

        if (len(ranint) == 3):
            templist = list(ranint)
            templist.append('1')
            ranint = ''.join(templist)
            ranint = int(ranint, 2)
        elif (len(ranint) == 4):
            templist = list(ranint)

            r = random.randint(2, 3)

            if r != 2 or r == 3:
                if templist[r] == '0':
                    templist[r] = '1'
                else:
                    templist[r] = '0'
            else:
                templist.append('1')
            ranint = ''.join(templist)

            ranint = int(ranint, 2)

        elif (len(ranint) == 5):
            templist = list(ranint)

            if templist[3] == '0':
                templist[3] = '1'
            else:
                templist[3] = '0'
            if templist[4] == '0':
                templist[4] = '1'
            else:
                templist[4] = '0'

            ranint = ''.join(templist)
            ranint = int(ranint, 2)

        elif (len(ranint) == 6):
            templist = list(ranint)
            if templist[2] == '1':
                templist[2] = '0'
                a = random.randint(3, 5)
                if templist[a] == '0':
                    templist[a] = '1'
                b = random.randint(3, 5)
                if templist[b] == '0':
                    templist[b] = '1'
            ranint = ''.join(templist)
            ranint = int(ranint, 2)
        array[r] = ranint

    child = (array)
    return child


def fillboard(array):
    for i in range(8):
        for j in range(8):
            if i+1 == array[j]:
                board[i][j] = 'F'


def geneticalgo():
    populationgen()
    chromosome = []
    fit = 0
    i = 0
    a = 0
    while (fit <= 7):
        if (len(population) > 100):
           
            population.pop(0)

       
        roulwheel()
        offspring1, offspring2 = crossover()

        newpop1 = mutation(offspring1)
        newpop2 = mutation(offspring2)
        makeboard(board)
        fillboard(newpop1)
        fitness = fitnesscalc(newpop1, board)
        offspring = (fitness, newpop1)
        makeboard(board)
        fillboard(offspring2)
        fitness2 = fitnesscalc(newpop2, board)
        if(fitness > fitness2):
            population.append(offspring)
            fit = fitness
        else:
            offspring = (fitness2, newpop2)
            population.append(offspring)
            fit = fitness2

        a, chromosome = offspring
        print('iteration =', i, 'chromosome: ', chromosome, 'fitness =', fit)
       # print(fit)
        population.sort()

        i += 1
        a += 1
        if (a > 2500):
            populationgen()
            a = 0

        if (i > 25000):  # to limit no of iterations
            if (fit >= 6):
                break

    
    print(chromosome)
    #print(population)





# Variables
population = []
parents = []
probabilities = []
board = []
queenpos = []

# Function Call

geneticalgo()
