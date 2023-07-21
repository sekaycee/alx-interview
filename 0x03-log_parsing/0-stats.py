#!/usr/bin/python3
''' read stdin line by line and compute metrics '''
import sys


def print_status(dic, size):
    ''' print information '''
    print('File size: {:d}'.format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print('{}: {:d}'.format(i, dic[i]))


# sourcery skip: use-contextlib-suppress
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_codes, size)

        st_list = line.split()
        count += 1

        try:
            size += int(st_list[-1])
        except Exception:
            pass

        try:
            if st_list[-2] in status_codes:
                status_codes[st_list[-2]] += 1
        except Exception:
            pass
    print_status(status_codes, size)


except KeyboardInterrupt:
    print_status(status_codes, size)
    raise
