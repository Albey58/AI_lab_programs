# Tower of Hanoi Problem Solver
# This program solves the Tower of Hanoi puzzle using a planning approach.
# The Tower of Hanoi is a classic puzzle where you have three rods and a number of disks of different sizes.
# The goal is to move all disks from the source rod to the target rod, following these rules:
# 1. Only one disk can be moved at a time.
# 2. A disk can only be placed on top of a larger disk or on an empty rod.
# 3. No disk may be placed on top of a smaller disk.

def hanoi_plan(n, source, target, auxiliary):
    """
    Generates a plan to solve the Tower of Hanoi for n disks.

    Args:
    n (int): Number of disks.
    source (str): Name of the source rod.
    target (str): Name of the target rod.
    auxiliary (str): Name of the auxiliary rod.

    Returns:
    list: A list of tuples, each representing a move (from, to).
    """
    if n == 1:
        # Base case: If there's only one disk, just move it directly.
        return [(source, target)]
    else:
        # Recursive case:
        # 1. Move n-1 disks from source to auxiliary, using target as auxiliary.
        # 2. Move the nth disk from source to target.
        # 3. Move the n-1 disks from auxiliary to target, using source as auxiliary.
        return hanoi_plan(n-1, source, auxiliary, target) + [(source, target)] + hanoi_plan(n-1, auxiliary, target, source)

def main():
    n = 3  # Number of disks
    source = 'A'
    target = 'C'
    auxiliary = 'B'

    # Generate the plan
    plan = hanoi_plan(n, source, target, auxiliary)

    print(f"Tower of Hanoi Solution for {n} disks:")
    print(f"Source: {source}, Target: {target}, Auxiliary: {auxiliary}")
    print(f"Total moves required: {len(plan)}\n")
    
    for i, move in enumerate(plan, 1):
        print(f"{i}. Move disk from {move[0]} to {move[1]}")

if __name__ == "__main__":
    main()