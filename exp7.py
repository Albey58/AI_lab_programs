import random
import math
import copy

def print_puzzle(state):
    for i in range(3):
        print(' '.join(str(x) if x != 0 else ' ' for x in state[i*3:(i+1)*3]))
    print()

def find_blank(state):
    for i in range(9):
        if state[i] == 0:
            return i // 3, i % 3

def get_neighbors(r, c):
    neighbors = []
    if r > 0: neighbors.append((r-1, c))
    if r < 2: neighbors.append((r+1, c))
    if c > 0: neighbors.append((r, c-1))
    if c < 2: neighbors.append((r, c+1))
    return neighbors

def move(state, dr, dc):
    new_state = state[:]
    r, c = find_blank(state)
    nr, nc = r + dr, c + dc
    if 0 <= nr < 3 and 0 <= nc < 3:
        idx = r*3 + c
        nidx = nr*3 + nc
        new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
    return new_state

def heuristic(state, goal):
    count = 0
    for i in range(9):
        if state[i] != goal[i]:
            count += 1
    return count

def simulated_annealing(initial, goal, max_iter=10000, initial_temp=100):
    current = initial
    current_cost = heuristic(current, goal)
    temp = initial_temp
    for _ in range(max_iter):
        if current == goal:
            return current
        r, c = find_blank(current)
        neighbors = get_neighbors(r, c)
        if not neighbors:
            continue
        nr, nc = random.choice(neighbors)
        dr, dc = nr - r, nc - c
        new_state = move(current, dr, dc)
        new_cost = heuristic(new_state, goal)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = new_state
            current_cost = new_cost
        temp *= 0.99  # cooling
    return current

def main():
    initial = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    print("8-Puzzle Problem - Simulated Annealing Algorithm")
    print("\nInitial state:")
    print_puzzle(initial)
    print("Goal state:")
    print_puzzle(goal)
    
    result = simulated_annealing(initial, goal)
    print("Final state:")
    print_puzzle(result)
    
    if result == goal:
        print("Status: Solved")
    else:
        print("Status: Not solved")

if __name__ == "__main__":
    main()