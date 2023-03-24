from queue import PriorityQueue
import heapq
import copy
import timeit

#PriorityQueue implementation
class PriorityQueue:
    def __init__(self):
        self.nodes = []
        heapq.heapify(self.nodes)
        
    # def insert(self, currNode):
    #     heapq.heappush(self.nodes,currNode)
        
    def insert(self, currNode, priority):
        heapq.heappush(self.nodes, (priority, currNode))    
    
    def pop(self):
        heapq.heapify(self.nodes)
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
        self.old = ''
        self.new = ''
        
    def __lt__(self, other):
        Fn = self.cost + (1 - self.balanceScore)
        Pn = other.cost + (1 - other.balanceScore)
        if (Fn == Pn): return self.cost < other.cost
        else:
            return Fn < Pn  
        
    def updateBalance(self):
        self.balanceScore = self.calculateBalance(self.cargo)
        
    def updateCost(self, time):
        self.cost = time
    
    def calculateBalance(self, cargo):
        leftWeight = 0
        rightWeight = 0
        
        for i in range(rows):
            for j in range(columns):
                if (j < columns/2):
                    leftWeight += cargo[i][j].weight
                else:
                    rightWeight += cargo[i][j].weight
        score = min(leftWeight,rightWeight)/max(leftWeight,rightWeight) 
        #//////////////////////////// DEBUG MESSAGE ///////////////////////////
        #print(score)
        return score
    
    def columnNotEmpty(self, column):
        #Checks if any containers in the column are not named UNUSED
        for i in reversed(range(rows)):
            if(self.cargo[i][column].name != 'UNUSED' and self.cargo[i][column].name != 'NAN'):
                return i,column
        return -1,-1
    
    def nearestContainer(self, column):
        for i in reversed(range(rows)):
            if(self.cargo[i][column].name != 'UNUSED' and self.cargo[i][column].name != 'NAN'):
                return i+1, column
            elif(self.cargo[i][column].name == 'NAN'):
                return i+1, column
        return i, column
    
class Container:
    def __init__(self, y, x, weight, name):
        self.y = y
        self.x = x
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
        for i in reversed(range(rows)):
            for j in range(columns):
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

def writeToManifest(node):
    final_manifest = open('final_manifest.txt', 'w')
    cargo = node.cargo
    for i in cargo:
        for j in i:
            y = str(j.y+1).zfill(2)
            x = str(j.x+1).zfill(2)
            weight = str(j.weight).zfill(5)
            name = j.name
            
            final_manifest.write(str(f"[{y},{x}], {{{weight}}}, {name}\n"))
            
    print("Manifest finalized.")
    final_manifest.close()

def writeInstructions(node, parent):
    instructions = ''
    instructions = str(writeInstructionsHelp(node, parent, instructions))
    balanceOperations = open('balance_operations.txt', 'w')
    balanceOperations.write(str(instructions))
    balanceOperations.close()
    
    
def writeInstructionsHelp(node, parent, instructions):
    #base case
    if (parent[node] == None):
        print("Found the root\n")
        return ''
    print("recurssion")
    instructions += str(writeInstructionsHelp(parent[node], parent, instructions))
    oldY = str(node.old[0])
    oldX = str(node.old[1])
    newY = str(node.new[0])
    newX = str(node.new[1])
    line = str(f"({oldY}, {oldX}),({newY}, {newX})\n")
    instructions += line
    return instructions
    

#Meat and Potatoes
def search(start, listByWeight):
    #All visited nodes are placed into a set
    setOfVisitedNodes = cargoHash()
    setOfVisitedNodes.insertItem(start.cargo)
    queue = PriorityQueue()
    queue.insert(start, (1-start.balanceScore) + start.cost)
    # queue.insert(start)
    parent = {}
    parent[start] = None

    
    while not queue.isEmpty():
        #Grab the node at the top of the queue
        currNode = queue.pop()
        # ///////////////////// DEBUG MESSAGE /////////////////////////
        # print("func::search(): Observing this cargo: ")
        # displayCargo(currNode.cargo)
        currNode.updateBalance()
        # print("Balance Score: ", currNode.balanceScore)
        # print()
        #If the node is admissible, we can sail
        if isAdmissible(currNode):
            # print("Yo we found the goal!!!!!!!")
            print("Found admissible configuration:")
            print("balanceScore: ", currNode.balanceScore, ', ', 'Estimated Time: ', currNode.cost*4, 'minutes')
            displayCargo(currNode.cargo)
            writeInstructions(currNode, parent)
            writeToManifest(currNode)
            return currNode

        #Otherwise, we need to expand the nodes
        expandNode(currNode, queue, setOfVisitedNodes, parent)

    print("Yo we didn't find the goal...")
    SIFT(start, listByWeight)
    

