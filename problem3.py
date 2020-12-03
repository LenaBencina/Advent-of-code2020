def prepare_grid(file_name):

    with open(file_name, 'r') as input_file:
        grid = list()

        for line in input_file:
            line = line.strip('\n')
            grid.append(line)

        return grid


def get_number_of_trees(grid, steps_right, steps_down):

    # define height and weight of the grid
    height = len(grid)  # 323
    width = len(grid[0]) - 1  # 30

    # initialize
    col = 0
    tree_count = 0

    for row in range(0, height, steps_down):  # for each row

        current_position = grid[row][col]

        if current_position == '#':
            tree_count = tree_count + 1

        # moving through columns by 3
        col = col + steps_right

        if col > width:  # if out of grid
            col = col - width - 1  # go to beginning (-1 because of 0 index for first col)

    return (tree_count)


grid = prepare_grid('input3.txt')

# part1
print(get_number_of_trees(grid, steps_right=3, steps_down=1))

# part2
multiplied = 1
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:  # for different slopes
    tree_count = get_number_of_trees(grid, steps_right=right, steps_down=down)
    multiplied = multiplied * tree_count
print(multiplied)