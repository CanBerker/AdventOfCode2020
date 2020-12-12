import copy


def day8_part1(lines):
    instructions = parse_lines_to_instructions(lines)
    terminated, accumulator = execute_instructions(instructions)
    # terminates is false here
    return accumulator


def day8_part2(lines):
    instructions = parse_lines_to_instructions(lines)
    for i in range(len(instructions)):
        # Copy instructions so that changes don't persist.
        local_instructions = copy.deepcopy(instructions)
        # Switch statement jmp/nop
        command = local_instructions[i]['command']
        if command == 'jmp':
            local_instructions[i]['command'] = 'nop'
        elif command == 'nop':
            local_instructions[i]['command'] = 'jmp'

        terminated, result = execute_instructions(local_instructions)

        if terminated:
            return result


def parse_lines_to_instructions(lines):
    instructions = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        command, value = line.split(' ')

        value = int(value)
        instructions.append({
            'command': command,
            'value': value
        })
    return instructions


def execute_instructions(instructions):
    accumulator = 0
    current_instruction_index = 0
    visited = set()
    visited.add(0)
    while True:
        instruction = instructions[current_instruction_index]
        current_instruction_index += get_instruction_index_change(instruction)

        if current_instruction_index in visited:
            return False, accumulator
        visited.add(current_instruction_index)

        if instruction['command'] == 'acc':
            accumulator += instruction['value']

        if current_instruction_index == len(instructions):
            return True, accumulator


def get_instruction_index_change(instruction):
    command = instruction['command']
    if command == 'jmp':
        return instruction['value']
    return +1
