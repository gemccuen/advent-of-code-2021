with open("input.txt", 'r') as infile:
    lines = infile.read().splitlines()
    length = len(lines[0])

    gamma_str = epsilon_str = ""

    for i in range(length):
        count0 = 0
        count1 = 0
        for str in lines:
            if str[i] == "0":
                count0 += 1
            else:
                count1 += 1
        
        gamma_str += "0" if count0 > count1 else "1"
        epsilon_str += "0" if count0 < count1 else "1"
    
    gamma_num, epsilon_num = int(gamma_str, 2), int(epsilon_str, 2)

print(gamma_num * epsilon_num)