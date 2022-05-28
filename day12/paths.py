valid_paths = []

def search(map_of_caves, node, visited=None, path=None):
    if visited is None:
        visited = []
    
    if path is None:
        path = []

    if node == "end":
        valid_paths.append(path)
        return
    
    path.append(node)

    if node.islower():
        visited.append(node)

    for c in map_of_caves[node]:
        if c not in visited:
            search(map_of_caves, c, visited.copy(), path.copy())

with open("input.txt", 'r') as infile:
    map_of_caves = {}
    connections = infile.read().splitlines()
    for c in connections:
        c = c.split("-")
        for i, node in enumerate(c):
            other = not i
            if node not in map_of_caves:
                map_of_caves[node] = []
            map_of_caves[node].append(c[other])

    search(map_of_caves, "start")
    print(len(valid_paths))