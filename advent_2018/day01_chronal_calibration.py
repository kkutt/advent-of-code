#!/usr/bin/env python

# Day 1: Chronal Calibration
# For problem description see: https://adventofcode.com/2018/day/1

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2019, Krzysztof Kutt"


def part_one():
    '''
    Part one: find the sum of all numbers
    :return: the sum
    '''
    curr_val = 0
    for line in open('day01.in'):
        curr_val += int(line)
    return curr_val


def part_two():
    '''
    Part two: find the first repeat of the subtotal
    [go through the file over and over if necessary]
    :return: the searched subtotal
    '''
    curr_val = 0
    all_vals = {0}
    while True:
        for line in open('day01.in'):
            curr_val += int(line)
            if curr_val in all_vals:
                return curr_val
            all_vals.add(curr_val)


if __name__ == '__main__':
    # print(part_one())
    print(part_two())
