# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:41:56 2021

@author: ASUS
"""

def generate_skyline(buildings):
    #check if building_array is valid or not
    for i in range(len(buildings)):
        for j in range(len(buildings[i])):
            if j>2:
                print("invalid building at","[",i,"]","[",j,"]:",buildings[i][j])
                return False
            
    #analysis the buildings corner in tuple 
    cornerList = []
    tmpTuple = ()
    for i in range(len(buildings)):
        tmpTuple = (buildings[i][0],buildings[i][2])
        cornerList.append(tmpTuple)
        tmpTuple = (buildings[i][1],buildings[i][2])
        cornerList.append(tmpTuple)
    for i in cornerList:
        print(i)
    print("-analysis-")
        
    #sort tuple[i] ascending with tuple[i][1] descending
    for i in range(len(cornerList)):
        for j in range(i+1,len(cornerList)):
            if cornerList[i][0] > cornerList[j][0]:
                cornerList[i], cornerList[j] = cornerList[j], cornerList[i]
            if cornerList[i][0] == cornerList[j][0] and cornerList[i][1] < cornerList[j][1]:
                cornerList[i], cornerList[j] = cornerList[j], cornerList[i]
    for i in cornerList:
        print(i)
    print("-sort-")
    
    #create a list to add height, with max_height update from tuple[i][1]
    heightList =[0]
    maxHeight = 0
    for i in range(len(cornerList)):
        if cornerList[i][1] not in heightList:
            heightList.append(cornerList[i][1])
            if max(heightList) != maxHeight:
                print(cornerList[i])
                maxHeight = max(heightList)
        else:   
            heightList.remove(cornerList[i][1])
            # print("--1--")
            # print(cornerList[i])
            # print("maxheight", maxHeight)
            # print(type(maxHeight))
            # print(max(heightList))
            # print("--2--")
            if max(heightList) != maxHeight:
                maxHeight = max(heightList)
                cornerList[i] = (cornerList[i][0], maxHeight)
                print(cornerList[i])
                
    print("-skyline-")
    #print [(position, height),(),...] for every time max_height updated
    
print(generate_skyline([(1,3,3),(2,4,4),(5,8,2),(6,7,4),(8,9,4)]))