def SIFT(start, listByWeight):
    print("Starting SIFT function:")
    #First construct goal state
    copyStart = copy.deepcopy(start)
    goalState = constructGoal(start, listByWeight)
    copyStart.cost = updateCost(copyStart, listByWeight)
    # print("cost: ", copyStart.cost)
    #Then run manhattan distance on goal
    setOfVisitedNodes = cargoHash()
    setOfVisitedNodes.insertItem(copyStart.cargo)
    queue = PriorityQueue()
    queue.insert(copyStart, (1-copyStart.balanceScore) + copyStart.cost)
    # queue.insert(start)
    parent = {}
    parent[copyStart] = None

    
    while not queue.isEmpty():
        #Grab the node at the top of the queue
        currNode = queue.pop()
        # ///////////////////// DEBUG MESSAGE /////////////////////////
        # print("func::search(): Observing this cargo: ")
        # displayCargo(currNode.cargo)
        # print("Cost: ", currNode.cost)
        # currNode.updateBalance()
        # print("Balance Score: ", currNode.balanceScore)
        # print()
        #If the node is admissible, we can sail
        if (currNode.cost == 0):
            print("Constructed SIFT admissible configuration:")
            currNode.updateBalance()
            print("balanceScore: ", currNode.balanceScore, ', ', 'Estimated Time: ', currNode.cost*4, 'minutes')
            displayCargo(currNode.cargo)
            writeInstructions(currNode, parent)
            writeToManifest(currNode)
            return currNode

        #Otherwise, we need to expand the nodes
        expandSIFTNode(currNode, queue, setOfVisitedNodes, parent, listByWeight)
    

def constructGoal(start, listByWeight):
    goalCargo = copy.deepcopy(start)
    for i in range(8):
        for j in range(12):
            if(goalCargo.cargo[i][j].name != 'NAN'):
                goalCargo.cargo[i][j].clear()
    
    #Populate
    leftIndex = 5
    rightIndex = 6
    rowIndex = 0
    for j in range(len(listByWeight)):
        #print("Inserting ", listByWeight[j].name)
        if(leftIndex == 12 and rightIndex == -1):
            rowIndex+=1
            leftIndex = 5
            rightIndex = 6
        if (j%2 == 0):
            if (goalCargo.cargo[rowIndex][rightIndex].name == 'NAN'):
                break
            # print("Inserting Right...")
            listByWeight[j].y = rowIndex
            listByWeight[j].x = rightIndex
            #print(listByWeight[j].name,':',listByWeight[j].y,listByWeight[j].x)
            goalCargo.cargo[rowIndex][rightIndex] = listByWeight[j]
            rightIndex += 1
        else:
            if (goalCargo.cargo[rowIndex][leftIndex].name == 'NAN'):
                break
            #print("Inserting Left...")
            listByWeight[j].y = rowIndex
            listByWeight[j].x = leftIndex
            #print(listByWeight[j].name,':',listByWeight[j].y,listByWeight[j].x)
            goalCargo.cargo[rowIndex][leftIndex] = listByWeight[j]
            leftIndex -= 1

    displayCargo(goalCargo.cargo)
    return goalCargo
    
def manhatDist(x1, x2, y1, y2):
    # print(x1, x2, y1, y2)
    return (abs(x2-x1) + abs(y2-y1))


def expandNode(nodeToExpand, queue, setOfVisitedNodes, parent):
    #We cycle the crane over each column, left to right
    for i in range(columns):
        #Find the columns that are not empty
        if((-1,-1) != nodeToExpand.columnNotEmpty(i)):
            #Expand this container by moving it to a valid position
            coordinates = nodeToExpand.columnNotEmpty(i)
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            # print("func::expandNode(): ", coordinates)
            # print("func::expandNode(): Shifting container: ", nodeToExpand.cargo[coordinates[0]][coordinates[1]].name)
            expandHelper(nodeToExpand, coordinates, queue, setOfVisitedNodes, parent)
            
#helper function
def expandHelper(node, coordinates, queue, setOfVisitedNodes, parent):
    #For each column, find a valid cell to move the container to
    for i in range(columns):
        y, x = node.nearestContainer(i)
        #////////////////////////////DEBUG MESSAGE////////////////////////////////
        # print("func::expandHelper(): We are looking at location:", y, ' ', x)
        if (i != coordinates[1] and y != rows):
            tempNode = copy.deepcopy(node)
            tempNode.cargo[y][i].weight = node.cargo[coordinates[0]][coordinates[1]].weight
            tempNode.cargo[y][i].name = node.cargo[coordinates[0]][coordinates[1]].name
            tempNode.cargo[coordinates[0]][coordinates[1]].clear()
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            # displayCargo(tempNode.cargo); print()
            if not setOfVisitedNodes.isRepeated(tempNode.cargo):
                tempNode.old = coordinates
                tempNode.new = (y,x)
                newCost = manhatDist(coordinates[0], x, coordinates[1], y) + node.cost
                tempNode.updateCost(newCost)
                priority = newCost + (1 - tempNode.calculateBalance(tempNode.cargo))
                tempNode.updateBalance()
                setOfVisitedNodes.insertItem(tempNode.cargo)
                parent[tempNode] = node
                queue.insert(tempNode, priority)
        else:
            pass
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            #print("func::expandHelper(): Skipping cell...")
            
