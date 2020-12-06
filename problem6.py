from problem4 import prepare_input

# import input by using the function from problem4
answers_all = prepare_input('input6.txt')

get_num_correct_answers = {1: lambda group: (len(set(group.replace('\n', '')))),
                           2: lambda group: (len(set.intersection(*map(set, group.split('\n')))))}

print(sum([get_num_correct_answers[1](group) for group in answers_all]))  # part1
print(sum([get_num_correct_answers[2](group) for group in answers_all]))  # part2
