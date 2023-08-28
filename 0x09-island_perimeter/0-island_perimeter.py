#!/usr/bin/python3
''' island_perimeter module '''


def island_perimeter(grid):
    '''  return the perimeter of the island described in grid '''

    def edges(matrix):
        ''' detect number of edges along horizontal direction '''
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i-1]
        return count

    island = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            island[i].append(item)

    return edges(grid) + edges(island)
