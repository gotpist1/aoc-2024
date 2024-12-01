def flatten(l):
    return [item for sublist in l for item in sublist]


def groupBy(key_lambda, list_to_be_grouped):
    g = list(map(key_lambda, list_to_be_grouped))
    empty_array_map = {entry[0]: [] for entry in g}
    for entry in g:
        empty_array_map[entry[0]].append(entry[1])
    return empty_array_map
