visited = []
paths = []
completed_paths = []

class PathNode:
    def __init__(self, coords, risk):
        self.coords = coords
        self.risk = risk
        self.next = None
    
    def __str__(self):
        return str(self.coords) + ", " + str(self.risk)

class Path:
    def __init__(self, coords, risk):
        self.head = PathNode(coords, risk)
    
    def __str__(self):
        node_list = []
        node = self.head
        for n in self:
            node_list.append(str(n.risk))
        return ' -> '.join(node_list)
    
    def append(self, node):
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node
    
    def diverge(self, node):
        new_path = Path(self.head.coords, self.head.risk)
        n = self.head
        while n.next is not None:
            n = n.next
            new_node = PathNode(n.coords, n.risk)
            new_path.append(new_node)
        new_path.append(node)
        return new_path

    @property
    def risk(self):
        total_risk = 0
        for n in self:
            total_risk += n.risk
        return total_risk
    
    @property
    def coords(self):
        n = self.head
        while n.next is not None:
            n = n.next
        return n.coords
    
    def __lt__(self, other):
        return self.risk < other.risk  

    def __iter__(self):
        self.n = self.head
        return self   

    def __next__(self):
        if self.n is not None:
            prev = self.n
            self.n = self.n.next
            return prev
        else:
            raise StopIteration   

with open("input.txt", 'r') as infile:
    risks = infile.read().splitlines()
    for i, l in enumerate(risks):
        risks[i] = [int(c) for c in l]

    WIDTH = len(risks)
    paths.append(Path([0, 0], 0))

    while len(paths) != 0:
        first_path = paths[0]
        del paths[0]
        while first_path.coords in visited:
            if len(paths) == 0:
                break
            first_path = paths[0]
            del paths[0]
        x, y = first_path.coords
        visited.append([x, y])

        new_paths = []
        if x > 0:
            nx, ny = x-1, y
            if [nx, ny] not in visited:
                new_paths.append(PathNode([nx, ny], risks[ny][nx]))
        if y > 0:
            nx, ny = x, y-1
            if [nx, ny] not in visited:
                new_paths.append(PathNode([nx, ny], risks[ny][nx]))
        if x < WIDTH - 1:
            nx, ny = x+1, y
            if [nx, ny] not in visited:
                new_paths.append(PathNode([nx, ny], risks[ny][nx]))
        if y < WIDTH - 1:
            nx, ny = x, y+1
            if [nx, ny] not in visited:
                new_paths.append(PathNode([nx, ny], risks[ny][nx]))
        
        for p in new_paths:
            new_path = first_path.diverge(p)
            if p.coords == [WIDTH - 1, WIDTH - 1]:
                print('found')
                completed_paths.append(new_path)
            else:
                paths.append(new_path)
        
        paths.sort()

        if len(visited) % 10 == 0:
            print(f"visited at {len(visited)}")
    
    completed_paths.sort()
    print(completed_paths[0].risk)