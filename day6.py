from functools import reduce


def day6_part1(lines):
    groups = preprocess_input_into_groups(lines)
    selections_of_groups = map(count_selections_of_group, groups)
    unique_selections_of_groups = map(dict.keys, selections_of_groups)
    counts_of_unique_selections = map(len, unique_selections_of_groups)
    return sum(counts_of_unique_selections)


def day6_part2(lines):
    groups = preprocess_input_into_groups(lines)
    selections_of_groups = map(count_selections_of_group, groups)
    unanimous_selection_counts = count_unanimous_selections(zip(groups, selections_of_groups))
    return sum(unanimous_selection_counts)


def preprocess_input_into_groups(lines):
    groups = []
    group = []
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) != 0:
            group.append(stripped_line)
            continue

        groups.append(group)
        group = []

    return groups


def count_selections_of_group(group):
    selections = {}
    for person in group:
        for selection in person:
            selections[selection] = selections.get(selection, 0) + 1

    return selections


def count_unanimous_selections(groups_with_selections):
    unanimous_selection_counts = []
    for group_with_selections in groups_with_selections:
        group, selections = group_with_selections
        group_size = len(group)
        unanimous_selection_count = 0
        for selection, selection_count in selections.items():
            if selection_count == group_size:
                unanimous_selection_count += 1
        unanimous_selection_counts.append(unanimous_selection_count)
    return unanimous_selection_counts
