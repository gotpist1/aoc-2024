from functools import lru_cache


def get_calc_dict(input_list):
    calc_dict = {}
    for line in input_list:
        cl = line.split(':')
        calc_dict[int(cl[0].strip())] = list(
            map(lambda x: int(x), filter(lambda x: x != '', list(map(lambda x: x.rstrip(), cl[1].split(' '))))))
    return calc_dict


def can_calculate_target_concat(target, nums, concat_allowed=False):
    memo = {}  # Memoization to avoid redundant calculations

    # Recursive helper function to try all ways of calculating the target
    def try_calculate(index, current_value, concat):
        # Early pruning: if current value exceeds target, stop exploring
        if current_value > target:
            return False

        # Base case: If we've used all numbers and reached the target
        if index == len(nums):
            return current_value == target

        # Check if this subproblem has been already computed
        if (index, current_value) in memo:
            return memo[(index, current_value)]

        # Try all three possible operations from the current position
        result = False
        next_num = nums[index]

        # Addition
        if not result:
            result = try_calculate(index + 1, current_value + next_num, concat_allowed)

        # Multiplication
        if not result:
            result = try_calculate(index + 1, current_value * next_num, concat_allowed)

        # Concatenation (||)
        if concat and not result:
            # Efficient concatenation without converting to string use math instead
            concatenated = current_value * (10 ** len(str(next_num))) + next_num
            result = try_calculate(index + 1, concatenated, concat_allowed)

        # Memoize the result
        memo[(index, current_value)] = result
        return result

    return try_calculate(1, nums[0], concat_allowed)


def getSolutionPart1(input_list):
    calc_dict = get_calc_dict(input_list)
    possible_values = list()
    for test_value, values in calc_dict.items():
        if can_calculate_target_concat(test_value, values):
            possible_values.append(test_value)

    print(sum(possible_values))


def getSolutionPart2(input_list):
    calc_dict = get_calc_dict(input_list)
    possible_values = list()
    for test_value, values in calc_dict.items():
        if can_calculate_target_concat(test_value, values, True):
            possible_values.append(test_value)
    print(sum(possible_values))


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        getSolutionPart1(file_input)
    else:
        getSolutionPart2(file_input)
