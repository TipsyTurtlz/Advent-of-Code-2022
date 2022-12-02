########### PART ONE #################
import numpy as np
# A = Rock, B = Paper, C = Scicssors
# X = Rock (1p), Y = Paper (2p), Z = Scissors (3p)
# Win = 6p, Lose = 0p (win%win), Draw = 3p (win/2)

win_points, lose_points, draw_points = 6,0,3
rock, paper, scissors = 1,2,3
data_dict = {}
rock_list, paper_list, scissors_list = [], [],[]

with open("C:/Users/busch/OneDrive/Desktop/Advent of Code/02/AoC_02_input_data.txt") as file:
    for line in file:
       (key, val) = line.split()
       if key == 'A':
        rock_list.append(val)
        data_dict[key] = rock_list
       elif key == 'B':
        paper_list.append(val)
        data_dict[key] = paper_list
       elif key == 'C':
        scissors_list.append(val)
        data_dict[key] = scissors_list

# how many rocks (x), papers (y) and scissors (z) related to a rock, paper or scissors (key)
rock_counts = [data_dict['A'].count('X'), data_dict['A'].count('Y'), data_dict['A'].count('Z')]
paper_counts = [data_dict['B'].count('X'), data_dict['B'].count('Y'), data_dict['B'].count('Z')]
scissors_counts = [data_dict['C'].count('X'), data_dict['C'].count('Y'), data_dict['C'].count('Z')]


rock_points = [rock_counts[0]*(rock + draw_points), rock_counts[1]*(paper + win_points), rock_counts[2]*(scissors+lose_points)]
paper_points = [paper_counts[0]*(rock + lose_points), paper_counts[1]*(paper+draw_points), paper_counts[2]*(scissors+win_points)]
scissors_points = [scissors_counts[0]*(rock + win_points), scissors_counts[1]*(paper + lose_points), scissors_counts[2]*(scissors + draw_points)]

sum = np.sum(rock_points) + np.sum(paper_points) + np.sum(scissors_points)
print(sum)
# 14827 is right 

########### PART TWO ################
# X = lose, Y = draw, Z = win

rock_points = [rock_counts[0]*(scissors + lose_points), rock_counts[1]*(rock + draw_points), rock_counts[2]*(paper+win_points)] 
paper_points = [paper_counts[0]*(rock + lose_points), paper_counts[1]*(paper+draw_points), paper_counts[2]*(scissors+win_points)]
scissors_points = [scissors_counts[0]*(paper + lose_points), scissors_counts[1]*(scissors + draw_points), scissors_counts[2]*(rock + win_points)]
sum2 = np.sum(rock_points) + np.sum(paper_points) + np.sum(scissors_points)
print(sum2)
# 13889 is right