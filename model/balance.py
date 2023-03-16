from queue import PriorityQueue
import heapq

#PriorityQueue implementation
class PriorityQueue:
    def __init__(self):
        self.nodes = []
        
    def insert(self, Node, priority):
        heapq.heappush(self.nodes, (priority, Node))
        
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    def isEmpty(self):
        return len(self.nodes) == 0

#Class declaration/definitions
class Node:
    #Creates state/node- to be expanded by moving cargo
    def __init__(self, shipcargo):
        self.currCargo = shipcargo
        self.balanceScore = self.calculateBalance(shipcargo)
        self.cost = 0
    
    def calculateBalance(self, currCargo):
        leftWeight = 0
        rightWeight = 0
        
        for i in currCargo:
            for j in i:
                if (j.x < 3):
                    leftWeight += j.weight
                else:
                    rightWeight += j.weight
        return min(leftWeight,rightWeight)/max(leftWeight,rightWeight)
    
    def columnNotEmpty(self, column):
        for i in self.currCargo:
            if (i.x == column & i.name != 'UNUSED'):
                return True
        return False

class Container:
    def __init__(self, y, x, weight, name):
        self.y = y-1
        self.x = x-1
        self.weight = weight
        self.name = name
        keyPair = (y,x)



#Meat and Potatoes
# def search(start):
#     #All visited nodes are placed into a set
#     setOfVisitedNodes = {}
    
#     queue = PriorityQueue()
#     queue.insert(start, start.balanceScore)
#     parent = {}
#     cost_so_far = {}
#     parent[start] = None
#     cost_so_far[start] = 0
    
#     while not queue.isEmpty():
#         #Grab the node at the top of the queue
#         currNode = queue.pop()
        
#         #If the node is admissible, we can sail
#         if isAdmissible(currNode):
#             return currNode

#         #Otherwise, we need to expand the nodes
#         expandedNodes = []
        


# def expandNode(expandNode, expandedNodes):
#     #We cycle the crane over each column, left to right
#     for i in 6:
#         #Find the columns that are not empty
#         if(expandNode.isNotEmpty(i)):
#             #Move container
#             tempContainer 

# def isAdmissible(node):
#     if (node.balanceScore >= 0.9):
#         return True 

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
    print(testNode.balanceScore)
    
    file.close()