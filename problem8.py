import copy

# prepare a list of instructions
def get_original_instructions(file_name):
    with open(file_name, 'r') as input_file:
        instructions = []
        for instruction in input_file:
            instruction_list = instruction.strip('\n').split()
            instructions.append({'operation': instruction_list[0], 'argument': int(instruction_list[1])})
    return instructions


# function for getting global value
def execute_accumulator(instructions):
    # initialize
    position, global_value = 0, 0
    visited = [False] * len(instructions)  # for following visited

    # execute until all are visited once
    while not visited[position]:

        operation, value = instructions[position]['operation'], instructions[position]['argument']

        # mark used instruction
        visited[position] = True

        if operation == 'nop':
            position = position + 1

        elif operation == 'acc':
            global_value = global_value + value
            position = position + 1  # go to next one

        elif operation == 'jmp':
            position = position + value  # jump

        if position == len(instructions):
            return {'value': global_value, 'terminates': True}

    test = visited[position]
    return {'value': global_value, 'terminates': False}


# part1
original_instructions = get_original_instructions('input8.txt')
print(execute_accumulator(original_instructions)['value'])


# part2
def get_value_for_finite_version_of_instructions(original_instructions):

    current_instruction_position = 0
    instructions = copy.deepcopy(original_instructions) # save original dict

    for instruction in original_instructions:

        operation = instruction['operation']

        # rewrite ONE operator (nop or jmp)
        if operation == 'nop':
            instructions[current_instruction_position].update(operation='jmp')

        elif operation == 'jmp':
            instructions[current_instruction_position].update(operation='nop')

        # check if i-th version of instruction terminates
        execution_result = execute_accumulator(instructions)
        if execution_result['terminates']:
            return execution_result['value']
        else:
            current_instruction_position = current_instruction_position + 1
            instructions = copy.deepcopy(original_instructions) # get original again
            continue


print(get_value_for_finite_version_of_instructions(original_instructions))
