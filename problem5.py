import math
import re





def get_parameters(boarding_pass, row):

    if row:
        return ''.join(re.findall(pattern='[FB]', string=boarding_pass)).replace('F', 'L').replace('B', 'U')

    else:
        return ''.join(re.findall(pattern='[LR]', string=boarding_pass)).replace('R', 'U')



def get_row_or_column(chars):

    # initialize
    l = 0
    u = 2 ** len(chars) - 1
    m = None

    for i in chars:

        # calculate middle of the interval
        m = l + (u - l) / 2

        if i == 'L':
            u = math.floor(m)

        if i == 'U':
            l = math.ceil(m)


    if l != u:
        print('sth is wrong')

    return l


def get_all_ids(file_name):
    with open(file_name, 'r') as input_file:

        ids = list()

        for line in input_file:

            # get row and column
            row = get_row_or_column(get_parameters(line, row=True))
            column = get_row_or_column(get_parameters(line, row=False))

            # add current id
            ids.append(row * 8 + column)

        return(ids)


ids = get_all_ids('input5.txt')

# part1

def get_id1(ids):
    return max(ids)

print(get_id1(ids))

# part2

def get_id2(ids):

    ids.sort()

    for i in range(len(ids)-1):
        if ids[i+1] - ids[i] != 1: # if the difference is not 1
            return(ids[i] + 1)


print(get_id2(ids))








