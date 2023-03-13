from queue import PriorityQueue


#Class declaration/definitions
class Node:
    #Creates state/node- to be expanded by moving cargo
    def __init__(self, shipcargo):
        self.currCargo = shipcargo
        self.balanceScore = self.calculateBalance(shipcargo)
    
    def calculateBalance(self, currCargo):
        leftWeight = 0
        rightWeight = 0
        
        for i in currCargo:
            if (i.x < 3):
                leftWeight += i.weight
            else:
                rightWeight += i.weight
        return min(leftWeight,rightWeight)/max(leftWeight,rightWeight)

class Container:
    def __init__(self, y, x, weight, name):
        self.y = y-1
        self.x = x-1
        self.weight = weight
        self.name = name
        keyPair = (y,x)



#Meat and Potatoes
def search(Graph, ):
    pass



#Menial functions...
def displayCargo(shipcargo):
    for i in shipcargo:
        print(i.name.ljust(5), ' ',end='')
        if (i.x == 5):
            print('\n')
        
def calculateWeight(shipcargo, side):
     pass   

if __name__ == "__main__":
    #First things first, we need to populate a list of lists with the information of the manifest
    
    file = open('model/balanceTest1.txt', 'r')
    
    shipcargo = []
    
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue
        
        y, x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        name = parts[2]
        
        y = int(y)
        x = int(x)
        weight = int(weight)
        # print(y,x)
        
        tempContainer = Container(y,x,weight,name)
        shipcargo.append(tempContainer)
        
    displayCargo(shipcargo)
    
    testNode = Node(shipcargo)
    print(testNode.balanceScore)
    
    file.close()