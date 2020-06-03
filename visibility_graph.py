# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:23:37 2020

@author: Paras

Visibility graph construction

"""
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
from shapely import geometry

#_______________________________________________________________________________

## Function to test the line intersection

def line_intersection(line1, line2):
    
    line1 = geometry.LineString(line1)
    line2 = geometry.LineString(line2)
    x = str(line1.intersection(line2))
    if 'POINT' in x:
        return True
    else:
        return False
    
#______________________________________________________________________________
        
## Graph generation function (Creates Adjacency list form final_path_edges)
        
def graph_generation(final_path_edges):
        
    graph = {}
    for path_edge in final_path_edges:
        vertex = path_edge[0]
        graph[vertex] = {}
        
        if len(graph[vertex]) == 0:
            for path_edge in final_path_edges:
                if path_edge[0] == vertex:
                    distance = int(((path_edge[1][1] - path_edge[0][1])**2 + (path_edge[1][0] - path_edge[0][0])**2)**0.5)
                    graph[vertex].update({path_edge[1]:(distance)})
                    # graph[vertex].update({path_edge[1]:(distance)})
                    
    return graph

#_______________________________________________________________________________

## Obstacle Inflation Function

def obstacle_inflation(image, contours):    
    for i in range(len(contours)):
        for e in contours[i]:
            image = cv2.circle(image, tuple(e[0]), 10, (255,0,0), -1)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
                
    inflated_contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return inflated_contours

#__________________________________________________________________________________

## Dijkstra's shortest path Algorithm
        
def dijkstra_algo(graph,start,goal):
    
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 10000000
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
#    print(shortest_distance)
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        
        return shortest_distance[goal], path


#______________________________________________________________________________________

if __name__=='__main__':

    image = cv2.imread('C:\\Users\\HP\\Desktop\\major proje ct\\vis_graph\\obstacle course3.png')
    # rols, cols,_ = image.shape
    # print(rols, cols)
    # image = cv2.resize(image, (800,400), interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    
    nodes = []            # nodes
    obstacles = []        # set of obstacles
    path_edges = []       # edges between nodes
    obstacle_edges = []   # obstacle edges
    final_path_edges = [] # final total edges        
    
    inflated_contours = obstacle_inflation(image, contours)
    # cv2.imwrite('image.png',image)
    
    for i in range(len(inflated_contours)):
        cnt = inflated_contours[i]
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect) 
 
#     clockwise points in box :
    
#        2 ______ 3
#         |      |
#         |      |
#         |______|
#        1        4
        
        box = np.int0(box)
        obstacles.append(box)
#        points = np.append(points, box, axis=0) 
#        print(box)
        
        image = cv2.drawContours(image, [box] , -1, (0,255,0), 2)        
#        image1 = cv2.drawContours(image, cnt , -1, (0,255,0), 2)        
    
#     Create nodes list
        
    for obstacle in obstacles:
        obstacle_edges.append([[tuple(obstacle[0]),tuple(obstacle[1])], [tuple(obstacle[1]),tuple(obstacle[2])], [tuple(obstacle[2]),tuple(obstacle[3])], [tuple(obstacle[3]),tuple(obstacle[0])]])
        for i in obstacle:
            nodes.append(i)
            
#     Create path_edges list
#     Find all edges in the graph
            
    for node in nodes:
        for obstacle in obstacles:
            if node in obstacle:
                continue
            else:
                for i in obstacle:
                    path_edge = [tuple(node), tuple(i)]
                    path_edges.append(path_edge)
                 
#                    cv2.line(image, path_edge[0], path_edge[1], (0, 0 ,0), 1)    # edges including intersections
    
#     Find visible edges in the graph
      
    for path_edge in path_edges:
        counter = 0
       
        for obstacle in obstacle_edges:
            for obstacle_edge in obstacle:
                if line_intersection(path_edge, obstacle_edge):                
                    counter += 1
        if counter == 4:
            final_path_edges.append([path_edge[0], path_edge[1]])
#            print(path_edge[0], path_edge[1])
            cv2.line(image, path_edge[0], path_edge[1], (0, 0, 0), 1)    # edges excluding intersections 
        
# To add obstacle edges as paths in final_path_edges
            
    for obstacle in obstacle_edges:
        for obstacle_edge in obstacle:
            reverse = [obstacle_edge[1], obstacle_edge[0]]
            final_path_edges.append(obstacle_edge)
            final_path_edges.append(reverse)
            
    # print(final_path_edges)

    graph = graph_generation(final_path_edges)
    print(graph)
    shortest_distance, path = dijkstra_algo(graph,(81, 350),(525,174)) 
    
    for i in range(len(path)-1):
        cv2.line(image, path[i], path[i+1], (0, 0, 255), 3)
    
    print('Shortest path = ', path)
    print()
    print('Shortest distance = ', shortest_distance)
    
    # cv2.imshow('image',image)
    plt.imshow(image)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

