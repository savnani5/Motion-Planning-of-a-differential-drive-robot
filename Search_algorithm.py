# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:22:31 2020

@author: Paras

Search algorithms

"""
# BFS using Adjacency list implementation

#graph = {
#  'A' : ['B','C'],
#  'B' : ['D', 'E'],
#  'C' : ['F'],
#  'D' : [],
#  'E' : ['F'],
#  'F' : []
#}
#
#visited_bfs = [] # List to keep track of visited nodes.
#queue = []     #Initialize a queue
#visited_dfs = []
#
#def bfs(visited_bfs, graph, node):
#    visited_bfs.append(node)
#    queue.append(node) 
#    while queue:
#        s = queue.pop(0) 
#        print (s, end = " ") 
#
#        for neighbour in graph[s]:
#            if neighbour not in visited_bfs:
#              
#                visited_bfs.append(neighbour)
#                queue.append(neighbour)
#
## DFS using Adjacency list implementation
#                         
#def dfs(visited_dfs, graph, node):
#    if node not in visited_dfs:
#        print(node)
#        visited_dfs.append(node)
#        for neighbour in graph[node]:
#            dfs(visited_dfs, graph, neighbour)
#
## Driver Code
#bfs(visited_bfs, graph, 'A')
#print()
#dfs(visited_dfs, graph ,'A')
#

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
                    
    return graph


def dijkstra(graph,start,goal):
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
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
 

final_path_edges = [[(76, 383), (235, 368)], [(76, 383), (190, 312)], [(76, 383), (236, 275)], [(76, 383), (563, 394)], [(76, 383), (304, 219)], [(62, 369), (304, 104)], [(76, 356), (235, 368)], [(76, 356), (190, 312)], [(76, 356), (236, 275)], [(76, 356), (563, 394)], [(76, 356), (304, 219)], [(76, 356), (304, 104)], [(89, 369), (235, 368)], [(89, 369), (190, 312)], [(89, 369), (236, 275)], [(89, 369), (563, 394)], [(89, 369), (304, 219)], [(89, 369), (304, 104)], [(235, 368), (76, 383)], [(235, 368), (76, 356)], [(235, 368), (89, 369)], [(235, 368), (563, 394)], [(235, 368), (563, 270)], [(235, 368), (498, 219)], [(190, 312), (76, 383)], [(190, 312), (76, 356)], [(190, 312), (89, 369)], [(190, 312), (304, 219)], [(190, 312), (304, 104)], [(236, 275), (76, 383)], [(236, 275), (76, 356)], [(236, 275), (89, 369)], [(236, 275), (563, 394)], [(236, 275), (563, 270)], [(236, 275), (498, 219)], [(236, 275), (304, 219)], [(236, 275), (304, 104)], [(281, 331), (563, 394)], [(281, 331), (563, 270)], [(281, 331), (498, 219)], [(281, 331), (304, 219)], [(281, 331), (304, 104)], [(563, 394), (76, 383)], [(563, 394), (76, 356)], [(563, 394), (89, 369)], [(563, 394), (235, 368)], [(563, 394), (236, 275)], [(563, 394), (281, 331)], [(563, 394), (498, 219)], [(563, 394), (304, 219)], [(563, 394), (498, 104)], [(563, 270), (235, 368)], [(563, 270), (236, 275)], [(563, 270), (281, 331)], [(563, 270), (498, 219)], [(563, 270), (304, 219)], [(563, 270), (498, 104)], [(563, 270), (608, 64)], [(563, 270), (608, 47)], [(563, 270), (626, 64)], [(686, 270), (498, 219)], [(686, 270), (304, 219)], [(686, 270), (498, 104)], [(686, 270), (608, 64)], [(686, 270), (626, 47)], [(686, 270), (626, 64)], [(498, 219), (235, 368)], [(498, 219), (236, 275)], [(498, 219), (281, 331)], [(498, 219), (563, 394)], [(498, 219), (563, 270)], [(498, 219), (686, 270)], [(498, 219), (608, 64)], [(498, 219), (608, 47)], [(498, 219), (626, 64)], [(304, 219), (76, 383)], [(304, 219), (76, 356)], [(304, 219), (89, 369)], [(304, 219), (190, 312)], [(304, 219), (236, 275)], [(304, 219), (281, 331)], [(304, 219), (563, 394)], [(304, 219), (563, 270)], [(304, 219), (686, 270)], [(304, 104), (62, 369)], [(304, 104), (76, 356)], [(304, 104), (89, 369)], [(304, 104), (190, 312)], [(304, 104), (236, 275)], [(304, 104), (281, 331)], [(304, 104), (608, 64)], [(304, 104), (608, 47)], [(304, 104), (626, 64)], [(498, 104), (563, 394)], [(498, 104), (563, 270)], [(498, 104), (686, 270)], [(498, 104), (608, 64)], [(498, 104), (608, 47)], [(498, 104), (626, 64)], [(608, 64), (563, 270)], [(608, 64), (686, 270)], [(608, 64), (498, 219)], [(608, 64), (304, 104)], [(608, 64), (498, 104)], [(608, 47), (563, 270)], [(608, 47), (498, 219)], [(608, 47), (304, 104)], [(608, 47), (498, 104)], [(626, 47), (686, 270)], [(626, 64), (563, 270)], [(626, 64), (686, 270)], [(626, 64), (498, 219)], [(626, 64), (304, 104)], [(626, 64), (498, 104)], [(76, 383), (62, 369)], [(62, 369), (76, 383)], [(62, 369), (76, 356)], [(76, 356), (62, 369)], [(76, 356), (89, 369)], [(89, 369), (76, 356)], [(89, 369), (76, 383)], [(76, 383), (89, 369)], [(235, 368), (190, 312)], [(190, 312), (235, 368)], [(190, 312), (236, 275)], [(236, 275), (190, 312)], [(236, 275), (281, 331)], [(281, 331), (236, 275)], [(281, 331), (235, 368)], [(235, 368), (281, 331)], [(563, 394), (563, 270)], [(563, 270), (563, 394)], [(563, 270), (686, 270)], [(686, 270), (563, 270)], [(686, 270), (686, 394)], [(686, 394), (686, 270)], [(686, 394), (563, 394)], [(563, 394), (686, 394)], [(498, 219), (304, 219)], [(304, 219), (498, 219)], [(304, 219), (304, 104)], [(304, 104), (304, 219)], [(304, 104), (498, 104)], [(498, 104), (304, 104)], [(498, 104), (498, 219)], [(498, 219), (498, 104)], [(608, 64), (608, 47)], [(608, 47), (608, 64)], [(608, 47), (626, 47)], [(626, 47), (608, 47)], [(626, 47), (626, 64)], [(626, 64), (626, 47)], [(626, 64), (608, 64)], [(608, 64), (626, 64)]]
graph = graph_generation(final_path_edges)
dijkstra(graph,(76,383),(626,64))

print(len(final_path_edges))
graph = graph_generation(final_path_edges)
print(len(graph))


