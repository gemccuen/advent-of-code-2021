import time
start = process_start = time.time()

NEW_FISH = 8
RESET_FISH = 6

with open("input.txt", 'r') as infile:
    fish = [int(f) for f in infile.readline().split(",")]
    simulation_length = 256

    counts = [0 for i in range(9)]
    for i in range(9):
        counts[i] = fish.count(i)
    
    for day in range(simulation_length):
        zero_value = counts[0]
        for key in range(1, 9):
            counts[key - 1] = counts[key]
            counts[key] = 0
        counts[NEW_FISH] = zero_value
        counts[RESET_FISH] += zero_value

        print(f"Took {time.time() - process_start:.3f} seconds to simulate day {day + 1} ({sum(counts)} fish and {time.time() - start:.3f} total seconds)")
        process_start = time.time()