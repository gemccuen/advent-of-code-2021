import numpy as np

with open("input.txt", 'r') as infile:
    start_chars = "([{<"
    end_chars = ")]}>"

    lines = infile.read().splitlines()
    totals = []

    for line in lines:
        total = 0
        start_stack = []
        invalid = False
        for c in line:
            if c in start_chars:
                start_stack.append(c)
            elif c in end_chars:
                last_start = start_stack.pop()
                if start_chars.index(last_start) != end_chars.index(c):
                    invalid = True
                    break
        if invalid:
            continue
        
        while len(start_stack) > 0:
            last = start_stack.pop()
            total *= 5
            total += start_chars.index(last) + 1
        
        totals.append(total)
    
    print(int(np.median(totals)))