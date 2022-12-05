crate_row = []
crate_stacks = []
total_moves = []
new_crate_stacks = []
new_model_crate_stacks = []


with open('day5_input.txt', 'r') as file:
    for line in file:
        if line[0] == '[':         # get stack configurations
            newline = line.find('\n')
            for i in range(9):
                if 4*i+1 < newline:
                    crate_row.append(line[4*i+1])
                else:
                    crate_row.append(' ')       # signals no box in this location
            crate_stacks.append(crate_row)
            crate_row = []
        elif line[0] == 'm':        # get instructions for move
            moves = [int(s) for s in line.split() if s.isdigit()]
            total_moves.append(moves)

# invert 2-dimentional list (easier to do operations below)
new_crate_stacks_tuple = list(zip(*crate_stacks))
for row in new_crate_stacks_tuple:
    row_list = list(row)
    new_crate_stacks.append(row_list)
    new_model_crate_stacks.append(row_list)

# remove spaces as they are no longer needed
for idx in range(len(new_crate_stacks)):
    new_crate_stacks[idx] = [i for i in new_crate_stacks[idx] if i != ' ']
    new_model_crate_stacks[idx] = [i for i in new_crate_stacks[idx] if i != ' ']

# moving day
for each_move in total_moves:
    for i in range(each_move[0]):
        moving = new_crate_stacks[each_move[1]-1].pop(0)
        new_crate_stacks[each_move[2]-1].insert(0, moving)

top_shelf = ''
for stack in new_crate_stacks:
    top_shelf += stack[0]

###############################

# moving day...again
for each_move in total_moves:
    for i in range(each_move[0], 0, -1):
        moving = new_model_crate_stacks[each_move[1]-1].pop(i-1)
        new_model_crate_stacks[each_move[2]-1].insert(0, moving)

new_top_shelf = ''
for stack in new_model_crate_stacks:
    new_top_shelf += stack[0]

print(f'The top of the shelves is {top_shelf}.')
print(f'The new top of shelves is {new_top_shelf}.')