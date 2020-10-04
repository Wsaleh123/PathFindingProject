from tkinter import *
import time 
import sys
import tkinter.font as tkFont
from random import random
from Heap import Heap


sys.setrecursionlimit(3500)

class Edge():
    def __init__(self, vnum, next, weight):
        self.vnum = vnum
        self.weight = weight
        self.next = next 

class boardNode():
    def __init__(self, x, y, vnum):
        self.x = x
        self.y = y
        self.vnum = vnum
        self.box = None

class Node():
    def __init__(self, vnum):
        self.vnum = vnum
        self.adjLists = None
        self.f = 9999999
        self.h = 9999999
        self.g = 9999999

class grid():
    def __init__(self, x, y, m, n):
        self.board = [[None]*m for i1 in range(n)]
        self.graph = [None]*(m*n)
 
        #ESTABLISHING CONNECTION TO 8 SURROUNDING BOXES
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                vertNum = i*n+j
                self.graph[vertNum] = Node(vertNum)
                ptr = self.graph[vertNum]

                self.board[i][j] = boardNode(x+i*800/n, y+j*800/m, vertNum)

                if(j>0):
                    if(i<len(self.board)-1):
                        bottomLeft = (i+1)*n+j-1
                        ptr.adjLists = Edge(bottomLeft, ptr.adjLists, 1)
                    
                    leftVertex = i*n+j-1
                    ptr.adjLists = Edge(leftVertex, ptr.adjLists, 1)

                if(i<len(self.board)-1):
                    if(j<n-1):
                        bottomRight = (i+1)*n+j+1
                        ptr.adjLists = Edge(bottomRight, ptr.adjLists, 1)
                    
                    downVertex = (i+1)*n+j 
                    ptr.adjLists = Edge(downVertex, ptr.adjLists, 1)
                
                if(j<n-1):
                    if(i>0):
                        topRight = (i-1)*n+j+1
                        ptr.adjLists = Edge(topRight, ptr.adjLists, 1)
                    
                    rightVertex = i*n+j+1
                    ptr.adjLists = Edge(rightVertex, ptr.adjLists, 1)
                
                if(i>0):
                    if(j>0):
                        topLeft = (i-1)*n+j-1
                        ptr.adjLists = Edge(topLeft, ptr.adjLists, 1)
                    
                    upVertex = (i-1)*n+j
                    ptr.adjLists = Edge(upVertex, ptr.adjLists, 1)
                
    def resize(self, x, y, m, n):
        self.board = [[None]*m for i1 in range(n)]
        self.graph = [None]*(m*n)
 
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                vertNum = i*n+j
                self.graph[vertNum] = Node(vertNum)
                ptr = self.graph[vertNum]

                self.board[i][j] = boardNode(x+i*800/n, y+j*800/m, vertNum)

                if(j>0):
                    if(i<len(self.board)-1):
                        bottomLeft = (i+1)*n+j-1
                        ptr.adjLists = Edge(bottomLeft, ptr.adjLists, 1)
                    
                    leftVertex = i*n+j-1
                    ptr.adjLists = Edge(leftVertex, ptr.adjLists, 1)

                if(i<len(self.board)-1):
                    if(j<n-1):
                        bottomRight = (i+1)*n+j+1
                        ptr.adjLists = Edge(bottomRight, ptr.adjLists, 1)
                    
                    downVertex = (i+1)*n+j 
                    ptr.adjLists = Edge(downVertex, ptr.adjLists, 1)
                
                if(j<n-1):
                    if(i>0):
                        topRight = (i-1)*n+j+1
                        ptr.adjLists = Edge(topRight, ptr.adjLists, 1)
                    
                    rightVertex = i*n+j+1
                    ptr.adjLists = Edge(rightVertex, ptr.adjLists, 1)
                
                if(i>0):
                    if(j>0):
                        topLeft = (i-1)*n+j-1
                        ptr.adjLists = Edge(topLeft, ptr.adjLists, 1)
                    
                    upVertex = (i-1)*n+j
                    ptr.adjLists = Edge(upVertex, ptr.adjLists, 1)

    def astar(self, i, j, i_, j_):
        res = list()
        vist = list()

        destinationNode = j_*len(self.board[0]) + i_
        startingNode = j*len(self.board[0]) + i

        visited = [False]*len(self.graph)

        ptr = startingNode 

        heap = Heap()
        heap.insert(self.graph[ptr])
        self.graph[ptr].h = self.heuristic1(i,j,i_,j_)
        self.graph[ptr].f = self.graph[ptr].h
        self.graph[ptr].g = 0

        while(heap.size!=0): 
            ptr = heap.delete().vnum

            if(ptr==destinationNode):
                break
            
            visited[ptr] = True
            temp = list()

            if(ptr==destinationNode):
                res.append(destinationNode)
                break

            pt = self.graph[ptr].adjLists 
            
            while(pt!=None):
                if(pt.vnum == destinationNode):
                    break

                temp.append(pt.vnum)

                x = pt.vnum%len(self.board) 
                y = pt.vnum/len(self.board) 
                self.graph[pt.vnum].h = self.heuristic1(x,y,i_,j_)
                self.graph[pt.vnum].g = self.graph[ptr].g + pt.weight

                self.graph[pt.vnum].f = self.graph[pt.vnum].h + self.graph[pt.vnum].g

                if(visited[pt.vnum]):
                    pt = pt.next
                    continue

                visited[pt.vnum] = True
                heap.insert(self.graph[pt.vnum])

                pt = pt.next

            if(pt!=None and pt.vnum == destinationNode):
                break
            vist.append(temp)

        self.graph[destinationNode].f = 0
        self.graph[destinationNode].h = 0
        #BACKTRACKING 

        ptr = startingNode
        visited = [False]*len(self.graph)
        visited[ptr] = True

        while(ptr!=destinationNode):
            res.append(ptr)
            pt = self.graph[ptr].adjLists
            minPtr = pt


            while(pt!=None):
                if(visited[pt.vnum]):
                    pt = pt.next
                    continue 

                visited[pt.vnum] = True 

                if(self.graph[minPtr.vnum].f > self.graph[pt.vnum].f):
                    minPtr = pt

                pt = pt.next

            ptr = minPtr.vnum 

        res.append(destinationNode)
        return (res,vist)

    def dijkstra(self, i, j, i_, j_):
        res = list()
        vist = list()

        destinationNode = j_*len(self.board[0]) + i_
        startingNode = j*len(self.board[0]) + i

        visited = [False]*len(self.graph)

        ptr = startingNode 

        heap = Heap()
        heap.insert(self.graph[ptr])
        self.graph[ptr].h = self.heuristic2(i,j,i_,j_)
        self.graph[ptr].f = self.graph[ptr].h
        self.graph[ptr].g = 0

        while(heap.size!=0): 
            ptr = heap.delete().vnum

            if(ptr==destinationNode):
                break
            
            visited[ptr] = True
            temp = list()

            if(ptr==destinationNode):
                res.append(destinationNode)
                break

            pt = self.graph[ptr].adjLists 
            
            while(pt!=None):
                if(pt.vnum == destinationNode):
                    break

                temp.append(pt.vnum)

                x = pt.vnum%len(self.board) 
                y = pt.vnum/len(self.board) 
                self.graph[pt.vnum].h = self.heuristic2(x,y,i_,j_)
                self.graph[pt.vnum].g = min(self.graph[pt.vnum].g, self.graph[ptr].g + pt.weight)

                self.graph[pt.vnum].f = self.graph[pt.vnum].h + self.graph[pt.vnum].g

                if(visited[pt.vnum]):
                    pt = pt.next
                    continue

                visited[pt.vnum] = True
                heap.insert(self.graph[pt.vnum])

                pt = pt.next

            if(pt!=None and pt.vnum == destinationNode):
                break
            vist.append(temp)

        self.graph[destinationNode].f = 0
        self.graph[destinationNode].h = 0

        #BACKTRACKING 

        ptr = destinationNode
        visited = [False]*len(self.graph)
        visited[ptr] = True

        while(ptr!=startingNode):
            res.insert(0,ptr)
            pt = self.graph[ptr].adjLists
            minPtr = pt

            while(pt!=None):
                if(visited[pt.vnum]):
                    pt = pt.next
                    continue 

                visited[pt.vnum] = True 

                if(self.graph[minPtr.vnum].f > self.graph[pt.vnum].f):
                    minPtr = pt

                pt = pt.next

            ptr = minPtr.vnum 

        res.insert(0,startingNode)
        return (res,vist)

    def heuristic1(self, i, j, i_, j_):
        return (i_-i)*(i_-i) + (j_-j)*(j_-j)
    
    def heuristic2(self, i, j, i_, j_):
        return 0
    
    def unweightedPathFindingAlgorithm(self,i, j, i_, j_):
        res = list()
        vist = list()

        destinationNode = j_*len(self.board[0]) + i_
        startingNode = j*len(self.board[0]) + i

        dist = [9999999]*len(self.graph)
        visited = [False]*len(self.graph)

        dist[destinationNode] = 0
        self.fillDistances(destinationNode, dist, visited)

        for i in range(len(self.graph)-1):
            pt = self.graph[i].adjLists

            while(pt!=None):
                temp = list()
                temp.append(pt.vnum)
                pt = pt.next
            
            vist.append(temp)

        ptr = startingNode
        res.append(startingNode)

        visited = [False]*len(self.graph)
        visited[startingNode] = True 

        while(ptr!=destinationNode):
            temp = list()
            if(dist[ptr] == 9999999):
                return (res, vist)

            min = 9999999
            nextShortest = 0

            e = self.graph[ptr].adjLists

            
            while(e!=None):
                if(visited[e.vnum]==True):
                    pass
                
                if(dist[e.vnum]<min):
                    min = dist[e.vnum]
                    nextShortest = e.vnum

                e=e.next

            visited[nextShortest] = True
            ptr = nextShortest 
            res.append(nextShortest)

        res.append(destinationNode)

        return (res,vist)

    # Getting the distance from starting node to every node in the graph
    def fillDistances(self, startingNode, dist, visited):
        visited[startingNode] = True

        e = self.graph[startingNode].adjLists
        while(e!=None):
            if(1+dist[startingNode]<dist[e.vnum]):
                dist[e.vnum] = 1+dist[startingNode]
                self.fillDistances(e.vnum, dist, visited)

            e=e.next
        
        e = self.graph[startingNode].adjLists

        while(e!=None):
            if(visited[e.vnum] != True):
                self.fillDistances(e.vnum, dist, visited)
            e = e.next

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

