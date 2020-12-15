import enum
import math


class ClockWiseDirections(enum.Enum):
    E = 0  # East
    S = 1  # South
    W = 2  # West
    N = 3  # North


origin = (0, 0)


def day12_part1(lines):
    lines = clean_input(lines)

    ship_state = {
        'current_direction': ClockWiseDirections.E,
        'x_pos': 0,
        'y_pos': 0,
    }

    for line in lines:
        command, amount = line[0], int(line[1:])
        handle_command(ship_state, command, amount)

    return get_manhattan_distance(ship_state['x_pos'], ship_state['y_pos'])


def handle_command(ship_state, command, amount):
    if command == ClockWiseDirections.E.name:
        ship_state['x_pos'] += amount
    elif command == ClockWiseDirections.W.name:
        ship_state['x_pos'] -= amount
    elif command == ClockWiseDirections.N.name:
        ship_state['y_pos'] += amount
    elif command == ClockWiseDirections.S.name:
        ship_state['y_pos'] -= amount
    elif command == 'R':
        ship_state['current_direction'] = ClockWiseDirections(
            (ship_state['current_direction'].value + amount // 90) % len(ClockWiseDirections))
    elif command == 'L':
        ship_state['current_direction'] = ClockWiseDirections(
            (ship_state['current_direction'].value - amount // 90) % len(ClockWiseDirections))
    elif command == 'F':
        handle_command(ship_state, ship_state['current_direction'].name, amount)


def day12_part2(lines):
    lines = clean_input(lines)

    ship_state = {
        'x_waypoint': 10,
        'y_waypoint': 1,
        'x_pos': 0,
        'y_pos': 0,
    }

    for line in lines:
        command, amount = line[0], int(line[1:])
        handle_waypoint_command(ship_state, command, amount)

    return get_manhattan_distance(ship_state['x_pos'], ship_state['y_pos'])


def handle_waypoint_command(ship_state, command, amount):
    if command == ClockWiseDirections.E.name:
        ship_state['x_waypoint'] += amount
    elif command == ClockWiseDirections.W.name:
        ship_state['x_waypoint'] -= amount
    elif command == ClockWiseDirections.N.name:
        ship_state['y_waypoint'] += amount
    elif command == ClockWiseDirections.S.name:
        ship_state['y_waypoint'] -= amount
    elif command == 'R':
        ship_state['x_waypoint'], ship_state['y_waypoint'] = rotate(origin, (
            ship_state['x_waypoint'], ship_state['y_waypoint']), -amount)
    elif command == 'L':
        ship_state['x_waypoint'], ship_state['y_waypoint'] = rotate(origin, (
            ship_state['x_waypoint'], ship_state['y_waypoint']), amount)
    elif command == 'F':
        ship_state['x_pos'] += ship_state['x_waypoint'] * amount
        ship_state['y_pos'] += ship_state['y_waypoint'] * amount


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    angle = math.radians(angle)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)


def clean_input(lines):
    return list(map(str.strip, lines))


def get_manhattan_distance(x, y):
    return abs(x) + abs(y)
