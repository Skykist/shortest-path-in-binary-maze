# Michael Chau
"""
Finds the shortest path in a maze, and outputs the distance.
Input matrix should be binary, where 0s are passable and 1s are not.
The maze starts at top-left, and ends at bottom right
Distance is the amount of nodes in the path.
Note: this solution only works for equal columns in each row
"""

import queue

class Node:
    def __init__(self, rowNum, colNum, maze):
        self.rowNum = rowNum
        self.colNum = colNum
        self.maze = maze

    def __hash__(self):
        return self.rowNum ^ self.colNum 

    def __eq__(self, other):
        return self.rowNum == other.rowNum and self.colNum == other.colNum

    def getNeighbors(self):
        #returns list of 0 neighbor nodes at current node
        #0 nodes are passable, 1 is not
        neighbors = []
        rowNum = self.rowNum
        colNum = self.colNum
        maze = self.maze

        #when current row isn't the highest
        if rowNum > 0:
            if maze[rowNum - 1][colNum] == 0: #check if top node is 0
                #appends top node of current node to neighbors list
                neighbors.append( Node(rowNum - 1, colNum, maze) )
                
        #when current node isn't on the left most edge wall
        if colNum > 0:
            if maze[rowNum][colNum - 1] == 0: #check if left node is 0
                neighbors.append( Node(rowNum, colNum - 1, maze) )

        #when current node isn't on the lowest row
        if rowNum < len(maze) - 1:
            if maze[rowNum + 1][colNum] == 0: #check if bottom node is 0
                neighbors.append( Node(rowNum + 1, colNum, maze) )
                
        #when current node isn't on the right most wall
        if colNum < len(maze[0]) - 1:
            if maze[rowNum][colNum + 1] == 0: #check if right node is 0
                neighbors.append( Node(rowNum, colNum + 1, maze) )

        return neighbors

class Graph():

    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze) #how many lists are in the maze list
        self.columns = len(maze[0]) #how many elements in first row

    def bfs(self):
        #returns amount of nodes in the path to the last node of the maze
        visited = queue.Queue() #initialize queue
        start = Node(0, 0, self.maze) #first node is starting point
        visited.put(start) #insert first node to the queue
        distance = {start: 1} #create dictionary for distance to each node

        #while queue isn't empty
        while not visited.empty():

            node = visited.get() #get and remove node in queue
            
            #if node is the last
            if node.rowNum == self.rows - 1 and node.colNum == self.columns - 1:
                #return value from distance dictionary
                return distance[node]

            #for each neighbor node of current node
            for neighbor in node.getNeighbors():
                #if neighbor wasn't visited yet
                if neighbor not in distance.keys():
                    #create node key and add current node's distance + 1 as value
                    distance[neighbor] = distance[node] + 1
                    #insert neighbor to queue
                    visited.put(neighbor)
        
        #if there is no path to last node
        return ("No path found")

def shortestDistance(maze):
    #simplifies solution process
    #creates graph object for maze list and calls bfs()
    g = Graph(maze)
    return g.bfs()

maze1 = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0]
    ]

maze2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
    ]

maze3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
    ]

maze4 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
    ]

maze5 = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0]
    ]

print(shortestDistance(maze1))
print(shortestDistance(maze2))
print(shortestDistance(maze3))
print(shortestDistance(maze4))
print(shortestDistance(maze5))