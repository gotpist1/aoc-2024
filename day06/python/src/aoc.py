from day06.python.utils.aoc_utils import InputGrid

# Movement and direction change mappings
guard_positions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
next_pos = {"^": ">", ">": "v", "v": "<", "<": "^"}

def simulate_guard(input_grid, start_y, start_x):
    y, x = start_y, start_x
    p = '^'  # Start direction is up
    visited = set()

    print(f"Starting simulation from ({y}, {x}) facing {p}")

    while True:
        # Track position and direction to detect a loop
        if (y, x, p) in visited:
            print(f"Loop detected at ({y}, {x}) facing {p}")
            return True  # Loop detected

        visited.add((y, x, p))

        # Determine the next position based on the current direction
        dy, dx = guard_positions[p]
        new_y, new_x = y + dy, x + dx

        match = input_grid.grid_dict.get((new_y, new_x), "")
        if match == "":
            break  # Guard is outside the grid
        elif match == "#":
            # Change direction and stay in the current position
            p = next_pos[p]
        else:
            # Move to the new position
            y, x = new_y, new_x

    return False  # No loop detected


def get_start_position(input_grid):
    for y, x in input_grid.grid_dict:
        if input_grid.grid_dict[y, x] in guard_positions.keys():
            return y, x

def getSolutionPart1(input_list):
    input_grid = InputGrid(input_list)
    (y, x) = get_start_position(input_grid)
    guard_inside = True
    direction = "^"  # Current direction of the guard
    distinct_positions = set()
    distinct_positions.add((y, x))  # Add the initial position to the set of visited positions

    while guard_inside:
        # Determine the next position based on the current direction
        dy, dx = guard_positions[direction]
        new_y, new_x = y + dy, x + dx

        match = input_grid.grid_dict.get((new_y, new_x), "")
        if match == "":
            guard_inside = False  # Guard is outside the grid
        elif match == "#":
            # Change direction and stay in the current position
            direction = next_pos[direction]
        else:
            # Move to the new position
            y, x = new_y, new_x

        # Add the current position to the set of visited positions
        distinct_positions.add((y, x))

    print(len(distinct_positions))


def getSolutionPart2(input_list):
    input_grid = InputGrid(input_list)
    (start_y, start_x) = get_start_position(input_grid)

    loop_positions = []

    for k in input_grid.grid_dict.keys():
        (y, x) = k
        # Skip positions that are already obstacles or starting position
        if input_grid.grid_dict.get((y, x)) == '#' or (y, x) == (start_y, start_x):
            continue
        # Temporarily place an obstacle at (y, x) and check if it creates a loop
        input_grid.grid_dict[(y, x)] = '#'
        if simulate_guard(input_grid, start_y, start_x):
            loop_positions.append((y, x))
        input_grid.grid_dict[(y, x)] = '.'  # Remove the obstacle

    print(len(loop_positions))


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
