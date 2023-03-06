f = open('ShipCase3.txt', 'r')
for line in f:
    parts = line.strip().split(", ")
    if len(parts) != 3:
        continue
    cell = parts[0].strip("{}").split(", ")
    weight = parts[1].strip("{}")
    info = parts[2]
    print(f"{cell}, {weight}, {info}")
f.close()