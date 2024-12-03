import re
from os import environ
MUL_PATTERN = re.compile(r'mul\(\s*-?\d+\s*,\s*-?\d+\s*\)')
MUL_PATTERN_DO_DONT = re.compile(r"mul\(\s*-?\d+\s*,\s*-?\d+\s*\)|do\(\)|don't\(\)")
NUM_PATTERN = re.compile(r'-?\d+')




def getSolutionPart1(input_list):
    multipliers = MUL_PATTERN.findall(input_list)
    numbers = [NUM_PATTERN.findall(g) for g in multipliers]
    multiplied = [int(n[0]) * int(n[1]) for n in numbers]
    total = sum(multiplied)
    print(f'Total multiplied numbers: {total}')



def getSolutionPart2(input_list):
    matches = MUL_PATTERN_DO_DONT.findall(input_list)
    include = True
    multipliers = []

    for match in matches:
        if match == "do()":
            include = True
        elif match == "don't()":
            include = False
        else:
            if include:
                multipliers.append(match)
    numbers = [NUM_PATTERN.findall(g) for g in multipliers]
    multiplied = [int(n[0]) * int(n[1]) for n in numbers]
    total = sum(multiplied)
    print(f'Total multiplied numbers: {total}')





def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.read()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
