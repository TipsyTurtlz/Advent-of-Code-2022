########### PART ONE #################
import numpy as np
empty = '\n'
# contains the indicies of where the information in each stack is saved
stack_content = []
# line number where the stack numbers are located
stack_numbers = []
move_commands = []
indices = []

stacks =[]

with open('Day 5/AoC_05_input_data.txt') as file:
    for line in file:
        # separate stack content from input
        if line != empty and '1' not in line and 'move' not in line:
            line = line.replace('\n','')
            stack_content.append(line)
        # separate stack numbers
        if line != empty and 'move' not in line and '1' in line:
            line = line.replace('\n','')
            stack_numbers.append(line)
        # separate move commands
        if line != empty and 'move' in line:
            line = line.replace('\n','').replace('move','').replace('from','').replace('to','').replace(' ','')
            move_commands.append(line)


rows, columns, height = 72, 9, 8
stack_array = np.zeros((rows,columns),dtype=str)
# print(stack_array)
print(stack_content)
i=0
for line in stack_content:
    j=0
    for char in line:
        # if line.index(char)%4 ==1 and char != ' ':
        #     stack_array[5+i][(j-1)/4] = char
        # print(char)
        if j%4 == 1 and char != ' ':
            # print(char)
            a=int(rows-height+i)
            b=int((j-1)/4)
            # print (a, b)
            stack_array[a][b] = char
        j+=1
    i+=1



print(stack_array) # ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]']
# [['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' '' '' '' '' '' '' '']
#  ['' '' 'F' 'Q' '' '' 'Q' '' '']
#  ['B' '' 'Q' 'V' 'D' '' 'S' '' '']
#  ['S' 'P' 'T' 'R' 'M' '' 'D' '' '']
#  ['J' 'V' 'W' 'M' 'F' '' 'J' '' 'J']
#  ['Z' 'G' 'S' 'W' 'N' 'D' 'R' '' 'T']
#  ['V' 'M' 'B' 'G' 'S' 'C' 'T' 'V' 'S']
#  ['D' 'S' 'L' 'J' 'L' 'G' 'G' 'F' 'R']
#  ['G' 'Z' 'C' 'H' 'C' 'R' 'H' 'P' 'D']]


#Pickup-Funktion
def move(num, column, target)

#for schleife num mal ausführen 
#oberstes Element in Spalte column finden

#oberstes Element zwischenspeichern in temp und löschen

#oberstes element in target finden
#temp oberhalb einfügen



# def function(args):
#     pass

#Place-Funktion