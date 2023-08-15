#!/usr/bin/python3
''' Rotate 2D Matrix '''


def rotate_2d_matrix(matrix):
    ''' rotate a given n x n 2d matrix by 90 degrees clockwise. '''
    rows = len(matrix)
    for row in range(int(rows / 2)):
        offset = 0
        i = rows - 1 - row
        for col in range(row, i):
            tmp = matrix[row][col]
            matrix[row][col] = matrix[i - offset][row]
            matrix[i - offset][row] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[col][i]
            matrix[col][i] = tmp
            offset += 1
