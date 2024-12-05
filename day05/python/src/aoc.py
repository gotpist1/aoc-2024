from day05.python.utils.aoc_utils import groupBy


def get_input(data):
    s = data.split("\n\n")
    ordering_rules_dict = groupBy(lambda x: x, [x.rstrip().split("|") for x in s[0].split("\n")])
    updates = [x.split(',') for x in s[1].split("\n")]
    return ordering_rules_dict, updates


def get_middle_number(lst):
    length = len(lst)
    if length % 2 != 0:  # Check if the length is odd
        middle_index = length // 2
        return lst[middle_index]
    else:  # If the length is even
        middle_indices = length // 2
        return (lst[middle_indices - 1] + lst[middle_indices]) / 2


def getSolutionPart1(input_list):
    ordering_rules_dict, updates = get_input(input_list)
    ok_updates = []
    for update in updates:
        checked_keys = []
        for i in range(len(update)):
            first = update[i].strip()
            if i + 1 < len(update):
                second = update[i + 1].strip()
                if first not in ordering_rules_dict.keys():
                    break
                keys_children = ordering_rules_dict.get(first)
                if second not in keys_children:
                    break
                checked_keys.append(first)
            else:
                keys_children = ordering_rules_dict.get(first)
                if keys_children and any(child_checked in keys_children for child_checked in checked_keys):
                    break
                else:
                    middle_number = get_middle_number(update)
                    ok_updates.append(int(middle_number))
    print(sum(ok_updates))


def getSolutionPart2(input_list):
    ordering_rules_dict, updates = get_input(input_list)
    ok_updates = []
    for update in updates:
        current = []
        is_valid = True
        for page in update:
            if page in ordering_rules_dict:
                for idx, valid in enumerate(current):
                    if valid in ordering_rules_dict[page]:
                        is_valid = False
                        current.insert(idx, page)
                        break
                else:
                    current.append(page)
            else:
                current.append(page)
        middle = get_middle_number(current)
        if not is_valid:
            ok_updates.append(int(middle))
    print(sum(ok_updates))


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.read()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
