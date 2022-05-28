with open("input.txt", 'r') as infile:
    vent_map = {}
    overlaps = []
    lines = [line.split(" -> ") for line in infile.read().splitlines()]
    for line in lines:
        line1 = [int(coord) for coord in line[0].split(",")]
        line2 = [int(coord) for coord in line[1].split(",")]
        if line1[0] == line2[0] or line1[1] == line2[1]:
            index = line1[0] == line2[0]
            matching = not index
            bound1, bound2 = line1[index], line2[index]
            matching_num = line1[matching]
            step = 1 if bound1 < bound2 else -1
            for i in range(bound1, bound2 + step, step):
                key = f"{str(matching_num) if not matching else str(i)}-{str(matching_num) if matching else str(i)}"
                try:
                    vent_map[key] += 1
                    if key not in overlaps:
                        overlaps.append(key)
                except KeyError:
                    vent_map[key] = 1
    
    print(len(overlaps))
