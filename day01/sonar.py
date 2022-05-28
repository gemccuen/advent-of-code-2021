with open("input.txt", 'r') as infile:
    prev_s = infile.readline().strip()
    s = infile.readline().strip()
    times = 0
    while s != "":
        prev_num, num = int(prev_s), int(s)
        if num > prev_num:
            times += 1
        prev_s = s
        s = infile.readline().strip()

print(times)