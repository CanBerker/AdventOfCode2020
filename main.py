if __name__ == '__main__':
    # https://adventofcode.com/2020

    # from day1 import *
    # print(f"day1-part1 result: {day1_part1(day1_input)}")
    # print(f"day1-part2 result: {day1_part2(day1_input)}")

    # from day2 import *
    # print(f"day2-part1 result: {day2_part1(day2_input)}")
    # print(f"day2-part2 result: {day2_part2(day2_input)}")

    # from day3 import *
    # right_amount, down_amount = 3, 1
    # print(f"day3-part1 result: {day3_part1(day3_input, right_amount, down_amount)}")
    # amounts = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    # print(f"day3-part1 result: {day3_part2(day3_input, amounts)}")

    # from day4 import *
    # file1 = open('day4input.txt', 'r')
    # lines = file1.readlines()
    # mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #cid is optional
    # print(f"day4-part1 result: {day4_part1(lines, mandatory_fields)}")
    # print(f"day4-part2 result: {day4_part2(lines, mandatory_fields)}")

    # from day5 import *
    # file1 = open('day5input.txt', 'r')
    # lines = file1.readlines()
    # print(f"day5-part1 result: {day5_part1(lines)}")
    # print(f"day5-part2 result: {day5_part2(lines)}")

    # from day6 import *
    # file1 = open('day6input.txt', 'r')
    # lines = file1.readlines()
    # print(f"day6-part1 result: {day6_part1(lines)}")
    # print(f"day6-part2 result: {day6_part2(lines)}")

    from day7 import *

    file1 = open('day7input.txt', 'r')
    lines = file1.readlines()
    print(f"day7-part1 result: {day7_part1(lines)}")
    print(f"day7-part2 result: {day7_part2(lines)}")

    pass
