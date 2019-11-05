import numpy as np
import sys

cities = []


def input():
    file = sys.argv[1]
    data = open(file,"r")
    data.readline()
    for line in data:   
        city,x,y = line.split()
        cities.append([int(x),int(y)])
    data.close()

def Euclidean_distance(cityX,cityY):
    return ((cityX[0] - cityY[0])**2 + (cityX[1] - cityY[1])**2) ** 0.5

def total_distance(cities):
    return sum([Euclidean_distance(city,cities[index+1]) for index,city in enumerate(cities[:-1])])

def TSP(cities):
    start = cities[0]
    must_visit = cities
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: Euclidean_distance(path[-1],x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

def main():
    input()
    print(total_distance(TSP(cities)))

main()