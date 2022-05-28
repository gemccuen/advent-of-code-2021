with open("input.txt", 'r') as infile:
    lines = infile.read().splitlines()

    polymer = lines[0]
    insertions = lines[2:]

    insertion_map = {}
    for i in insertions:
        key, value = i.split(' -> ')
        insertion_map[key] = value
    
    steps = 10
    for _ in range(steps):
        new_polymer = ''
        for c in range(len(polymer) - 1):
            new_str = polymer[c] + insertion_map[polymer[c:c+2]]
            new_polymer += new_str
        new_polymer += polymer[-1]
        polymer = new_polymer
    
    char_map = {}
    for c in polymer:
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] += 1
    
    values = char_map.values()
    print(max(values) - min(values))