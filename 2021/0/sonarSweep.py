#!/usr/bin/python3
import unittest

list = []
with open('input.txt', encoding='utf8') as input:
    for line in input:
        list.append(int(line.strip()))


def countIncrements(list):
    count = 0
    previous = None
    for current in list:
        if previous and current > previous:
            count += 1
        previous = current
    return count


def countIncrementsSliding(list, step=3):
    count = 0
    previous = None
    stop = (len(list)-(step-1))
    for index in range(0, stop):
        current = sum(list[index:index+step])
        if previous and current > previous:
            count += 1
        previous = current
    return count

