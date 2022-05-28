import math

def basin(coord,  heightmap):
    x, y = coord[1], coord[0]
    if heightmap[y][x] == 9:
        return 0

    total = 1
    heightmap[y][x] = 9
    if x > 0:
        total += basin([y, x-1], heightmap)
    if x < len(heightmap[0]) - 1:
        total += basin([y, x+1], heightmap)
    if y > 0:
        total += basin([y-1, x], heightmap)
    if y < len(heightmap) - 1:
        total += basin([y+1, x], heightmap)
    
    return total

with open("input.txt") as infile:
    heightmap = infile.read().splitlines()
    low_points = []
    basins = []
    for i, row in enumerate(heightmap):
        col_list = []
        for col in row:
            col_list.append(int(col))
        heightmap[i] = col_list
    
    for y, row in enumerate(heightmap):
        for x, col in enumerate(row):
            if x > 0:
                if heightmap[y][x-1] <= col:
                    continue
            if x < len(row) - 1:
                if heightmap[y][x+1] <= col:
                    continue
            if y > 0:
                if heightmap[y-1][x] <= col:
                    continue
            if y < len(heightmap) - 1:
                if heightmap[y+1][x] <= col:
                    continue
            low_points.append([y, x])
    
    for low_point in low_points:
        basins.append(basin(low_point, heightmap))
    
    product = math.prod(sorted(basins)[-3:])
    print(product)