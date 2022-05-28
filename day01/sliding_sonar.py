with open("testinput.txt", 'r') as infile:
    times = 0

    s1 = infile.readline().strip()
    s2 = infile.readline().strip()
    s3 = infile.readline().strip()
    prev_num = int(s1) + int(s2) + int(s3)

    s1 = s2
    s2 = s3
    s3 = infile.readline().strip()
    while s3 != "":
        n1, n2, n3 = int(s1), int(s2), int(s3)
        num = n1 + n2 + n3
        if num > prev_num:
            times += 1
        
        prev_num = num
        s1 = s2
        s2 = s3
        s3 = infile.readline().strip()

print(times)