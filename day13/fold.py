def fold(coords, fold_number, axis):
    new_coords = []
    for c in coords:
        if c[axis] == fold_number:
            continue
        new_point = fold_number - abs(c[axis] - fold_number)
        c[axis] = new_point
        
        if c not in new_coords:
            new_coords.append(c)
    
    return new_coords

with open("input.txt", 'r') as infile:
    lines = infile.read().splitlines()

    space = lines.index('')
    coords = lines[:space]
    folds = lines[space+1:]

    for i, c in enumerate(coords):
        coords[i] = [int(j) for j in c.split(",")]
    
    for i, f in enumerate(folds):
        f = f.split('=')
        folds[i] = [True if f[0][-1] == 'y' else False, int(f[1])]

for f in folds:
    coords = fold(coords, f[1], f[0])

x_max, y_max = 0, 0

for c in coords:
    x_max = max(x_max, c[0])
    y_max = max(y_max, c[1])

display = []
for y in range(y_max + 1):
    display.append([])
    for x in range(x_max + 1):
        display[y].append('.')

for c in coords:
    display[c[1]][c[0]] = '#'

for row in display:
    print(''.join(row))