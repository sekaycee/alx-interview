#!/usr/bin/python3
''' Rotate 2D Matrix '''


def rotate_2d_matrix(matrix):
    ''' Given an n x n 2D matrix, rotate it 90 degrees clockwise. '''
    rows = len(matrix)
    for row in range(int(rows / 2)):
        offset = 0
        i = rows - 1 - row
        for column in range(row, i  ):
            top = matrix[row][column]
            matrix[row][column] = matrix[i - offset][row]
            matrix[i - offset][row] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[column][i]
            matrix[column][i] = top
            offset += 1
