
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
    """Given a node, generates all possible child nodes"""
    children = []

    if node.airborn_container is not None:
        i, j = node.airborn_container

        for target in node.targets:
                if target == (i,j) and (i,j) == (7,0):
                    new_grid = [row[:] for row in node.grid]
                    node.targets.remove(target)
                    new_grid[i][j] = 0
                    new_grid[7][0] = 0
                    new_node = Node(new_grid, node.targets, node, node.g, node.h, "unload")
                    new_node.airborn_container = None
                    children.append(new_node)

        if node.grid[i][j] == 1:

                    # Move container up
            if i < 7 and node.grid[i+1][j] == 0:
                new_grid = [row[:] for row in node.grid]
                new_grid[i][j], new_grid[i+1][j] = new_grid[i+1][j], new_grid[i][j]
                new_targets = [(t[0]+1,t[1]) if t[0]==i and t[1]==j else t for t in node.targets]
                new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i+1}, {j})")
                new_node.airborn_container = (i+1, j)
                children.append(new_node)

                    # Move container down
            if i > 0 and node.grid[i-1][j] == 0:
                new_grid = [row[:] for row in node.grid]
                new_grid[i][j], new_grid[i-1][j] = new_grid[i-1][j], new_grid[i][j]
                new_targets = [(t[0]-1,t[1]) if t[0]==i and t[1]==j else t for t in node.targets]
                new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i-1}, {j})")
                if new_node.grid[i-2][j] == 1 or new_node.grid[i-2][j] == 2:
                    new_node.airborn_container = None
                else:
                    new_node.airborn_container = (i-1,j)
                children.append(new_node)

                    # Move container left
            if j > 0 and node.grid[i][j-1] == 0 and not container_above(node, i, j):
                new_grid = [row[:] for row in node.grid]
                new_grid[i][j], new_grid[i][j-1] = new_grid[i][j-1], new_grid[i][j]
                new_targets = [(t[0],t[1]-1) if t[0]==i and t[1]==j else t for t in node.targets]
                new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i}, {j-1})")
                if new_node.grid[i-1][j-1] == 1:
                    new_node.airborn_container = None
                else:
                    new_node.airborn_container = (i,j-1)
                children.append(new_node)

                    # Move container right
            if j < 11 and node.grid[i][j+1] == 0 and not container_above(node, i, j):
                new_grid = [row[:] for row in node.grid]
                new_grid[i][j], new_grid[i][j+1] = new_grid[i][j+1], new_grid[i][j]
                new_targets = [(t[0],t[1]+1) if t[0]==i and t[1]==j else t for t in node.targets]
                new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i}, {j+1})")
                if new_node.grid[i-1][j+1] == 1:
                    new_node.airborn_container = None
                else:
                    new_node.airborn_container = (i,j+1)
                children.append(new_node)
        
    else:
        for i in range(len(node.grid)):
            for j in range(len(node.grid[i])):
                if node.grid[i][j] == 2:
                    continue

                for target in node.targets:
                    if target[0] == i and target[1] == j and (i,j) == (7,0):
                        new_grid = [row[:] for row in node.grid]
                        node.targets.remove(target)
                        new_grid[i][j] = 0
                        new_grid[7][0] = 0
                        new_node = Node(new_grid, node.targets, node, node.g, node.h, "unload")
                        children.append(new_node)

                if node.grid[i][j] == 1:

                    # Move container up
                    if i < 7 and node.grid[i+1][j] == 0:
                        new_grid = [row[:] for row in node.grid]
                        new_grid[i][j], new_grid[i+1][j] = new_grid[i+1][j], new_grid[i][j]
                        new_targets = [(t[0]+1,t[1]) if t[0]==i and t[1]==j else t for t in node.targets]
                        new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i+1}, {j})")
                        new_node.airborn_container = (i+1, j)
                        children.append(new_node)

                    # Move container down
                    if i > 0 and node.grid[i-1][j] == 0:
                        new_grid = [row[:] for row in node.grid]
                        new_grid[i][j], new_grid[i-1][j] = new_grid[i-1][j], new_grid[i][j]
                        new_targets = [(t[0]-1,t[1]) if t[0]==i and t[1]==j else t for t in node.targets]
                        new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i-1}, {j})")
                        if new_node.grid[i-1][j] == 0:
                            new_node.airborn_container = (i,j)
                        children.append(new_node)

                    # Move container left
                    if j > 0 and node.grid[i][j-1] == 0 and not container_above(node, i, j):
                        new_grid = [row[:] for row in node.grid]
                        new_grid[i][j], new_grid[i][j-1] = new_grid[i][j-1], new_grid[i][j]
                        new_targets = [(t[0],t[1]-1) if t[0]==i and t[1]==j else t for t in node.targets]
                        new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i}, {j-1})")
                        if new_node.grid[i-1][j-1] == 0:
                            new_node.airborn_container = (i,j-1)
                        children.append(new_node)

                    # Move container right
                    if j < 11 and node.grid[i][j+1] == 0 and not container_above(node, i, j):
                        new_grid = [row[:] for row in node.grid]
                        new_grid[i][j], new_grid[i][j+1] = new_grid[i][j+1], new_grid[i][j]
                        new_targets = [(t[0],t[1]+1) if t[0]==i and t[1]==j else t for t in node.targets]
                        new_node = Node(new_grid, new_targets, node, node.g+1, node.h, f"({i}, {j}),({i}, {j+1})")
                        if new_node.grid[i-1][j+1] == 0:
                            new_node.airborn_container = (i,j+1)
                        children.append(new_node)

    return children

