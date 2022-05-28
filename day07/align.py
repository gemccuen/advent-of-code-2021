with open("input.txt", 'r') as infile:
    crabs = [int(c) for c in infile.readline().split(",")]
    crab_map = {}
    min_num = 10000000000000000000
    final_pos = 0
    for c in crabs:
        if not str(c) in crab_map:
            s = 0
            for pos in crabs:
                s += abs(pos - c)
            if s < min_num:
                final_pos = c
                min_num = s
    print(f"Pos {final_pos}, fuel consumption {min_num}")