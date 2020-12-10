
# prepare input in a list
with open('input9.txt', 'r') as input_file:
    numbers = [int(number) for number in input_file]



# prepare the sums in advance
def get_all_sums():
    sums = []
    for i in range(len(numbers)):
        tmp = []
        for j in range(len(numbers)):
            tmp.append(numbers[i] + numbers[j])
        sums.append(tmp)
    return sums



def get_first_number(step):

    sums = get_all_sums()
    position_checking_number = step

    for checking_number in numbers[step:]:
        is_sum = False
        valid_positions = range(position_checking_number - step, position_checking_number)
        for position_number1 in valid_positions:
            for position_number2 in valid_positions:
                if position_number1 == position_number2:
                    continue
                if checking_number == sums[position_number1][position_number2]:
                    is_sum = True
        if not is_sum:
            return {'number': checking_number, 'position': position_checking_number}

        position_checking_number = position_checking_number + 1


invalid_number = get_first_number(step=25)
print(invalid_number)


# part2
def get_encryption_weakness(invalid_number):
    last_valid_position = invalid_number['position'] - 1
    for position1 in range(last_valid_position+1):
        for position2 in range(position1+1, last_valid_position+1):
            current_set = numbers[position1:position2 + 1]
            if sum(current_set) == invalid_number['number']:
                return min(current_set) + max(current_set)


print(get_encryption_weakness(invalid_number))

