#!/usr/bin/python3
''' Show list of lists of integers representing the Pascal's triangle of n '''


def pascal_triangle(n):
    '''
    Create a list of lists of integers representing
    the Pascal's triangle of a given integer
    '''
    # return an empty array for n less than 0
    if n <= 0:
        return []

    # initialize the triangle as a 2d array with a single value 1
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
