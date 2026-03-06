def alpha_beta_pruning(values, branching=2, is_max=True, alpha=-float('inf'), beta=float('inf')):
    if not values:
        return 0, []
    if len(values) == 1:
        return values[0], [values[0]]
    if is_max:
        max_val = -float('inf')
        best_path = []
        for i in range(branching):
            if i * (len(values) // branching) < len(values):
                sub_values = values[i * (len(values) // branching):(i+1) * (len(values) // branching)]
                val, path = alpha_beta_pruning(sub_values, branching, False, alpha, beta)
                if val > max_val:
                    max_val = val
                    best_path = [f"MAX({val})"] + path
                alpha = max(alpha, val)
                if beta <= alpha:
                    break  # prune
        return max_val, best_path
    else:
        min_val = float('inf')
        best_path = []
        for i in range(branching):
            if i * (len(values) // branching) < len(values):
                sub_values = values[i * (len(values) // branching):(i+1) * (len(values) // branching)]
                val, path = alpha_beta_pruning(sub_values, branching, True, alpha, beta)
                if val < min_val:
                    min_val = val
                    best_path = [f"MIN({val})"] + path
                beta = min(beta, val)
                if beta <= alpha:
                    break  # prune
        return min_val, best_path

def main():
    values = [5, 3, 2, 4, 1, 3, 6, 2, 8, 7, 5, 1, 3, 4]
    print("Game Tree Alpha-Beta Pruning")
    print(f"Leaf values: {values}")
    print(f"Branching factor: 2, Depth: 4")
    print(f"Root player: MIN\n")
    
    val, path = alpha_beta_pruning(values, 2, False)
    print(f"Root value: {val}")
    print(f"Pruned tree path: {path}", )

if __name__ == "__main__":
    main()