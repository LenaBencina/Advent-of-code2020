# part1
def validate_password1(passwords_with_policies):
    policy_occurrences = passwords_with_policies[0].split('-')
    min_occurences, max_occurences = int(policy_occurrences[0]), int(policy_occurrences[1])
    policy_letter = passwords_with_policies[1].replace(':', '')
    password = passwords_with_policies[2]
    number_of_occurrences = password.count(policy_letter)

    if min_occurences <= number_of_occurrences <= max_occurences:
        return True
    else:
        return False


# part2
def validate_password2(passwords_with_policies):
    policy_occurrences = passwords_with_policies[0].split('-')
    position1, position2 = int(policy_occurrences[0]), int(policy_occurrences[1])
    policy_letter = passwords_with_policies[1].replace(':', '')
    password = passwords_with_policies[2]

    match1 = password[position1-1] == policy_letter
    match2 = password[position2-1] == policy_letter

    if match1 + match2 == 1: # True + False or False + True
        return True
    else:
        return False


# count validated passwords (both parts)
def count_correct_passwords(file_name, part):
    validate_password = [validate_password1, validate_password2]
    counter = 0
    with open(file_name, 'r') as input_file:
        for line in input_file:
            passwords_with_policies = line.strip('\n').split(' ')
            validated = validate_password[part - 1](passwords_with_policies)
            if validated:
                counter = counter + 1

        return counter


print(count_correct_passwords('input2.txt', part=1))
print(count_correct_passwords('input2.txt', part=2))

