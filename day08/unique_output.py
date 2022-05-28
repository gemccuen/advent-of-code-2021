with open("input.txt", 'r') as infile:
    uniques = 0
    groups = [g.split(" | ") for g in infile.read().splitlines()]
    for group in groups:
        outputs = group[1].split(" ")
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                uniques += 1
    
    print(uniques)