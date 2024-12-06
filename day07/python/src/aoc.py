from day07.python.utils.aoc_utils import InputGrid



def getSolutionPart1(input_list):
    pass


def getSolutionPart2(input_list):
    pass


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
