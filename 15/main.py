import os
import re


def no_beacon_positions(pos, sensor_x, sensor_y, beacon_x, beacon_y):
    distance_x = abs(sensor_x - beacon_x)
    distance_y = abs(sensor_y - beacon_y)
    distance = distance_x + distance_y

    print(distance_x, distance_y, distance)
    for x in range(sensor_x - distance, sensor_x + distance):
        current_distance_x = abs(x - sensor_x)
        range_y = distance - current_distance_x
        for y in range(sensor_y - range_y, sensor_y + range_y + 1):
            pos.append((x, y))

    if (beacon_x, beacon_y) in pos:
        pos.remove((beacon_x, beacon_y))


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    with open(input_path) as f:
        data = f.read().splitlines()
        no_beacon_pos = []
        for line in data:
            match = re.search(r'^.*x=([+-]?\d+), y=([+-]?\d+).*x=([+-]?\d+), y=([+-]?\d+)$', line)  # noqa 501
            if match is not None:
                print(line)
                sensor_x = int(match[1])
                sensor_y = int(match[2])
                beacon_x = int(match[3])
                beacon_y = int(match[4])
                no_beacon_positions(no_beacon_pos, sensor_x, sensor_y, beacon_x, beacon_y)  # noqa 501

    line_to_check = 2000000
    no_beacon_pos_on_y = [pos for pos in no_beacon_pos if pos[1] == line_to_check]  # noqa 501
    print(len(no_beacon_pos_on_y))


if __name__ == '__main__':
    main()
