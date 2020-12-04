import re

def prepare_input(file_name):
    # import file
    with open(file_name, 'r') as input_file:
        input_string = ''
        for line in input_file:
            input_string = input_string + line

    # split
    passports = input_string.split('\n\n')
    return passports




def convert_list_to_dict(passport_list):

    passport_dict = {}

    for element in passport_list:

        element = element.split(':')
        key, value = element[0], element[1]
        passport_dict[key] = value

    return passport_dict



def validate_passport1(passport_dict):


    # if missing attributes
    if len(passport_dict.keys()) < 7:
        return False

    # if only one missing, but not the optional one (i.e 'cid')
    if len(passport_dict.keys()) == 7 and ('cid' in passport_dict.keys()):
        return False

    # else
    return True


def validate_passport2(passport_dict):

    testing = passport_dict['hgt']

    # byr (Birth Year) - four digits; at least 1920 and at most 2002
    if not (1920 <= int(passport_dict['byr']) <= 2002):
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020
    if not (2010 <= int(passport_dict['iyr']) <= 2020):
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    if not (2020 <= int(passport_dict['eyr']) <= 2030):
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193
    hgt_num_list = re.findall(pattern='^[0-9]+', string=passport_dict['hgt'])
    hgt_num_int = int(''.join(map(str, hgt_num_list))) # convert [1,2,3] to 123

    if 'cm' in passport_dict['hgt']:
        if not (150 <= hgt_num_int <= 193):
            return False

    # If in, the number must be at least 59 and at most 76
    if 'in' in passport_dict['hgt']:
        if not (59 <= hgt_num_int <= 76):
            return False

    if 'in' not in passport_dict['hgt'] and 'cm' not in passport_dict['hgt']:
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    if not re.match(pattern=r'^#[0-9a-f]{6}$', string=passport_dict['hcl']):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    if passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes
    if not re.match(pattern='[0-9]{9}$', string=passport_dict['pid']):
        return False

    # if all True
    return True



def count_validated_passports(passports, part):

    validated_count1 = 0
    validated_count2 = 0

    for passport in passports:

        # tidy
        passport = passport.replace('\n', ' ')
        passport_list = passport.split(' ')

        # convert to dict
        passport_dict = convert_list_to_dict(passport_list)

        # validate
        if validate_passport1(passport_dict):
            validated_count1 = validated_count1 + 1

            # part2
            if validate_passport2(passport_dict):
                validated_count2 = validated_count2 + 1


    return {1:validated_count1, 2:validated_count2}[part]




passports = prepare_input('input4.txt')
print(count_validated_passports(passports, part=1))
print(count_validated_passports(passports, part=2))



