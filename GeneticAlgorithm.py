import random


"""
<--------------------------------------------------Functions Needed for Step 1 (Selection) -------------------------------------------------------------------->

"""

def selection(pop):
    fitness_list=[routeFitness(pop[i]) for i in range(len(pop))]
    probabilityList=selectionProb(fitness_list)
    parents = []
    var = 1
    while(var == 1):
        parent_index = weightedRandomChoice(probabilityList)
        if(len(parents) == 2 ):
            break
        else:
            if pop[parent_index] in parents:
                continue
            else:
                parents.append(pop[parent_index])

    return parents

def routeFitness(route):
    #Calculates finess of each route.
    distance=0
    for i in range(0,9):

        temp_lis=dictx[route[i]]
        temp_str=route[i+1]
        if temp_str=='C10':
            connecting_city=10
        else:
            connecting_city=int(temp_str[1])
        #print(temp_lis[connecting_city-1])
        distance+=temp_lis[connecting_city-1]
    return distance

def selectionProb(fit_list):
    fitness_sum = sum(fit_list)
    selection_prob= [i/fitness_sum for i in fit_list]
    return selection_prob

def weightedRandomChoice(prob_list):
    #Roulete Wheel method used for selection.
    total_prob = sum(prob_list)
    pick = random.uniform(0,total_prob)
    current = 0
    for i in range(0,len(prob_list)):
        current+=prob_list[0]

        if current > pick:

            return i
    return prob_list.index(max(prob_list))

"""
<-------------------------------------------------------------------------Step 1 Functions End Here! ------------------------------------------------------------>
"""

"""
<----------------------------------------------------------------------------Step 2 Crosover------------------------------------------------------------------------->
"""

def mate(parent_list):
    #Generating random number for crossower.

    rand = random.randint(0,9)
    temp_child, children=[], []

    for i in range (len(parent_list)):
        for j in range(rand):
            temp_child.append(parent_list[i][j])
        for k in range(len(parent_list[0])):
            if i==0:
                #print("k ", k)
                if parent_list[1][k] not in temp_child:
                    temp_child.append(parent_list[1][k])
            if i==1:
                #print("k ", k)

                if parent_list[0][k] not in temp_child:
                    temp_child.append(parent_list[0][k])

        children.append(temp_child)
        temp_child=[]
    return children


"""
<---------------------------------------------------------------------------------Step 3 Mutation--------------------------------------------------------------------->
"""


def mutate(child_list):
    for i in range(len(child_list)):
        rand1 = random.randint(0,9)
        rand2 = random.randint(0,9)
        temp = child_list[i][rand1]
        child_list[i][rand1]=child_list[i][rand2]
        child_list[i][rand2]=temp
    return child_list


"""
<------------------------------------------------------------------------End------------------------------------------------------------------------------------------>
"""

#A Dictionary that contain cities as keys and values are a list whose elemets are distances from that city to all other cities.
#Index+1 of a list is the city number that it has as element.
#Such as index 2 represents C3.

dictx = {'C1':[0,66,21,300,500,26,77,59,125,650],'C2':[66,0,35,115,36,65,85,90,44,54],'C3':[21,35,0,450,448,846,910,47,11,145],'C4':[300,115,450,0,65,478,432,214,356,251],
'C5':[500,36,448,65,0,258,143,325,125,39],'C6':[26,65,846,478,258,0,369,256,345,110],'C7':[77,85,910,432,143,369,0,45,120,289],
'C8':[69,90,47,214,325,256,45,0,325,981],'C9':[125,44,11,356,125,345,120,325,0,326],'C10':[650,54,145,251,39,110,289,981,326,0]}

#Chromosome Representation.
#The order presents the sequnce in which cities shall be visited.
#A fitness function calculates the total distance between each city in the chromosome representation.
#The smaller the overall distance, the higher the fitness of the individual.

cities = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
#routeFitness(cities)
#Initial Population.
#With given cities, randomly generate a population of possible routes.
#Population size = 50

population_size=50


#A 2D list to hold all the shuffled states.
population= []

#Generating random states for to build up population.
for i in range (0,population_size):
    population.append(random.sample(cities,len(cities)))


fitness = 1000000

for i in range(0,600):
    temp_list1 = mutate(mate(selection(population)))
    tempvar=routeFitness(temp_list1[0])
    tempvar2=routeFitness(temp_list1[0])
    temp_min = min(tempvar,tempvar2)
    
    #Step 4 Evaluation.
    if temp_min < fitness:
        fitness = temp_min
        if tempvar == temp_min:
            fit_route = temp_list1[0]
        else:
            fit_route = temp_list1[1]
    population.append(temp_list1[0])
    population.append(temp_list1[1])
    print("Generation:",i+1) 
    print("Route: ", fit_route)
    print("fitness: ",fitness)
