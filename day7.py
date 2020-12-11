import re
from collections import defaultdict


def day7_part1(lines):
    bags = preprocess_lines_into_bags(lines)
    answer = set()

    def search(color):
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                search(b)

    search('shiny gold')
    return len(answer)


def day7_part2(lines):
    bags = preprocess_lines_into_bags(lines)

    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count

    return search('shiny gold') - 1  # Rm one for shiny gold itself


def preprocess_lines_into_bags(lines):
    bags = defaultdict(dict)
    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = int(count)
    return bags
