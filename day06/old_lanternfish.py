import time
start = process_start = time.time()

with open("input.txt", 'r') as infile:
    fish = [int(f) for f in infile.readline().split(",")]
    simulation_length = 80

    NEW_FISH = 9
    RESET_FISH = 6

    for day in range(simulation_length):
        for i, f in enumerate(fish):
            new = f - 1
            if new < 0:
                fish.append(NEW_FISH)
                new = RESET_FISH
            fish[i] = new
        print(f"Took {time.time() - process_start:.3f} seconds to simulate day {day + 1} ({len(fish)} fish and {time.time() - start:.3f} total seconds)")
        process_start = time.time()