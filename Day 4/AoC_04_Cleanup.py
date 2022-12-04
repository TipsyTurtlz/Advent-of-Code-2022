########### PART ONE #################
counter = 0

# import
input_data = open('Day 4/AoC_04_input_data.txt','r')
# input_data = open('Day 4/test.txt','r')
data = input_data.read()
data_list = data.splitlines()   

for string in data_list:
    string_index = data_list.index(string)
    data_list[string_index] = string.replace(',','-')
    data_list[string_index] = data_list[string_index].split('-')

# pair one inside pair two a>c && b<d
# pair two inside pair one a<c && b>d
for string in data_list:
    
    a = int(string[0])
    b = int(string[1])
    c = int(string[2])
    d = int(string[3])
    
    if a >= c and b <= d:
        counter += 1
        # print(f"{a}-{b} is in {c}-{d}")
    elif a <= c and b >= d:
        counter += 1
        # print(f"{c}-{d} is in {a}-{b}")
        
    ########### PART TWO #################    
    elif a <= c and c <= b and d >= b:
        counter += 1
        # print(f"{a}-{b} is in {c}-{d}")
    elif c <= a and a <= d and d <= b:
        counter += 1
        # print(f"{c}-{d} is in {a}-{b}")
   
    
print(counter)


