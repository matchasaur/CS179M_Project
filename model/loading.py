def load(tuples):
    pass

def container_above(tuples, target):
    y = int(target[0]) + 1
    x = int(target[1])
    print(y)
    print(x)
    for i in range(len(tuples)):
        if int(tuples[i][0]) == y and int(tuples[i][1]) == x:
            print(tuple[i])
            if tuples[i][3] == "UNUSED":
                return False
            else:
                return True
            break

    print("Couldn't find container")
    return True
            



if __name__ == "__main__":

    # Temporary (for testing different target crates)
    # y_in, x_in = input("What are the coordinates of the target container? (y, x)\n").split(" ")
    # print(F"Target container: {y_in}, {x_in}")
    target = ("01", "03", "10001", "Ewe")

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

    if container_above(tuples, target):
        print("Container above target")
    else:
        print("No container above target")

    # print(tuples)
    f.close()

