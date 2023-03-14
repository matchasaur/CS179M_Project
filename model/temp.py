def load(tuples):
    pass

############## EMPTY CELL CHECK #####################

def container_above(tuples, target):
    y = int(target[0]) + 1
    x = int(target[1])
    for i in range(len(tuples)):
        if int(tuples[i][0]) == y and int(tuples[i][1]) == x:
            if tuples[i][3] == "UNUSED":
                print("No container above target\n")
                return False
            else:
                print("Container above target\n");
                return True
            break

    print("Couldn't find container")
    return True

def container_left(tuples, target):
    y = int(target[0])
    x = int(target[1]) - 1
    if x < 0:
        print("Container at x = 0")
        exit
    for i in range(len(tuples)):
        if int(tuples[i][0]) == y and int(tuples[i][1]) == x:
            if tuples[i][3] == "UNUSED":
                print("No container left of target\n")
                return False
            else:
                print("Container left of target\n")
                return True
            break
    print("Couldn't find container\n")
    return True


############### OPERATIONS #####################


def move_up(tuples, file, target):
    if not container_above(tuples, target):
            index_1, index_2 = 0, 0
            x_1 = target[1]
            y_1 = target[0]
            x_2 = target[1]
            y_2 = target[0]
            
            for i in range(len(tuples)):
                if int(tuples[i][0]) == int(target[0]) and int(tuples[i][1]) == int(target[1]):
                    index_1 = i
                    print(index_1)
            
            for i in range(len(tuples)):
                if int(tuples[i][0]) == int(target[0]) + 1 and int(tuples[i][1]) == int(target[1]):
                    index_2 = i

            
            print(tuples[2])
            print(tuples[14])
            
            tuples[index_1], tuples[index_2] = tuples[index_2], tuples[index_1]
            tuples[index_1][0] = y_2

            print(tuples[2])
            print(tuples[14])
                

def move_left(tuples, file, target):
    if not container_left(tuples, target):
        num = int(target[1])
        print(num)
        for i in range(num, 0, -1):
            file.write("Move left\n")
    

if __name__ == "__main__":
    file = open("operations.txt", "w")
    # Temporary (for testing different target crates)
    # y_in, x_in = input("What are the coordinates of the target container? (y, x)\n").split(" ")
    # print(F"Target container: {y_in}, {x_in}")
    target = ("01", "03", "00600", "Dog")

    # Opens manifest
    f = open('ShipCase3.txt', 'r')

    tuples = []
    i = 0

    # Parses manifest for each containers coordinates, weight, and info
    # y, x, weight, info stored in a list of tuples
    for line in f:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue

        y, x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        info = parts[2]

        tuples.append((y, x, weight, info))
        # print(f"{y} {x}")
    #print(tuples)
    move_up(tuples, file, target)
    #print(tuples)
    move_left(tuples, file, target)
    # print(tuples)
    f.close()
    file.close()