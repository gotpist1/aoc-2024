import re
from os import environ


def get_reports(input_list):
    reports = list()
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    for line in scrubbed:
        levels = line.split(' ')
        reports.append([int(level) for level in levels])
    return reports

def get_sorted_reports(reports):
    safe_list = list()
    unsafe_dict = {}
    count = 0
    print('------------------')
    for report in reports:
        safe = True
        operator = None
        for i in range(len(report)):
            one_ahead = i + 1
            if one_ahead > len(report) - 1:
                break
            curr = report[i]
            if not curr - 3 <= report[one_ahead] <= curr + 3:
                unsafe_dict[count] = one_ahead
                safe = False
                break
            else:
                if report[one_ahead] > curr:
                    curr_operator = '+'
                elif report[one_ahead] < curr:
                    curr_operator = '-'
                else:
                    curr_operator = '='
            if operator is None:
                operator = curr_operator
            else:
                if operator != curr_operator or curr_operator == '=':
                    unsafe_dict[count] = one_ahead
                    safe = False
                    break
        if safe:
            safe_list.append(report)
        count += 1
        print(f'Report: {report} safe: {safe}')
    return safe_list, unsafe_dict


def getSolutionPart1(input_list):
    reports = get_reports(input_list)
    safe_list, _ = get_sorted_reports(reports)
    print(f'Total safe reports: {len(safe_list)}')





def getSolutionPart2(input_list):
    reports = get_reports(input_list)
    safe_list, unsafe_dict = get_sorted_reports(reports)
    dampener_applied = list()
    for count, _ in unsafe_dict.items():
        unsafe_report = reports[count]
        for i in range(len(unsafe_report)):
            unsafe_report_copy = unsafe_report.copy()
            unsafe_report_copy.pop(i)
            safe_list2, _ = get_sorted_reports([unsafe_report_copy])
            if len(safe_list2) > 0:
                dampener_applied.append(unsafe_report)
                break
    merged = dampener_applied + safe_list
    print(f'Total merged reports: {len(merged)}')



def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