def a_star(target, tuples):
    f = open('operations.txt', 'w')

    open_list = []
    closed_list = []
    open_list.append(target)

    while open_list:
        open_list.sort(key=lambda x: x.f())
        node = open_list.pop(0)
        # closed_list.append(node)

        if len(node.targets) < 1:
            path = []
            while node.parent:
                path.append(node)
                node = node.parent
            path.append(node)
            path.reverse()
            write_manifest(path, tuples)
            for node in path:
                if node.move:
                    f.write(node.move)
                    f.write("\n")
            print("Successfully unloaded.")
            f.close()
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
    for target in node.targets:
        h += 1
        h += abs(target[0] - 7) + abs(target[1])
    return h

def read_manifest(file, targets):
    grid = [[None for x in range(12)] for y in range(8)]
    tuples = [[None for x in range(12)] for y in range(8)]
    target_containers = []
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) != 3:
            continue
        y,x = parts[0].strip("[]").split(",")
        weight = parts[1].strip("{}")
        desc = parts[2]
        tuples[int(y)-1][int(x)-1] = (y,x,weight,desc)

        if (int(weight), desc) in targets:
            target_containers.append((int(y)-1, int(x)-1))
        
        if (desc == "UNUSED"):
            grid[int(y)-1][int(x)-1] = 0
        elif (desc == "NAN"):
            grid[int(y)-1][int(x)-1] = 2
        else:
            grid[int(y)-1][int(x)-1] = 1
        
        target_node = Node(grid, None, None, 0, 0, None)

    return target_node, target_containers, tuples

def write_manifest(path, tuples):
    updated_manifest = open('updated_manifest.txt', 'w')
    for node in path:
        if node.move == "unload":
            tuples[7][0] = ('08','01', '00000', 'UNUSED')
        elif node.move is not None:
            y_1, x_1, y_2, x_2 = [int(num.strip("()")) for num in node.move.split(",")]
            if len(str(y_1)) < 2:
                y_1 = '0' + str(y_1+1)
            if len(str(x_1)) < 2:
                x_1 = '0' + str(x_1+1)
            if len(str(y_2)) < 2:
                y_2 = '0' + str(y_2+1)
            if len(str(x_2)) < 2:
                x_2 = '0' + str(x_2+1)
            # tuples[y_1][x_1][-2:], tuples[y_2][x_2][-2:] = tuples[y_2][x_2][-2:], tuples[y_1][x_1][-2:]
            print_manifest(tuples)
            print("\n")
            temp1 = (str(y_1), str(x_1), tuples[int(y_2)-1][int(x_2)-1][2], tuples[int(y_2)-1][int(x_2)-1][3])
            temp2 = (str(y_2), str(x_2), tuples[int(y_1)-1][int(x_1)-1][2], tuples[int(y_1)-1][int(x_1)-1][3])
            tuples[int(y_1)-1][int(x_1)-1] = temp1
            tuples[int(y_2)-1][int(x_2)-1] = temp2

    print_manifest(tuples)
    for tup in tuples:
        for i in range(12):
            updated_manifest.write(str(f"[{tup[i][0]},{tup[i][1]}], {{{tup[i][2]}}}, {tup[i][3]}").strip("()"))
            updated_manifest.write("\n")
    print("Manifest updated.")

def print_manifest(tuples):
    for i in range(7,-1,-1):
        row = [tuples[i][j][3].ljust(11) for j in range(11)]
        print("".join(row))

def start_unload():
    file = open('ShipCase1.txt')

    targets = []
    num = input("How many containers will you be unloading? ")
    print("Please provide the weight and contents of each container (weight, contents):")
    for i in range(int(num)):
        user_input = input()
        weight, contents = user_input.split(", ")
        targets.append((int(weight), str(contents)))

    target_node, target_containers, tuples = read_manifest(file, targets)
    target_node.targets = target_containers
    a_star(target_node, tuples)

if __name__ == "__main__":
    start_unload()
    