def expandSIFTNode(nodeToExpand, queue, setOfVisitedNodes, parent, listByWeight):
    #We cycle the crane over each column, left to right
    for i in range(columns):
        #Find the columns that are not empty
        if((-1,-1) != nodeToExpand.columnNotEmpty(i)):
            #Expand this container by moving it to a valid position
            coordinates = nodeToExpand.columnNotEmpty(i)
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            # print("func::expandNode(): ", coordinates)
            # print("func::expandNode(): Shifting container: ", nodeToExpand.cargo[coordinates[0]][coordinates[1]].name)
            expandSIFTHelper(nodeToExpand, coordinates, queue, setOfVisitedNodes, parent, listByWeight)
            
def expandSIFTHelper(node, coordinates, queue, setOfVisitedNodes, parent, listByWeight):
    #For each column, find a valid cell to move the container to
    for i in range(columns):
        y, x = node.nearestContainer(i)
        #////////////////////////////DEBUG MESSAGE////////////////////////////////
        # print("func::expandHelper(): We are looking at location:", y, ' ', x)
        if (i != coordinates[1] and y != rows):
            tempNode = copy.deepcopy(node)
            tempNode.cargo[y][i].weight = node.cargo[coordinates[0]][coordinates[1]].weight
            tempNode.cargo[y][i].name = node.cargo[coordinates[0]][coordinates[1]].name
            tempNode.cargo[coordinates[0]][coordinates[1]].clear()
            #////////////////////////////DEBUG MESSAGE////////////////////////////////
            # displayCargo(tempNode.cargo); print()
            if not setOfVisitedNodes.isRepeated(tempNode.cargo):
                newCost = updateCost(tempNode, listByWeight)
                tempNode.updateCost(newCost)
                #////////////////////////////DEBUG MESSAGE////////////////////////////////
                # print("Adding this state to the queue:")
                # displayCargo(tempNode.cargo)
                # print("Cost: ", newCost)
                tempNode.old = coordinates
                tempNode.new = (y,x)
                priority = newCost
                tempNode.balanceScore = 0
                setOfVisitedNodes.insertItem(tempNode.cargo)
                parent[tempNode] = node
                queue.insert(tempNode, priority)

                
def updateCost(node, listByWeight):
    # print("\tUpdating cost...")
    total = 0
    # displayCargo(node.cargo)
    for i in listByWeight:
        # print("Searching for: ", i.name)
        for j in range(12):
            for k in reversed(range(8)):
                if (node.cargo[k][j].name == 'NAN'):
                    break
                if (i.name == node.cargo[k][j].name):
                    # print("Found ", i.name)
                    total += manhatDist(i.x, node.cargo[k][j].x, i.y, node.cargo[k][j].y)
                    # print("Total: ", total)
    return total

def isAdmissible(node):
    if (node.balanceScore > 0.9):
        return True 

#Menial functions...
def displayCargo(shipcargo):
    for i in reversed(shipcargo):
        for j in (i):
            print(j.name.center(12), ' ', end='')
        print('')
        
def displayCoord(shipcargo):
    for i in reversed(shipcargo):
        for j in (i):
            print('(', j.y, ',', j.x, ')', end='')
        print('')
        
def displayWeight(shipcargo):
    for i in reversed(shipcargo):
        for j in reversed(i):
            print(str(j.weight).center(12), ' ', end='')
        print('')

def weightFunc(container):
    return container.weight

if __name__ == "__main__":
    #First things first, we need to populate a list of lists with the information of the manifest
    global columns, rows 
    columns = 12
    rows = 8
    
    
    
    file = open('ShipCase1.txt', 'r')
    
    shipcargo = [[0] * columns for i in range(rows)]
    listByWeight = []
    
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
        if(tempContainer.name != 'UNUSED' and tempContainer.name != 'NAN'):
            listByWeight.append(tempContainer)
        
    listByWeight.sort(key=weightFunc, reverse=True)
    displayCargo(shipcargo)
    
    testNode = Node(shipcargo)
    
    print("Attempting to balance...")
    starttime = timeit.default_timer()
    search(testNode, listByWeight)
    stoptime = timeit.default_timer()
    execution_time = stoptime - starttime
    print("Program ran in ", "{0:.4f}".format(execution_time), " seconds.")
    # print(testNode.balanceScore)
    # print(testNode.columnNotEmpty(5))
    
    file.close()