# PathFindingProject

## Overview

This project aims to allow users to compare and contrast different pathfinding algorithms by vizualising them. The following are the variables that the user is allowed to choose.
* Source Node Coordinates
  * User can choose the x and y coordinates of the source node
* Destination Node Coordinates
  * User can choose the x and y coordinates of the destination node
* Pathfinding Algorithm
  * The user can choose between DFS, Dijkstra, and A* algorithms
* Grid Size
  * The user can choose the grid size (limit of 59x59 to avoid recursion errors)
* Maze Option 
  * The user is given the option to place obstacles over 1/3 of the grid at random 

## Structure 
There are two representations for the grid, the board (for front-end uses) and the graph (for back-end uses). 
The board is a 2-dimensional array of board node objects. Each board node object contains the node's x and y coordinates 
as well as a reference to a tkinter rectangle object. The graph data structure is a 1-dimensional array of Node objects. 
Each Node object as a vertex number, its adjacency linked list, and some values that are exclusive to some of the algorithms.

The conversion from board to graph is quite simple. Each square has a graph connection to each of the 8 squares bordering it. 
The conversion from vertex number to cartesian coordinates and vice-versa is given by the two equations below.

* Converting from Cartesian Coordinates (x,y) to vertexNum: 
  * **vertNum = y*len(board)+x**
* Converting from vertexNum to Cartesian Coordinates (x,y): 
  * **x = vertNum%len(board); y = vertNum/len(board)**

## Algorithms

  ### DFS
  The Depth-First Search Algorithm is a basic pathfinding algorithm for unweighted 
  graph connections. The algorithm starts by finding the distance between every 
  node in the graph and the source node. The distance between two adjacent nodes
  is, by default, 1. Once the algorithm computes the distances, the algorithm will
  backtrack from the destination node to find the shortest path. 
    
  ### A*
  The A* Algorithm is slightly more complicated. A* is considered to be a "smart"
  pathfinding algorithm because the search is skewed towards the destination node
  due to a heuristic function. This heuristic function is variable, but for the 
  purposes of this project, the heirstic function is given by the euclidean distance
  between a node and the destination node. That is ![equation](https://bit.ly/34g2oK0), 
  where i corresponds to the destination node, j cooresponds to the source node, 
  and h is the heuristic function.
  
  Once the heuristic function is computed, a cost function is computed. The cost function
  is equal to the sum of the weights between one node and the source node, similar to 
  the DFS algorithm. The cost function is given by g. Adding these two together will give
  us an overall distance as defined by the A* method, that takes into account the distance 
  from the source node and the distance to the destination node. That is ![equation](https://bit.ly/33qu7IY).
  
  The algorithm starts with the source node and finds the child node with the minimum f value.
  The algorithm enters a loop untill it gets to the destination node. Then, a backtracking is done
  to find the shortest path.
  
  ### Dijkstra
  Upon some research of Dijkstra's algorithm, we find that Dijkstra's algorithm is very similar to the
  A* algorithm, however it does not take into account a heuristic function. Instead, the algorithm
  is not skewed towards the destination node and accounts for the cost function of all nodes in order to
  find the shortest path. Therefore, Dijkstra's algorithm was copied from the A* algorithm with a slight
  modifaction to the heuristic function where ![equation](https://bit.ly/3lfGgpZ)
  

  
