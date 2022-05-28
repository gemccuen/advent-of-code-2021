with open("test_input.txt", 'r') as infile:
    risks = infile.read().splitlines()
    for i, l in enumerate(risks):
        risks[i] = [int(c) for c in l]

    WIDTH = len(risks)
    print(risks)