class createCanvas():
    def __init__(self, root):
        self.root = root
        self.myframe = Frame(self.root)
        self.myframe.pack(fill=BOTH, expand=YES)
        self.mycanvas = ResizingCanvas(self.myframe,width=1002, height=802, bg="teal", highlightthickness=0)
        self.mycanvas.pack(fill=BOTH, expand=YES)

    def draw_cell(self, x,y, size_x, size_y, color):
        box = self.mycanvas.create_rectangle(x, y, (x+size_x), (y+size_y), fill=color, tags = "grid")
        return box

    
    def drawGrid(self, board):
        w = self.mycanvas.width
        h = self.mycanvas.height

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].box = self.draw_cell(board[i][j].x*w/1002, board[i][j].y*h/802, 800/len(board)*w/1002, 800/len(board[0])*h/802, "white")
    
    def showWindow(self):
        self.root.mainloop()
    
    def getCanvas(self):
        return self.mycanvas

    def highlightCell(self, board, i, j, color):  
        if(self.mycanvas.itemcget(board[int(i)][int(j)].box, 'fill') == "white" or self.mycanvas.itemcget(board[int(i)][int(j)].box, 'fill') == "blue" or self.mycanvas.itemcget(board[int(i)][int(j)].box, 'fill') == "gray"):
            if(self.mycanvas.itemcget(board[int(i)][int(j)].box, 'fill') == "gray" and color == "blue"):
                return
            self.mycanvas.itemconfig(board[int(i)][int(j)].box, fill = color)
        self.mycanvas.update()
    

