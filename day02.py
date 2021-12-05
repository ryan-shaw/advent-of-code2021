from aoc import DAY, timer, read_input, read_test

def parse(data):
    return [(a, int(i)) for a, i in [x.split(' ') for x in data]]

@timer
def part1(data):
    h_pos, depth = 0, 0
    data = parse(data)
    for action, val in data:
        if action == 'forward': h_pos += val
        elif action == 'down': depth += val
        elif action == 'up': depth -= val
    return h_pos * depth

@timer
def part2(data):
    h_pos, depth, aim = 0, 0, 0
    data = parse(data)
    for action, val in data:
        if action == 'forward': 
            h_pos += val
            depth += val * aim
        elif action == 'down': aim += val
        elif action == 'up': aim -= val
    return h_pos * depth

if __name__ == '__main__':
    data, expected = read_test(1, cast=str)
    assert part1(data) == int(expected[0])
    data = read_input(cast=str)
    part1(data)

    data, expected = read_test(1, cast=str)
    assert part2(data) == 900
    data = read_input(cast=str)
    part2(data)