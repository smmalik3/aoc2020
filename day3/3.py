
# psuedo code
#     split into each line into an array of 1 character strings
#     move three to the right on the first line then go to next line and move to third spot
#     identify if it's a tree or open space and record it
#     if tree:
#         return tree
#     else:
#         return open_space
#     add 3 to move to the right on the next line
#     repeat

array_index = 4
open_space = 0
tree_space = 0

def traverse_slope(array, array_index):
    if array[array_index] == '.':
        print("TRUE ====>>>> " + array[array_index])
        return True
    else:
        print("FALSE ====>>>> " + array[array_index])
        return False
    
if __name__=="__main__":
    input = [line.strip() for line in open("./input.txt", 'r')]
    length = len(input)
    input_length = len(input)
    for i in range(input_length):
        print(input[i])
        temp_arr = list(input[i])
        length_temp_arr = len(temp_arr)
        print(temp_arr)
        if i == 0:
            print("i ======>>>> do nothing => " + str(i))
        elif i == 1:
            array_index = 3
            print("i ======>>>> do stuff 1 => " + str(i))
            if traverse_slope(temp_arr, array_index):
                open_space = open_space + 1
                print("open_space = " + str(open_space))
            else:
                tree_space = tree_space + 1
                print("tree_space = " + str(tree_space))
            array_index = array_index + 3
            if array_index == length_temp_arr:
                print("array index ==>>> " + str(array_index))
                array_index = 0
            elif array_index == length_temp_arr + 1:
                array_index = 1
            elif array_index == length_temp_arr + 2:
                array_index = 2
            print("array_index ====>>>> " + str(array_index))
        else:
            print("i ======>>>> do stuff 2 => " + str(i))
            print(input[i])
            print(temp_arr)
            if traverse_slope(temp_arr, array_index):
                open_space = open_space + 1
                print("open_space = " + str(open_space))
            else:
                tree_space = tree_space + 1
                print("tree_space = " + str(tree_space))
            array_index = array_index + 3
            if array_index == length_temp_arr:
                print("array index ==>>> " + str(array_index))
                array_index = 0
            elif array_index == length_temp_arr + 1:
                array_index = 1
            elif array_index == length_temp_arr + 2:
                array_index = 2
            print("array_index ====>>>> " + str(array_index))