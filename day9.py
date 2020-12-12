import collections


def day9_part1(lines):
    numbers = parse_lines_into_numbers(lines)
    return find_violating_number(numbers)

def day9_part2(lines):
    numbers = parse_lines_into_numbers(lines)
    target = find_violating_number(numbers)
    array = find_contiguous_array_summing_to_target(numbers, target)
    return min(array) + max(array)


def parse_lines_into_numbers(lines):
    numbers = [int(line.strip()) for line in lines if (len(line.strip()) != 0)]
    return numbers


def find_violating_number(numbers):
    for n_index in range(0, len(numbers) - 26):
        preamble = numbers[n_index: n_index + 25]
        target = numbers[n_index + 25]
        if not do_any_two_numbers_sum_to_target(preamble, target):
            return target


def do_any_two_numbers_sum_to_target(numbers, target):
    for i_index, i in enumerate(numbers):
        for j_index, j in enumerate(numbers):
            if i_index != j_index and i + j == target:
                return True
    return False

def find_contiguous_array_summing_to_target(numbers, target):
    current_sum = 0
    current_numbers = collections.deque()
    for i in numbers:
        current_sum += i
        current_numbers.append(i)
        if current_sum == target:
            return current_numbers
        while current_sum > target:
            removed = current_numbers.popleft()
            current_sum -= removed
            if current_sum == target:
                return current_numbers
