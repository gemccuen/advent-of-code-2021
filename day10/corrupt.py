with open("input.txt", 'r') as infile:
    start_chars = "([{<"
    end_chars = ")]}>"

    invalid_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    invalid_amount = 0

    lines = infile.read().splitlines()

    for line in lines:
        start_stack = []
        for c in line:
            if c in start_chars:
                start_stack.append(c)
            elif c in end_chars:
                last_start = start_stack.pop()
                if start_chars.index(last_start) != end_chars.index(c):
                    print(f"Got invalid {c} instead of {end_chars[start_chars.index(last_start)]}")
                    invalid_amount += invalid_table[c]
                    break
    
    print(invalid_amount)