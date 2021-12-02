from aoc import DAY, timer, read_input, read_test

@timer
def part1(data):
    return sum([data[i] > data[i-1] for i in range(len(data))])

@timer
def part2(data):
    return sum([(data[i] + data[i+1] + data[i+2]) > (data[i-1] + data[i] + data[i+1]) for i in range(len(data)-2)])

if __name__ == "__main__":
    test_data, expected = read_test(1, cast=int)
    assert part1(test_data) == expected[0] 
    data = read_input(cast=int)
    part1(data)
    part2(data)
