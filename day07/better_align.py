with open("input.txt", 'r') as infile:
    crabs = [int(c) for c in infile.readline().split(",")]
    min_num = 10000000000000000000
    final_pos = 0
    for i in range(min(crabs), max(crabs) + 1):
        s = 0
        for c in crabs:
            diff = abs(c - i)
            s += diff * (diff + 1) / 2
        if s < min_num:
            min_num = s
            final_pos = i
    
    print(f"Pos {final_pos}, fuel consumption {min_num}")