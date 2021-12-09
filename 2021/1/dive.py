#!/usr/bin/python3

list = []
with open('input.txt', encoding='utf8') as input:
    for line in input:
        list.append(line.strip())


def calculatePosition(list):
    hor = depth = pos = 0
    for instruction in list:
        data = instruction.split(' ')
        direction = data[0]
        unit = int(data[1])
        if direction == 'forward':
            hor += unit
        elif direction == 'down':
            depth += unit
        elif direction == 'up':
            depth -= unit
    pos = hor * depth
    return pos


def calculatePositionWithAim(list):
    aim = hor = depth = pos = 0
    for instruction in list:
        direction = instruction.split(' ')[0]
        unit = int(instruction.split(' ')[1])
        if direction == 'forward':
            hor += unit
            depth += aim * unit
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit
    pos = hor * depth
    return pos

