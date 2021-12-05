from aoc import DAY, timer, read_input, read_test
from collections import defaultdict

@timer
def part1(data):
    rows = len(data)
    cols = len(data[0])
    counts = defaultdict(int)
    for row in data:
        for x in range(cols):
            counts[x] += int(row[x])
    binary = ''.join([str(int(v > rows/2)) for v in counts.values()])
    x = int(binary, 2)
    return x * (x ^ (2**cols)-1)


if __name__ == "__main__":
    data, expected = read_test(1)
    assert part1(data) == int(expected[0])
    data = read_input()
    part1(data)