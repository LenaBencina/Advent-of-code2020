# part1
with open('input1.txt', 'r') as input:
    num_list = [int(line) for line in input]


def get_two_nums(num_list):
    for i in num_list:
        for j in num_list:
            if i + j == 2020:
                return i * j


print(get_two_nums(num_list))


# part2
def get_three_nums(num_list):
    for i in num_list:
        for j in num_list:
            for g in num_list:
                if i + j + g == 2020:
                    return i * j * g


print(get_three_nums(num_list))
