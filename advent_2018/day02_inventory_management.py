#!/usr/bin/env python

# Day 2: Inventory Management System
# For problem description see: https://adventofcode.com/2018/day/2

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2019, Krzysztof Kutt"


def count_letters(box_id):
    '''
    Count letters in box_id
    :param box_id: Input string
    :return: True/False if there is a letter that appear twice and thrice
    '''
    # parse string
    sums = dict()
    for letter in box_id:
        if letter in sums:
            sums[letter] += 1
        else:
            sums[letter] = 1

    # check results
    twice = False
    thrice = False
    for count in sums.values():
        if count == 2:
            twice = True
        elif count == 3:
            thrice = True
    return twice, thrice


def part_one():
    '''
    Part one: (IDs with letters count == 2) * (IDs with letters count == 3)
    :return: the multiplication of boxes' counts
    '''
    count2 = 0
    count3 = 0
    for line in open('day02.in'):
        curr2, curr3 = count_letters(line)
        count2 += int(curr2)
        count3 += int(curr3)
    return count2 * count3


def count_difference(id1, id2):
    '''
    Check whether two IDs differ only on one place
    :param id1: ID
    :param id2: ID
    :return: True if id1 and id2 differ only on one place
    '''
    diffs = 0
    id12 = zip(id1, id2)
    for x, y in id12:
        if x != y:
            diffs += 1
            if diffs > 1:
                return False
    if diffs == 1:
        return True
    return False


def common_letters(id1, id2):
    '''
    Returns common letters in two IDs
    :param id1: ID
    :param id2: ID
    :return: String with common letters
    '''
    res = ""
    id12 = zip(id1, id2)
    for x, y in id12:
        if x == y:
            res += x
    return res


def part_two():
    '''
    Part two: Find two IDs that differ only on one place.
    There is only ONE such pair
    :return: Letters that are common between the two found IDs
    '''
    previous_ids = []
    for line in open('day02.in'):
        for prev in previous_ids:
            if count_difference(line, prev):
                return common_letters(line, prev)
        previous_ids.append(line)
    return None


if __name__ == '__main__':
    # print(part_one())
    print(part_two())
