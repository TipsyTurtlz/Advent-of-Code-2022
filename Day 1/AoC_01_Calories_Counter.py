import numpy as np
########### PART ONE #################
# open dataset
input_data = open('C:/Users/busch/OneDrive/Desktop/Advent of Code/01/AoC_01_input_data.txt','r')
# extract data from dataset
data = input_data.read()
# generate list containing strings
data_list = data.splitlines()
calories_list, calories= [],0
# generate list with sum of calories for each elf
for i in data_list:
    calories += int(i)  
    if i == '':
        calories_list.append(calories)
        calories = 0

max_calories = max(calories_list)   
    
# print(calories_list)
# print(data_list.count('') == len(calories_list))
# print(max_calories)

########### PART TWO #################
calories_sorted = np.sort(calories_list)
# print(calories_sorted)
sum_top_3 = np.sum(calories_sorted[-3:])
print(sum_top_3)