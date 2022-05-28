with open("input.txt", 'r') as infile:
    lines = infile.read().splitlines()
    length = len(lines[0])

    oxygen, co2 = 0, 0

    #OXYGEN
    list_to_search = lines
    for i in range(length):
        list0 = []
        list1 = []
        for str in list_to_search:
            if str[i] == "0":
                list0.append(str)
            else:
                list1.append(str)
        
        list_to_search = list1 if len(list1) >= len(list0) else list0
        if len(list_to_search) == 1:
            oxygen = int(list_to_search[0], 2)
            break
    
    #CARBON DIOXIDE
    list_to_search = lines
    for i in range(length):
        list0 = []
        list1 = []
        for str in list_to_search:
            if str[i] == "0":
                list0.append(str)
            else:
                list1.append(str)
        
        list_to_search = list0 if len(list1) >= len(list0) else list1
        if len(list_to_search) == 1:
            co2 = int(list_to_search[0], 2)
            break

print(oxygen * co2)