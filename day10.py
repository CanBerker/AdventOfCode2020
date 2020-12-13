import copy
import heapq

def day10_part1(lines):
    numbers = parse_lines_into_numbers(lines)

    heap = copy.deepcopy(numbers)
    heapq.heapify(heap)

    current_val = 0  # root outlet
    count_of_one_difference = 0
    count_of_three_difference = 0
    while len(heap) > 0:
        next_val = heapq.heappop(heap)
        diff = next_val - current_val
        if diff == 1:
            count_of_one_difference += 1
        if diff == 3:
            count_of_three_difference += 1
        current_val = next_val

    count_of_three_difference += 1  # reaching final device
    result = count_of_one_difference * count_of_three_difference
    print(count_of_one_difference, count_of_three_difference, result)
    return result


def day10_part2(lines):
    numbers = parse_lines_into_numbers(lines)
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort(reverse=True)
    path_count_cache = {}

    def calculate_all_paths_to(target):
        if target == len(numbers) - 1:
            return 1

        if target in path_count_cache:
            return path_count_cache[target]

        path_count = 0
        for i in range(target + 1, len(numbers)):
            if abs(numbers[i] - numbers[target]) <= 3:
                path_count += calculate_all_paths_to(i)

        path_count_cache[target] = path_count
        return path_count

    return calculate_all_paths_to(0)


def parse_lines_into_numbers(lines):
    numbers = [int(line.strip()) for line in lines if (len(line.strip()) != 0)]
    return numbers
