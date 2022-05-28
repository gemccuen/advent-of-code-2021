with open("input.txt", 'r') as infile:
    pos, depth, aim = 0, 0, 0

    step = infile.readline().strip()
    while step != "":
        cmd, arg = step.split(" ")
        num = int(arg)

        if cmd == "forward":
            pos += num
            depth += (aim * num)
        elif cmd == "down":
            aim += num
        elif cmd == "up":
            aim -= num

        step = infile.readline().strip()

print(pos * depth)