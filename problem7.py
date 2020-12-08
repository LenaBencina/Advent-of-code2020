import re

################################################################################################
# FIRST TRY FOR PREPARING DICTIONARY OF RULES - not very pretty
# # additional function
# def get_value(value_string):
#     if value_string == 'no other':
#         return None  # no color
#     splited_rule_one_part = value_string.split(" ", 1)  # split at first space
#     count, color = splited_rule_one_part[0], splited_rule_one_part[1]
#     return {'color': color, 'count': int(count)}
#     # return {color: count}
#
#
# # prepare a dictionary with rules
# rules_dict = {}
# with open("input7.txt", 'r') as input_file:
#     for line in input_file:
#         line = line.strip('.\n').replace(', ', ',') # remove \n and space after commas
#         bags_string = re.sub(r'\b bag[s]?\b', '', line)
#         bags_list = bags_string.split(' contain ')
#
#         bag_content = list(map(get_value, bags_list[1].split(',')))  # list of strings
#
#         if bag_content[0] == None:  # if contains no color
#             continue
#
#         rules_dict[bags_list[0]] = bag_content
################################################################################################




# prepare a dictionary with rules

regex = re.compile(r'(\d)?(.+)bag[s]?')  # define regex for getting number of bags and color name
rules_dict = {}  # initialize dict for all the rules

with open("input7.txt", 'r') as input_file:
    for rule in input_file:
        rule_splited = re.split(',|contain', rule)  # split line on comma or 'contain'

        containing_bags = []  # preparing value (dict for containing bags) for main dict
        for bag_info in rule_splited:  # for each bag in one rule
            regex_match = regex.match(bag_info.strip())  # match regex and remove whitespace
            number_of_bags = regex_match.group(1)  # save number
            bag_color = regex_match.group(2).strip()  # save color name

            # if no match for number (main bag or 'no other' bag)
            if not number_of_bags:

                # if 0 bags inside go to the next one
                if 'no other' in bag_color:
                    continue

                # if main (container) bag rewrite for adding into dict later
                main_bag_color = bag_color
            else:
                containing_bags.append({'color': bag_color, 'count': int(number_of_bags)})

        # if bag contains other bags add new rule
        if len(containing_bags) > 0:
            rules_dict[main_bag_color] = containing_bags




# part1
def contains_shiny_gold(current_color):
    # ending condition
    if current_color == 'shiny gold':
        return True
    if current_color not in rules_dict:
        return False

    for color in rules_dict[current_color]:
        if contains_shiny_gold(color['color']):
            return True

    # when no relation to shiny gold
    return False


final_number = 0
for current_color in rules_dict:

    if current_color == 'shiny gold':
        continue  # skip

    if contains_shiny_gold(current_color):  # returns true or false
        final_number = final_number + 1

print(final_number)





# part2
def count_colors_one_bag(bag_color):
    colors_count = 0

    if bag_color not in rules_dict:
        return colors_count

    current_bag = rules_dict[bag_color]
    for bag in current_bag:
        tmp_colors_count = bag['count'] + bag['count'] * count_colors_one_bag(bag['color'])
        colors_count = colors_count + tmp_colors_count

    # when no more bags, exit with total count
    return colors_count


print(count_colors_one_bag('shiny gold'))
