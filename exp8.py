import random
import copy

def distance_matrix(n):
    # Random distances
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = random.randint(1, 10)
            dist[i][j] = d
            dist[j][i] = d
    return dist

def path_cost(path, dist):
    cost = 0
    for i in range(len(path)-1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][path[0]]
    return cost

def hill_climbing_tsp(n, dist, max_iter=1000):
    current = list(range(n))
    random.shuffle(current)
    current_cost = path_cost(current, dist)
    for _ in range(max_iter):
        improved = False
        for i in range(n):
            for j in range(i+1, n):
                new_path = current[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                new_cost = path_cost(new_path, dist)
                if new_cost < current_cost:
                    current = new_path
                    current_cost = new_cost
                    improved = True
        if not improved:
            break
    return current, current_cost

def main():
    n = 5
    dist = distance_matrix(n)
    
    print("Travelling Salesman Problem - Hill Climbing Algorithm")
    print(f"\nDistance matrix ({n} cities):")
    for i, row in enumerate(dist):
        print(f"  City {i}: {row}")
    
    path, cost = hill_climbing_tsp(n, dist)
    print(f"\nBest path found: {path}")
    print(f"Total distance: {cost}")

if __name__ == "__main__":
    main()