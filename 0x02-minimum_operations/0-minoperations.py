#!/usr/bin/python3
''' task 0: module which contains minimum operations function '''


def minOperations(n):
    ''' calculate the fewest number of operations needed
        to result in exactly n H characters in the file
        args:
            n: repetitions of H
        returns:
            number of operations (Copy & Paste) to reach n Hs
    '''
    ops = 0
    sum = 1
    carrier = 0
    while sum < n:
        if n % sum == 0:  # Copy when summation is a multiple of n
            carrier = sum
            sum *= 2
            ops += 1
        else:
            sum += carrier
        ops += 1  # Always paste

    return ops
