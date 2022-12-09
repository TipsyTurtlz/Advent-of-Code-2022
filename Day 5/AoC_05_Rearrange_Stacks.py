########### PART ONE #################
empty  = '\n'
stack_numbers, move_commands, solution = [], [], []
crate_content, stack = {}, {}
# with open('Day 5/test.txt') as file:
with open('Day 5/AoC_05_input_data.txt') as file:
    for line in file:
        if 'move' not in line and line != empty:    
            stacks = range(1,len(line),4)
            for crate in stacks:
                if line[crate].isdigit():
                    stack_numbers.append(int(line[crate]))  
                if line[crate].isupper():
                    crate_content.setdefault(crate, []).append(line[crate])
        # separate move commands
        if line != empty and 'move' in line:
            line = line.replace('\n','').replace('move','').replace('from','-').replace('to','-').replace(' ','')
            move_commands.append(line) # digits are strings in here!

# # check reading output
# print(crate_content)
# print(move_commands)

# rearrange crate dict
crate_content_sorted = sorted(crate_content)
crate_content = {key:crate_content[key] for key in crate_content_sorted}
# print(crate_content)

# change keys from line position to stack number                
for line_position,stack_number in zip(crate_content,stack_numbers):
    stack[stack_number] = crate_content[line_position]
    

# # check output
# print(stack)

for command in move_commands:    
    how_many = int(command.split('-')[0])
    starting_stack = int(command.split('-')[1])
    destination_stack = int(command.split('-')[2])
    
########### PART TWO #################
    crates_to_move = stack[starting_stack][0:how_many]
    for crates in range(len(crates_to_move)-1,-1,-1):
        stack[destination_stack].insert(0,crates_to_move[crates])
    del stack[starting_stack][:len(crates_to_move)]

# # check output
# print(stack)

# get the result crates
for crates in stack:
    solution.append(stack[crates][0])     

print(''.join([*solution]))
        
## TIL:
#  *: Repetetion Operator on List Items -> returns a list
# zip() function for Parallel Iteration
# join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator
# map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator. In combination with str casting method
#       it converts each element of a list to the string type and returns the resultant list of items



