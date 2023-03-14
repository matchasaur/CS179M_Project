
def retrieve_container():
    pass

############ COLLISION CHECK ##############

def container_above(arr, target):
    y = target[0]
    x = target[1]
    if arr[y+1][x][1] == "UNUSED":
        return False
    else:
        return True
    
def container_left(arr, target):
    y = target[0]-1
    x = target[1]-1
    if arr[y][x-1][1] == "UNUSED":
        return False
    else:
        return True
    
def container_right(arr, target):
    y = target[0]
    x = target[1]
    if arr[y][x+1][1] == "UNUSED":
        return False
    else:
        return True
    
def container_below(arr, targe):
    y = target[0]-1
    x = target[1]-1
    if arr[y-1][x][1] == "UNUSED":
        return False
    else:
        return True

############# OPERATIONS #################

def move_up(arr, target):
    if not container_above(arr, target):
        y = target[0]-1
        x = target[1]-1
        arr[y][x], arr[y+1][x] = arr[y+1][x], arr[y][x]
        target = (y+2, x+1)
    else:
        print("Container in the way")
        return target

    return target

def move_down(arr, target):
    if not container_below(arr, target):
        y = target[0]-1
        x = target[1]-1
        arr[y][x], arr[y-1][x] = arr[y-1][x], arr[y][x]
        target = (y, x+1)
    else:
        print("Container in the way")
        return target

    return target

def move_left(arr, target):
    if not container_left(arr, target):
        y = target[0]-1
        x = target[1]-1
        arr[y][x], arr[y][x-1] = arr[y][x-1], arr[y][x]
        target = (y+1, x)
    else:
        print("Container in the way")
        return target

def move_right(arr, target):
    if not container_right(arr, target):
        y = target[0]-1
        x = target[1]-1
        arr[y][x], arr[y][x+1] = arr[y][x+1], arr[y][x]
        target = (y+1, x+2)
    else:
        print("Container in the way")
        return target


############### READ MANIFEST ##################

def make_arr(file):
    arr = [[None for x in range(12)] for y in range(8)]

    for line in file:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue

        y, x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        info = parts[2]

        tuple = (weight, info)
        arr[int(y)-1][int(x)-1] = tuple

    return arr


if __name__ == "__main__":
    file = open('ShipCase3.txt', 'r')
    target = (1, 3)

    arr = make_arr(file)

    print(target)
    target = move_up(arr, target)
    print(target)
    target = move_right(arr, target)
    print(target)
    target = move_right(arr, target)
    target = move_down(arr, target)
    print(target)