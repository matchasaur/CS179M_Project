class Container:
    def __init__(self, y, x, weight, name):
        self.y = y-1
        self.x = x-1
        self.weight = weight
        self.name = name
        keyPair = (y,x)
        
def displayCargo(shipcargo):
    for i in shipcargo:
        print(i.name.ljust(5), ' ',end='')
        if (i.x == 5):
            print('\n')
            

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
        # print(y,x)
        
        tempContainer = Container(y,x,weight,name)
        shipcargo.append(tempContainer)
        
    displayCargo(shipcargo)
    
    file.close()