def main():
    root = Tk()
    canvas = createCanvas(root)

    board = grid(200,0,30,30)

    canvas.drawGrid(board.board)
    can = canvas.getCanvas()

    title = Label(root, text="Path Finding Visualizer", bg = "teal",  font = tkFont.Font(family="Times New Roman", size=15))
    can.create_window(100,20,window=title)

    def resizeGrid():
        m = int(n.get())

        if(m>59):
            error_message.config(text="Grid Size has a limit of 59x59 to avoid recursion errors")
            m=59
        else:
            error_message.config(text="")

        board.resize(200,0,m,m)
        can.delete("grid")
        canvas.drawGrid(board.board)

    def highlightShortestPath():
        source_coor = source.get()
        source_x = 0
        source_y = 0

        if(source_coor[0]!='(' or source_coor[len(source_coor)-1]!=')'):
            error_message.config(text = "Invalid Coordinate Input")
            return

        index = 0
        for i in range(len(source_coor)):
            if(source_coor[i] =='('):
                continue
            elif(source_coor[i] == ','):
                index = i+1
                break 
            else:
                source_x = 10*source_x + int(source_coor[i])
        
        if(index == len(source_coor)-1):
            error_message.config(text = "Invalid Coordinate Input")
            return

        for i in range(index, len(source_coor)):
            if(source_coor[i] == ')'):
                break
            else:
                source_y = source_y*10 + int(source_coor[i])
        
        dest_coor = destination.get()
        dest_x = 0
        dest_y = 0

        if(dest_coor[0]!='(' or dest_coor[len(dest_coor)-1]!=')'):
            error_message.config(text = "Invalid Coordinate Input")
            return

        index = 0
        for i in range(len(dest_coor)):
            if(dest_coor[i] =='('):
                continue
            elif(dest_coor[i] == ','):
                index = i+1
                break 
            else:
                dest_x = 10*dest_x + int(dest_coor[i])
        
        if(index == len(dest_coor)-1):
            error_message.config(text = "Invalid Coordinate Input")
            return

        for i in range(index, len(dest_coor)):
            if(dest_coor[i] == ')'):
                break
            else:
                dest_y = dest_y*10 + int(dest_coor[i])

        if(source_x<0 or source_x>len(board.board) or source_y<0 or source_y>len(board.board) or dest_x<0 or dest_x>len(board.board) or dest_y<0 or dest_y>len(board.board)):
            error_message.config(text="Coordinates are not valid (Out of Bounds Exception)")
            return

        
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if(can.itemcget(board.board[int(i)][int(j)].box, 'fill') != "gray"):
                    can.itemconfig(board.board[int(i)][int(j)].box, fill = "white")
        
        if(can.itemcget(board.board[int(source_x)][int(source_y)].box, 'fill') == "gray"):
            error_message.config(text = "Source Node is blocked")
            return

        if(can.itemcget(board.board[int(dest_x)][int(dest_x)].box, 'fill') == "gray"):
            error_message.config(text= "Destination Node is blocked")
            return 

        canvas.highlightCell(board.board, dest_x, dest_y, "black")
        canvas.highlightCell(board.board, source_x, source_y, "black")

        if(variable.get() == "A*"):
            pack = board.astar(source_y, source_x, dest_y, dest_x)
        elif(variable.get() == "DFS"):
            pack = board.unweightedPathFindingAlgorithm(source_y, source_x, dest_y, dest_x)
        else:
            pack = board.dijkstra(source_y, source_x, dest_y, dest_x)


        path = pack[0]
        vist = pack[1]

        if(len(path) <= 1):
            error_message.config(text="There is no possible path")
            return
        else:
            error_message.config(text="")

        while(len(vist)>0):
            if(len(vist)>0):
                for item in vist[len(vist)-1]:
                    a = item/len(board.board)
                    b = item%len(board.board)
                    if(can.itemcget(board.board[int(i)][int(j)].box, 'fill') != "gray"):
                        root.after(0, canvas.highlightCell(board.board, a, b, "blue"))
            
                vist.remove(vist[len(vist)-1])

        while(len(path)>0):
            x = path[0]/len(board.board)
            y = path[0]%len(board.board)

            root.after(100,canvas.highlightCell(board.board, x, y, "red"))

            path.remove(path[0])
    
    def setWall(x, y):
        if(x>=0 and y>=0):
            if(can.itemcget(board.board[int(x)][int(y)].box, 'fill') == "white"):
                canvas.highlightCell(board.board, int(x), int(y), "gray")

                vert = int(int(x)*len(board.board[0])+int(y))
                ptr = board.graph[vert].adjLists

                while(ptr != None):
                    pt = board.graph[ptr.vnum].adjLists
                    if(pt.vnum == vert):
                        board.graph[ptr.vnum].adjLists = pt.next
                    else:
                        while(pt.next != None):
                            if(pt.next.vnum == vert):
                                pt.next = pt.next.next 
                                break
                            
                            pt = pt.next 
                        

                    ptr = ptr.next
            else:
                canvas.highlightCell(board.board, int(x), int(y), "white")

                vert = int(x)*len(board.board[0])+int(y)
                ptr = board.graph[vert].adjLists

                while(ptr != None):
                    board.graph[ptr.vnum].adjLists = Edge(vert, board.graph[ptr.vnum].adjLists, 1)
                    ptr = ptr.next
    
    def getorigin(eventorigin):
        x = eventorigin.x
        y = eventorigin.y

        w = can.width 
        h = can.height 

        x = ((x-(200*w/1002))/(802*w/1002)*len(board.board))
        y = y/h*len(board.board)

        setWall(x,y)


    def createMaze():
        resizeGrid()

        for i in range(int(int(len(board.board))*int(len(board.board))/5)):
            x = int(random()*len(board.board))
            y = int(random()*len(board.board))

            setWall(x,y)

    def setWeights():
        resizeGrid()

        for i in range(int(int(len(board.board))*int(len(board.board))/3)):
            x = int(random()*len(board.board))
            y = int(random()*len(board.board))

            setWeight(x,y)

    def setWeight(x, y):
        node = x+y*len(board.board)
        ptr = board.graph[node].adjLists

        while(ptr!=None):
            ptr.weight = int(random()*100)
            ptr = ptr.next

    root.bind("<Button 1>",getorigin)

    n = Entry(root, width=13)
    n.insert(6,"30")
    n.pack()
    can.create_window(100,100,window=n)

    button = Button(text="Generate Grid", command=resizeGrid)
    button.pack()
    can.create_window(100, 125, window = button)

    source = Entry(root, width=13)
    source.insert(6,"(0,0)")
    source.pack()
    can.create_window(100,200,window=source)
        

    destination = Entry(root, width=13)
    destination.insert(6,"(29,29)")
    destination.pack()
    can.create_window(100,225,window=destination)
            
    OptionList = [
        "DFS",
        "A*",
        "Dijkstra",
    ] 

    variable = StringVar(can)
    variable.set(OptionList[0])

    dropDown = OptionMenu(can, variable, *OptionList)
    dropDown.config(width=5)
    dropDown.pack()
    can.create_window(100,300,window=dropDown)

    button2 = Button(text="Find Shortest Path", command=highlightShortestPath)
    button2.pack()
    can.create_window(100, 350, window = button2)

    button3 = Button(text="Create Maze", command=createMaze)
    button3.pack()
    can.create_window(100, 400, window = button3)


    error_message = Label(root, text="" , fg = "black", bg = "teal",  font = tkFont.Font(family="Times New Roman", size=15), wraplength=100)
    can.create_window(100,700,window=error_message)

    canvas.showWindow()


if __name__ == "__main__":
    main()
