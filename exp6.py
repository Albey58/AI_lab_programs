import copy

def is_clear(state, block):
    for stack in state:
        if stack and stack[-1] == block:
            return True
    return False

def get_stack_index(state, block):
    for i, stack in enumerate(state):
        if block in stack:
            return i
    return -1

def move_block(state, block, to):
    new_state = copy.deepcopy(state)
    from_idx = get_stack_index(new_state, block)
    if from_idx == -1 or not new_state[from_idx] or new_state[from_idx][-1] != block:
        return None
    new_state[from_idx].pop()
    if to == 'table':
        new_state.append([block])
    else:
        to_idx = get_stack_index(new_state, to)
        if to_idx != -1 and is_clear(new_state, to):
            new_state[to_idx].append(block)
        else:
            return None
    new_state = [s for s in new_state if s]
    return new_state

def generate_and_test(initial, goal, max_depth=10):
    def generate(state, depth):
        if depth == 0:
            return [state]
        results = []
        for i, stack in enumerate(state):
            if stack:
                block = stack[-1]
                # Move to table
                new_state = move_block(state, block, 'table')
                if new_state:
                    results.extend(generate(new_state, depth - 1))
                # Move to other blocks
                for other_stack in state:
                    if other_stack and other_stack[-1] != block:
                        new_state = move_block(state, block, other_stack[-1])
                        if new_state:
                            results.extend(generate(new_state, depth - 1))
        return results
    for depth in range(1, max_depth + 1):
        states = generate(initial, depth)
        for state in states:
            if state == goal:
                return True  # Found
    return False

def means_ends_analysis(current, goal):
    if current == goal:
        return []
    # Find differences
    differences = []
    for i, s_goal in enumerate(goal):
        if i >= len(current) or current[i] != s_goal:
            differences.append((i, s_goal))
    if not differences:
        return []
    # Choose a difference
    idx, target_stack = differences[0]
    # Find operators to achieve
    operators = []
    for block in target_stack:
        # Find where block is
        current_stack_idx = get_stack_index(current, block)
        if current_stack_idx != idx or current[current_stack_idx].index(block) != target_stack.index(block):
            # Need to move
            operators.append(('move', block, 'table' if target_stack.index(block) == 0 else target_stack[target_stack.index(block) - 1]))
    # Apply first operator
    if operators:
        op = operators[0]
        new_state = move_block(current, op[1], op[2])
        if new_state:
            sub_plan = means_ends_analysis(new_state, goal)
            if sub_plan is not None:
                return [op] + sub_plan
    return None

def main():
    initial = [['E', 'B', 'F', 'D', 'A', 'C']]
    goal = [['A', 'D', 'B', 'E', 'F', 'C']]
    
    print("Block World - Generate & Test and Means-Ends Analysis")
    print(f"Initial: {initial}")
    print(f"Goal: {goal}\n")
    
    print("Generate & Test:")
    found = generate_and_test(initial, goal)
    print(f"  Solution exists: {found}")
    
    print("\nMeans-Ends Analysis:")
    plan = means_ends_analysis(initial, goal)
    if plan:
        print(f"  Plan steps: {len(plan)}")
        for i, step in enumerate(plan, 1):
            print(f"    {i}. {step}")
    else:
        print("  No plan found.")

if __name__ == "__main__":
    main()