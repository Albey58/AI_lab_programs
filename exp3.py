import itertools

def solve_cryptarithm(puzzle):
    parts = puzzle.replace(' ', '').split('=')
    if len(parts) != 2:
        return None
    
    left_side = parts[0].split('+')
    right_side = parts[1]
    all_words = left_side + [right_side]
    letters = list(set(''.join(all_words)))

    if len(letters) > 10:
        return None

    first_letters = set(word[0] for word in all_words)

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[let] == 0 for let in first_letters):
            continue

        try:
            left_sum = sum(int(''.join(str(mapping[c]) for c in word)) for word in left_side)
            right_val = int(''.join(str(mapping[c]) for c in right_side))
        except KeyError:
            continue

        if left_sum == right_val:
            return mapping

    return None

def main():
    puzzles = [
        "EAT + THAT = APPLE",
        "POINT + ZERO = ENERGY",
        "CROSS + ROADS = DANGER"
    ]
    
    for puzzle in puzzles:
        print(f"Solving: {puzzle}")
        solution = solve_cryptarithm(puzzle)
        
        if solution:
            print("Solution:")
            for letter, digit in sorted(solution.items()):
                print(f"  {letter} = {digit}")
            
            parts = puzzle.replace(' ', '').split('=')
            left = parts[0].split('+')
            right = parts[1]
            left_nums = [''.join(str(solution[c]) for c in word) for word in left]
            right_num = ''.join(str(solution[c]) for c in right)
            print(f"Verification: {' + '.join(left_nums)} = {right_num}")
        else:
            print("No solution found.")
        print()

if __name__ == "__main__":
    main() 
