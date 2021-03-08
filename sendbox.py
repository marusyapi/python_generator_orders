import math


def lcg(entry, multiplier, step, max):
    current = entry
    while True:
        next_entry = (current * multiplier + step) % max
        yield next_entry
        current = next_entry


sequence = iter(lcg(1, math.pi, math.e, 10))


if __name__ == '__main__':
    print([sequence.__next__() for i in range(0, 100)])
    ids = [hex(round(2000000000000 + i + sequence.__next__())) for i in range(0, 2000, 10)]

    print(ids)

