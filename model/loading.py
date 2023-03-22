class Node:
    def __init__(self, grid, target, empty, parent, g, h, move):
        self.grid = grid
        self.g = g
        self.h = h
        self.parent = None
        self.target = target
        self.empty = empty
        self.parent = parent
        self.move = move
        self.airborn_container = None

    def f(self):
        return self.g + self.h

    def __str__(self):
        rows = []
        for row in self.grid:
            rows.append(' '.join(str(cell) for cell in row))
        return '\n'.join(rows)
    
def container_above(node, y, x):
    if y > 6:
        return False
    elif node.grid[y+1][x] == 1:
        return True
    return False

def container_below(node, y, x):
    if y < 1:
        return True
    elif node.grid[y-1][x] == 1 or node.grid[y-1][x] == 2:
        True
    return False
    
def expand(node):
    children = []

    i,j = node.airborn_container

    if i > 0 and node.grid[i-1][j] == 0:
        print("sldflkj")
        new_grid = [row[:] for row in node.grid]
        new_grid[i][j], new_grid[i-1][j] = new_grid[i-1][j], new_grid[i][j]
        # new_targets = [(t[0]-1,t[1]) if t[0]==i and t[1]==j else t for t in node.targets]
        new_node = Node(new_grid, node.target, node.empty, node, node.g, node.h, f"({i}, {j})-->({i-1}, {j})")
        if new_node.grid[i-2][j] == 1 or new_node.grid[i-2][j] == 2:
            new_node.airborn_container = None
        else:
            new_node.airborn_container = (i-1,j)
        children.append(new_node)

    if j < 11 and node.grid[i][j+1] == 0 and not container_above(node, i, j):
        new_grid = [row[:] for row in node.grid]
        new_grid[i][j], new_grid[i][j+1] = new_grid[i][j+1], new_grid[i][j]
        # new_targets = [(t[0],t[1]+1) if t[0]==i and t[1]==j else t for t in node.targets]
        new_node = Node(new_grid, node.target, node.empty, node, node.g, node.h, f"({i}, {j})-->({i}, {j+1})")
        if new_node.grid[i-1][j+1] == 1:
            new_node.airborn_container = None
        else:
            new_node.airborn_container = (i,j+1)
        children.append(new_node)

    return children


def a_star(target):
    open_list = []
    closed_list = []
    open_list.append(target)

    while open_list:
        open_list.sort(key=lambda x: x.f())
        node = open_list.pop(0)

        if node.airborn_container is None:
            path = []
            while node.parent:
                path.append(node)
                node = node.parent
            path.append(node)
            path.reverse()

            for node in path:
                print(node.move)
            
            return True
        
        children = expand(node)

        for child in children:
            if child.grid in closed_list:
                continue
            print("\n")
            print(child)

            same_grid_in_open_list = False
            for n in open_list:
                if n.grid == child.grid:
                    same_grid_in_open_list = True
                    if child.g < n.g:
                        n.g = child.g
                        n.parent = node
                    break
            if not same_grid_in_open_list:
                child.g = node.g + 1
                child.h = manhattan(child)
                open_list.append(child)
                child.parent = node
            
            closed_list.append(child.grid)

    print("Could not find path")
    return None

def manhattan(node):
    h = 0
    h += abs(node.target[0] - node.empty[0]) + abs(node.target[1] - node.empty[1])
    return h

def find_empty(node):
    for i in range(len(node.grid)):
        for j in range(len(node.grid[i])):
            if node.grid[i][j] == 0:
                return (i,j)

def read_manifest(file):
    grid = [[None for x in range(12)] for y in range(8)]
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue
        y,x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        desc = parts[2]

        if (desc == "UNUSED"):
            grid[int(y)-1][int(x)-1] = 0
        elif (desc == "NAN"):
            grid[int(y)-1][int(x)-1] = 2
        else:
            grid[int(y)-1][int(x)-1] = 1
        
        target_node = Node(grid, (7,0), None, None, 0, 0, None)

    return target_node

if __name__ == "__main__":
    file = open('ShipCase4.txt')
    target_node = read_manifest(file)
    
    empty = find_empty(target_node)
    target_node.empty = empty
    target_node.airborn_container = (7,0)
    target_node.grid[7][0] = 1

    a_star(target_node)

    containers = 1
