def day5_part1(lines):
    rows_and_columns = preprocess_input_to_row_and_column(lines)
    seat_ids = map_to_seat_ids(rows_and_columns)
    return max(seat_ids)


def day5_part2(lines):
    rows_and_columns = preprocess_input_to_row_and_column(lines)
    seat_ids = map_to_seat_ids(rows_and_columns)
    sorted_seat_ids = sorted(seat_ids)
    return find_missing_id_in_sorted_consecutive_list(sorted_seat_ids)


def preprocess_input_to_row_and_column(lines):
    results = []
    for line in lines:
        binary_representation = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(binary_representation[:7], 2)
        column = int(binary_representation[7:], 2)
        results.append({"row": row, "column": column})
    return results


def find_missing_id_in_sorted_consecutive_list(sorted_seat_ids):
    for i in range(0, len(sorted_seat_ids) - 1):
        current_id = sorted_seat_ids[i]
        next_id = sorted_seat_ids[i + 1]
        if current_id + 1 != next_id:
            return current_id + 1
    return "Not found"


def map_to_seat_ids(rows_and_columns):
    return list(map(lambda entry: entry['row'] * 8 + entry['column'], rows_and_columns))
