########### PART ONE #################
empty = '\n'
# contains the indicies of where the information in each stack is saved
position = []
stack_content = []
# line number where the stack numbers are located
stack_numbers_line = 3
stack_number_list = [1,2,3]

with open('Day 5/test.txt') as file:
    for line in enumerate(file):
        stack_content.append(line[1].replace())
        if line[0] == stack_numbers_line:
            for number in stack_number_list:
                position.append(line[1].index(str(number)))
print(stack_content)
           










       

