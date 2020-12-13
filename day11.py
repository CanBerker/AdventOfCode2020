import copy


def day11_part1(lines):
    lines = clean_input(lines)
    prev_state = copy.deepcopy(lines)
    next_state = copy.deepcopy(prev_state)
    converged = False
    while not converged:
        converged = True
        for line_ind, line in enumerate(prev_state):
            for seat_ind, seat in enumerate(line):
                if seat == '.':
                    continue
                if seat == 'L' and should_fill_vacant_seat(prev_state, line_ind, seat_ind):
                    next_state[line_ind][seat_ind] = '#'
                    converged = False
                    continue
                if seat == '#' and should_vacate_filled_seat(prev_state, line_ind, seat_ind):
                    next_state[line_ind][seat_ind] = 'L'
                    converged = False
                    continue

        prev_state = next_state
        next_state = copy.deepcopy(prev_state)
    return count_filled_seats(next_state)


def should_fill_vacant_seat(state, line_ind, seat_ind):
    adjacent_seats = get_adjacent_seats(state, line_ind, seat_ind)
    if '#' not in adjacent_seats:
        return True
    return False


def should_vacate_filled_seat(state, line_ind, seat_ind):
    adjacent_seats = get_adjacent_seats(state, line_ind, seat_ind)
    if len([seat for seat in adjacent_seats if seat == '#']) >= 4:
        return True
    return False


def get_adjacent_seats(state, line_ind, seat_ind):
    adjacent_seats = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if is_current_seat(i, j):
                continue
            row_adjacent = line_ind + i
            seat_adjacent = seat_ind + j
            if is_out_of_bounds(state, row_adjacent, seat_adjacent):
                continue
            adjacent_seats.append(state[row_adjacent][seat_adjacent])
    return adjacent_seats


def day11_part2(lines):
    lines = clean_input(lines)
    prev_state = copy.deepcopy(lines)
    next_state = copy.deepcopy(prev_state)
    converged = False
    while not converged:
        converged = True
        for line_ind, line in enumerate(prev_state):
            for seat_ind, seat in enumerate(line):
                if seat == '.':
                    continue
                if seat == 'L' and part2_should_fill_vacant_seat(prev_state, line_ind, seat_ind):
                    next_state[line_ind][seat_ind] = '#'
                    converged = False
                    continue
                if seat == '#' and part2_should_vacate_filled_seat(prev_state, line_ind, seat_ind):
                    next_state[line_ind][seat_ind] = 'L'
                    converged = False
                    continue

        prev_state = next_state
        next_state = copy.deepcopy(prev_state)
    return count_filled_seats(next_state)


def clean_input(lines):
    return list(map(list, map(str.strip, lines)))


def part2_should_fill_vacant_seat(state, line_ind, seat_ind):
    adjacent_seats = get_visible_seats(state, line_ind, seat_ind)
    if '#' not in adjacent_seats:
        return True
    return False


def part2_should_vacate_filled_seat(state, line_ind, seat_ind):
    adjacent_seats = get_visible_seats(state, line_ind, seat_ind)
    if len([seat for seat in adjacent_seats if seat == '#']) >= 5:
        return True
    return False


def get_visible_seats(state, line_ind, seat_ind):
    visible_seats = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if is_current_seat(i, j):
                continue

            visible_seat = get_visible_seat_or_none(state, line_ind, seat_ind, i, j)
            if visible_seat is not None:
                visible_seats.append(visible_seat)
    return visible_seats


def get_visible_seat_or_none(state, line_ind, seat_ind, i, j):
    distance = 0
    while True:
        distance += 1
        row_visible = line_ind + (i * distance)
        seat_visible = seat_ind + (j * distance)
        if is_out_of_bounds(state, row_visible, seat_visible):
            return None
        visible_seat = state[row_visible][seat_visible]
        if visible_seat in ['#', 'L']:
            return state[row_visible][seat_visible]


def is_current_seat(i, j):
    return i == 0 and j == 0


def is_out_of_bounds(state, row_adjacent, seat_adjacent):
    return row_adjacent < 0 or seat_adjacent < 0 or row_adjacent >= len(state) or seat_adjacent >= len(state[0])


def count_filled_seats(next_state):
    filled_seat_count = 0
    for row in next_state:
        for seat in row:
            if seat == '#':
                filled_seat_count += 1

    return filled_seat_count
