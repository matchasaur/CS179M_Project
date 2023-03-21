class Node:
    def __init__(self, grid, targets, parent, g, h, move):
        self.grid = grid
        self.g = g
        self.h = h
        self.parent = None
        self.targets = targets
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

def a_star(target):
    open_list = []
    closed_list = []
    open_list.append(target)

    while open_list:
        open_list.sort(key=lambda x: x.f())
        node = open_list.pop(0)

        if len(node.targets) < 1:
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
        
        target_node = Node(grid, None, None, 0, 0, None)

    return grid

if __name__ == "__main__":
    file = open('ShipCase4.txt')
    target_node = read_manifest(file)

    containers = 1
