#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:12:49 2020

@author: yigitkeser
"""
import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt

cities = pd.read_csv('cities.txt', sep = ';', skiprows = 1 ,  names = ['name','latitude','longitude','admin','city_or_minor','population'])
roads = pd.read_csv('roads.txt', sep = ',', header = None, names = ['city1','city2'])
provinces = cities[cities['city_or_minor'] == 'admin'].reset_index(drop = True)

def getCity(name):
    return provinces[provinces.name == name]

def getX(name):
    return int(getCity(name).longitude)/1000

def getY(name):
    return int(getCity(name).latitude)/1000

def getNeighbors(name):
    return list(roads[roads.city1 == name].city2) + list(roads[roads.city2 == name].city1)

def getDistance(city1,city2):
    return (((getX(city1)-getX(city2))*79)**2 + ((getY(city1)-getY(city2))*111)**2)**0.5

def goTo(city1,city2):
    print("Generating road from {} to {}".format(city1,city2))
    visited = [city1]
    distance = 0.0
    while visited[-1] != city2:
        if all(item in visited for item in getNeighbors(visited[-1])):
            visited = [city1]
            distance = 0.0
            print('***There is no place left unvisited, starting over***\n')
            
        destination = random.choice(getNeighbors(visited[-1]))
        if destination not in visited:
            print("Destination : {} , Distance : {:.2f}".format(destination,getDistance(visited[-1],destination)))
            distance += getDistance(destination,visited[-1])
            visited.append(destination)
            #print(visited)
        
    print("We have reached {} by travelling {} km".format(city2,distance))
    print("Route {}".format(visited))
    return [distance,visited]

#def goToBonus():
    
goTo('Istanbul','Antalya')


