import re
from os import environ


def get_sorted_lists(input_list):
    ll = list()
    rl = list()
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    for line in scrubbed:
        line2 = line.replace('   ', ' ')
        parts = line2.split()
        ll.append(int(parts[0]))
        rl.append(int(parts[1]))
    ll.sort()
    rl.sort()
    return ll, rl


def getSolutionPart1(input_list):
    ll, rl = get_sorted_lists(input_list)
    tuple_list = [(ll[i], rl[i]) for i in range(len(ll))]
    distances = list()
    for t in tuple_list:
        if t[0] > t[1]:
            distance = t[0] - t[1]
        else:
            distance = t[1] - t[0]
        distances.append(distance)
    total = sum(distances)
    print(f'Total distance for part 1: {total}')


def getSolutionPart2(input_list):
    ll, rl = get_sorted_lists(input_list)
    score_list = list()
    for i in range(len(ll)):
        occurrences = rl.count(ll[i])
        score_list.append(ll[i] * occurrences)
    print(f'Total score for part 2: {sum(score_list)}')


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
