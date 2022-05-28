from math import ceil

with open("input.txt", 'r') as infile:
    lines = infile.read().splitlines()

    polymer = lines[0]
    insertions = lines[2:]

    insertion_map = {}
    for i in insertions:
        key, value = i.split(' -> ')
        insertion_map[key] = value
    
    polymer_map = {}
    for c in range(len(polymer) - 1):
        pair = polymer[c:c+2]
        polymer_map[pair] = polymer_map.get(pair, 0) + 1
    
    steps = 40
    for _ in range(steps):
        new_map = {}
        for k, v in polymer_map.items():
            ins = insertion_map[k]
            str1, str2 = k[0] + ins, ins + k[1]
            for s in [str1, str2]:
                new_map[s] = new_map.get(s, 0) + v 
        polymer_map = new_map
    
    char_map = {}
    for k, v in polymer_map.items():
        for c in k:
            char_map[c] = char_map.get(c, 0) + v * 0.5
    
    # for k, v in char_map.items():
    #     char_map[k] = ceil(v)
    values = char_map.values()
    print(ceil(max(values) - min(values)))