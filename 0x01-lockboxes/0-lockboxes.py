#!/usr/bin/python3
'''
With n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    ''' Check if all boxes can be unlocked '''
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    for i in range(n):
        if unlocked[i]:
            for key in boxes[i]:
                if key < n and not unlocked[key]:
                    unlocked[key] = True
                    keys.extend(boxes[key])

    return all(unlocked)
