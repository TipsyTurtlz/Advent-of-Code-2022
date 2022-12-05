########### PART ONE #################
stack_commands, command_list, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = [], [], [], [], [], [],[],[],[],[],[]


with open('Day 5/AoC_05_input_data.txt') as file:
    for line in file:
        
        if line != '\n' and not 'move' in line:
            line = line.replace('\n', '')
            # more generalization!
            stack1.append(line[1])  
            stack2.append(line[5])  
            stack3.append(line[9])  
            stack4.append(line[13]) 
            stack5.append(line[17]) 
            stack6.append(line[21]) 
            stack7.append(line[25]) 
            stack8.append(line[29]) 
            stack9.append(line[33]) 

        elif 'move' in line:
            line = line.replace('move', '')
            line = line.replace('from', '')
            line = line.replace('to', '')
            line = line.replace('\n', '')
            line = line.replace(' ','')
            stack_commands.append(line)
print([stack1,stack2, stack3])

       

# for command in stack_commands:
#     how_many = int(command[0])
#     starting_stack = int(command[1])
#     destination_stack = int(command[2])
#     # print([how_many,starting_stack,destination_stack])

