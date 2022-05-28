def display_dumbos(dumbos):
    for dumbo in dumbos:
        print("".join([str(i) if -1 < i < 10 else 'F' if i >= 10 else 'N' for i in dumbo]))
    print()

def flash(coord, dumbos):
    x, y = coord[0], coord[1]
    dumbos[y][x] = -1
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            if y+dy < 0 or x+dx < 0:
                continue
            try:
                if dumbos[y+dy][x+dx] >= 0:
                    dumbos[y+dy][x+dx] += 1
            except (IndexError, TypeError):
                pass
    
    for y, row in enumerate(dumbos):
            for x, col in enumerate(row):
                if col > 9:
                    flash([x, y], dumbos)

with open("input.txt", 'r') as infile:
    dumbos = infile.read().splitlines()
    simulation_length = 100
    flashes = 0

    for step in range(simulation_length):
        for i, row in enumerate(dumbos):
            col_list = []
            for col in row:
                col_list.append(int(col))
            dumbos[i] = col_list

        # First, increment each octopus
        for y, row in enumerate(dumbos):
            for x, col in enumerate(row):
                dumbos[y][x] = col + 1

        # Then, flash
        for y, row in enumerate(dumbos):
            for x, col in enumerate(row):
                if col > 9:
                    flash([x, y], dumbos)

        # Then, reset
        for y, row in enumerate(dumbos):
            for x, col in enumerate(row):
                if col < 0:
                    flashes += 1
                    dumbos[y][x] = 0
        
        print(f"STEP {step + 1}: {flashes} flashes")
        display_dumbos(dumbos)