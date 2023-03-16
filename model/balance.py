from queue import PriorityQueue
import heapq
import copy

#PriorityQueue implementation
class PriorityQueue:
    def __init__(self):
        self.nodes = []
        
    def insert(self, currNode, priority):
        heapq.heappush(self.nodes, (priority, currNode))
        
    def pop(self):
        return heapq.heappop(self.nodes)[1]
    
    def isEmpty(self):
        return len(self.nodes) == 0
    

#Class declaration/definitions
class Node:
    #Creates state/node- to be expanded by moving cargo
    def __init__(self, shipcargo):
        self.cargo = shipcargo
        self.balanceScore = self.calculateBalance(shipcargo)
        self.cost = 0
        
    def __lt__(self, other):
        Fn = self.cost + self.balanceScore
        Pn = other.cost + other.balanceScore
        if (Fn == Pn): return self.cost < other.cost
        else:
            return Fn < Pn  
        
    def updateBalance(self):
        self.balanceScore = self.calculateBalance(self.cargo)
    
    def calculateBalance(self, cargo):
        leftWeight = 0
        rightWeight = 0
        
        for i in cargo:
            for j in i:
                if (j.x < 3):
                    leftWeight += j.weight
                else:
                    rightWeight += j.weight
        score = min(leftWeight,rightWeight)/max(leftWeight,rightWeight) 
        #//////////////////////////// DEBUG MESSAGE ///////////////////////////
        print(score)
        return score
    
    def columnNotEmpty(self, column):
        #Checks if any containers in the column are not named UNUSED
        for i in range(2):
            if(self.cargo[i][column].name != 'UNUSED'):
                return i,column
        return -1,-1
    
    def nearestContainer(self, column):
        for i in range(2):
            if(self.cargo[i][column].name != 'UNUSED'):
                return i-1, column
        return i, column
    
class Container:
    def __init__(self, y, x, weight, name):
        self.y = y-1
        self.x = x-1
        self.weight = weight
        self.name = name
        keyPair = (y,x)
        
    def clear(self):
        self.weight = 0
        self.name = 'UNUSED'
        
class cargoHash():
    def __init__(self):
        self.hashtable = {}
        
    def hashFunction(self, cargo):
        hashValue = 0
        for i in range(2):
            for j in range(6):
                hashValue += cargo[i][j].weight*(i+1)*(j+1)
        #////////////////////////////DEBUG MESSAGE////////////////////////////////
        #print("func::cargoHash(): hashvalue: ", hashValue)
        return hashValue

    def insertItem(self, cargo):
        index = self.hashFunction(cargo)
        self.hashtable[index] = cargo
        
    def isRepeated(self, cargo):
        index = self.hashFunction(cargo)
        if (index in self.hashtable.keys()):
            return True
        return False

#Meat and Potatoes
def search(start):
    #All visited nodes are placed into a set
    setOfVisitedNodes = cargoHash()
    setOfVisitedNodes.insertItem(start.cargo)
    queue = PriorityQueue()
    queue.insert(start, start.balanceScore + start.cost)
    parent = {}
    parent[start] = None

    
    while not queue.isEmpty():
        #Grab the node at the top of the queue
        currNode = queue.pop()
        displayCargo(currNode.cargo)
        print()
        #If the node is admissible, we can sail
        if isAdmissible(currNode):
            print("Yo we found the goal!!!!!!!")
            print(currNode.balanceScore, ', ', currNode.cost)
            displayCargo(currNode.cargo)
            return currNode

        #Otherwise, we need to expand the nodes
        expandNode(currNode, queue, setOfVisitedNodes, parent)

    print("Yo we didn't find the goal...")

def expandNode(nodeToExpand, queue, setOfVisitedNodes, parent):
    #We cycle the crane over each column, left to right
    for i in range(6):
        #Find the columns that are not empty
        if((-1,-1) != nodeToExpand.columnNotEmpty(i)):
            #Expand this container by moving it to a valid position
            coordinates = nodeToExpand.columnNotEmpty(i)
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            #print("func::expandNode(): ", coordinates)
            #print("func::expandNode(): Shifting container: ", nodeToExpand.cargo[coordinates[0]][coordinates[1]].name)
            expandHelper(nodeToExpand, coordinates, queue, setOfVisitedNodes, parent)
            
#helper function
def expandHelper(node, coordinates, queue, setOfVisitedNodes, parent):
    #For each column, find a valid cell to move the container to
    for i in range(6):
        y, x = node.nearestContainer(i)
        #////////////////////////////DEBUG MESSAGE////////////////////////////////
        #print("func::expandHelper(): We are looking at location:", y, ' ', x)
        if (i != coordinates[1] and y != -1):
            tempNode = copy.deepcopy(node)
            tempNode.cargo[y][i].weight = node.cargo[coordinates[0]][coordinates[1]].weight
            tempNode.cargo[y][i].name = node.cargo[coordinates[0]][coordinates[1]].name
            tempNode.cargo[coordinates[0]][coordinates[1]].clear()
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            displayCargo(tempNode.cargo)
            print()
            if not setOfVisitedNodes.isRepeated(tempNode.cargo):
                priority = tempNode.cost + 1 + tempNode.calculateBalance(tempNode.cargo)
                tempNode.cost =+ 1
                tempNode.updateBalance()
                setOfVisitedNodes.insertItem(tempNode.cargo)
                parent[tempNode] = node
                queue.insert(tempNode, priority)
        else:
            pass
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            #print("func::expandHelper(): Skipping cell...")
            

def isAdmissible(node):
    if (node.balanceScore > 0.9):
        return True 

#Menial functions...
def displayCargo(shipcargo):
    for i in shipcargo:
        for j in i:
            print(j.name.center(12), ' ', end='')
        print('')

if __name__ == "__main__":
    #First things first, we need to populate a list of lists with the information of the manifest
    
    file = open('model/balanceTest1.txt', 'r')
    
    shipcargo = [[0] * 6 for i in range(2)]
    
    
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue
        
        y, x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        name = parts[2]
        
        y = int(y) - 1
        x = int(x) - 1
        weight = int(weight)
        # print(y,x)
        
        tempContainer = Container(y,x,weight,name)
        shipcargo[y][x] = tempContainer
        
    displayCargo(shipcargo)
    
    testNode = Node(shipcargo)
    
    print("Attempting to balance...")
    search(testNode)
    # print(testNode.balanceScore)
    # print(testNode.columnNotEmpty(5))
    
    file.close()