import sys
import random
import copy
import time
import math
import numpy as np

cities = []

#input fuction
def input():
    file = sys.argv[1]
    data = open(file,"r")
    data.readline()
    for line in data:   
        city,x,y = line.split()
        cities.append([int(x),int(y)])
    data.close()

#calculation funtion of distance between two cities    
def Euclidean_distance(cityX,cityY):
    return ((cityX[0] - cityY[0])**2 + (cityX[1] - cityY[1])**2) ** 0.5

#calculation function of all cost for current tour
def total_distance(cities):
    return sum([Euclidean_distance(city,cities[index+1]) for index,city in enumerate(cities[:-1])])

#generate a random beginning tour
def init_random_tour(cities):
    length = len(cities)
    tour = cities[1:]   #note that we have to begin tour from city A always
    random.shuffle(tour)
    tour.insert(0,cities[0])
    return tour

#generate all neighbors of current state
def neighbors_generate(tour):
    neighbors = []
    for i in range(len(tour)):
        if i == len(tour) - 1:
            break;
        temp = copy.copy(tour)
        temp[i],temp[i+1] = temp[i+1],temp[i]
        neighbors.append(temp)
    return neighbors
    
def hill_climb(cities):
    num_steps = 0
    best = init_random_tour(cities)
    current_cost = total_distance(best)
    while True:
        move_model = False
        for i in neighbors_generate(best):
            if total_distance(i) < current_cost:
                current_cost = total_distance(i)
                best = i
                move_model = True
                num_steps += 1
        if move_model == False:
            break
    return (best,current_cost,num_steps)

def hill_climb_random_restart(cities):
    best = None
    best_cost = 0
    max_times = 1000
    times = 0
    restart = 0
    
    while times < max_times:
        remain_times = max_times - times
        tour,cost,steps = hill_climb(cities)
        times += steps
	if cost > best_cost or best is None:
            best_cost = cost
            best = tour
	'''
    	if best_cost / 322 <= 1.01:
		break;
        '''
	restart += 1
    return (best,best_cost)

def simulated_annealing(cities):
    best = init_random_tour(cities)
    current_cost = total_distance(best)
    time = 0
    T = 1000
    while T > 1:
        next = random.choice(neighbors_generate(best))
        E = current_cost - total_distance(next)
        if E > 0:
            best = next
	    time += 1
        else:
            factor = E / T
            probility = np.exp(factor)
            temp = random.uniform(0,1)
            if probility > temp:
                best = next
  		time += 1
	'''
	T /= 1.01
	T *= 0.98 
	'''
	T -= 1

    #print(time)
    return (best,current_cost)

def main():
   start_time = time.time()
   input()
   tour,cost = simulated_annealing(cities)
   print(time.time()-start_time)
   print(cost / 318)
  
if __name__ == "__main__":
    main()
