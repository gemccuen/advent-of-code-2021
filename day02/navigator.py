with open("input.txt", 'r') as infile:
    pos, depth = 0, 0

    step = infile.readline().strip()
    while step != "":
        cmd, arg = step.split(" ")
        num = int(arg)

        if cmd == "forward":
            pos += num
        elif cmd == "down":
            depth += num
        elif cmd == "up":
            depth -= num

        step = infile.readline().strip()

print(pos * depth)