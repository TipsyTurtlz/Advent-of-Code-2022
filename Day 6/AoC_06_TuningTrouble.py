########### PART ONE #################
is_marker = True
with open('Day 6/AoC_06_input_data.txt') as file:
# with open('Day 6/test.txt') as file:
    for line in file:
        for char, position_char in zip(line,range(len(line)-1)):
            if position_char >= 3:
                mask = line[position_char-3:position_char+1]
                for letter,position_letter in zip(mask,range(len(mask))):
                    if mask.index(letter) != position_letter:
                        is_marker = False
                        break
                    is_marker = True # if all letters occure for the first time in the mask, than it is a marker!

                if is_marker:
                    print(f'Found on position: {position_char + 1}')
                    break

########### PART TWO #################
is_marker = True
with open('Day 6/AoC_06_input_data.txt') as file:
# with open('Day 6/test.txt') as file:
    for line in file:
        for char, position_char in zip(line,range(len(line)-1)):
            if position_char >= 13:
                mask = line[position_char-13:position_char+1]
                for letter,position_letter in zip(mask,range(len(mask))):
                    if mask.index(letter) != position_letter:
                        is_marker = False
                        break
                    is_marker = True # if all letters occure for the first time in the mask, than it is a marker!

                if is_marker:
                    print(f'Found on position: {position_char + 1}')
                    break                     

