# -*- encoding: utf-8 -*-
'''
Created on 2014-05-13 13:38:00

@author: xun.ms
'''


def queen(n=8, columns=[]):
    if len(columns) == n:
        yield columns
    for column in nextCol(columns, n):
        newColumns = columns + [column]
        for que in queen(n, newColumns):
            yield que


def nextCol(current, n=8):
    length = len(current)
    if length == n:
        return
    ls = \
        [(val + length - i, val - length + i) for i, val in enumerate(current)]
    print(ls)
    dangerous = current + \
        [item for l in ls for item in l if item >= 0 and item <= n]
    for i in range(n):
        if i not in dangerous:
            yield i


def fullQueen(column=[]):
    length = len(column)
    fullQueen = []
    for row in column:
        fullRow = []
        for col in range(length):
            if col == row:
                fullRow += [1]
            else:
                fullRow += [0]
        fullQueen += [fullRow]
    return fullQueen

if __name__ == '__main__':
    count = 1
    for solution in queen(4):
        print('count: ', count)
        print('rows: ')
        print(solution)
        print('full:')
        for row in fullQueen(solution):
            print(row)
        count += 1
    import sys
    sys.exit()
