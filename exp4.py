import heapq

# State: tuple of stacks, e.g. (('A','B','C'), ('D',), ())
# Goal: all blocks in one stack in order

start = (('E',), ('B','F'), ('D','A','C'))
goal  = (('E','F','C'), ('A','D','B'), ())

def heuristic(state):
    # Count blocks NOT in correct position in goal stack
    goal_stack = goal[0]
    count = 0
    for i, block in enumerate(goal_stack):
        if i >= len(state[0]) or state[0][i] != block:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    stacks = list(state)

    for i in range(len(stacks)):          # pick a stack to move FROM
        if not stacks[i]: continue        # skip empty stacks
        block = stacks[i][-1]             # top block

        for j in range(len(stacks)):      # pick a stack to move TO
            if i == j: continue
            new_stacks = [list(s) for s in stacks]
            new_stacks[i].pop()
            new_stacks[j].append(block)
            neighbors.append(tuple(tuple(s) for s in new_stacks))

    return neighbors

def best_first_search(start, goal):
    heap = [(heuristic(start), start)]   # (priority, state)
    visited = set()
    parent = {start: None}

    while heap:
        _, current = heapq.heappop(heap)

        if current == goal:
            # Trace path back
            path, node = [], current
            while node: path.append(node); node = parent[node]
            return path[::-1]

        if current in visited: continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(heap, (heuristic(neighbor), neighbor))

    return None

# --- Run & Display ---
path = best_first_search(start, goal)

for step, state in enumerate(path):
    print(f"Step {step}: {[list(s) for s in state]}")
