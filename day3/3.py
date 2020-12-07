
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
#   part 1 answer = 284
#   part 2 answer = 

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

def get_number_of_trees(index, buffer):
    open_space = 0
    tree_space = 0
    array_index = index
    y = index
    x = buffer
    for i in range(input_length):
        print(input[i + x])
        temp_arr = list(input[i + x])
        length_temp_arr = len(temp_arr)
        print(temp_arr)
        if i <= (0 + x):
            print("i ======>>>> do nothing => " + str(i + x))
        elif i == (1 + x):
            array_index = index
            print("i ======>>>> do stuff 1 => " + str(i + x))
            if traverse_slope(temp_arr, array_index):
                open_space = open_space + 1
                print("open_space = " + str(open_space))
            else:
                tree_space = tree_space + 1
                print("tree_space = " + str(tree_space))
            array_index = array_index + index
        else:
            print("i ======>>>> do stuff 2 => " + str(i + x))
            print(input[i + x])
            print(temp_arr)
            if traverse_slope(temp_arr, array_index):
                open_space = open_space + 1
                print("open_space = " + str(open_space))
            else:
                tree_space = tree_space + 1
                print("tree_space = " + str(tree_space))
            array_index = array_index + index
            if array_index == length_temp_arr:
                print("array index ==>>> " + str(array_index))
                array_index = 0
            elif array_index == length_temp_arr + 1:
                array_index = 1
            elif array_index == length_temp_arr + 2:
                array_index = 2
            elif array_index == length_temp_arr + 3:
                array_index = 3
            elif array_index == length_temp_arr + 4:
                array_index = 4
            elif array_index == length_temp_arr + 5:
                array_index = 5
            elif array_index == length_temp_arr + 6:
                array_index = 6
            elif array_index == length_temp_arr + 7:
                array_index = 7
            print("array_index ====>>>> " + str(array_index))

def get_number_of_trees2(index, buffer):
    open_space = 0
    tree_space = 0
    array_index = index
    y = index
    x = buffer
    for i in range(1, input_length + 1, 2):
        print(input[i + x])
        temp_arr = list(input[i + x])
        length_temp_arr = len(temp_arr)
        print(temp_arr)
        print("i ======>>>> do stuff 2 => " + str(i))
        print(input[i])
        print(temp_arr)
        if traverse_slope(temp_arr, array_index):
            open_space = open_space + 1
            print("open_space = " + str(open_space))
        else:
            tree_space = tree_space + 1
            print("tree_space = " + str(tree_space))
        array_index = array_index + index
        if array_index == length_temp_arr:
            print("array index ==>>> " + str(array_index))
            array_index = 0
        elif array_index == length_temp_arr + 1:
            array_index = 1
        print("array_index ====>>>> " + str(array_index))

REFECTORING BOTH METHODS INTO ONE - INCOMPELETE
def get_number_of_trees3(start_position, increment, step):
    open_space = 0
    tree_space = 0
    array_index = increment
    for i in range(start_position, input_length, step):
        print(input[i + increment])
        temp_arr = list(input[i + increment])
        length_temp_arr = len(temp_arr)
        if traverse_slope(temp_arr, array_index):
            open_space = open_space + 1
            print("open_space = " + str(open_space))
        else:
            tree_space = tree_space + 1
            print("tree_space = " + str(tree_space))
        array_index = array_index + increment
        if array_index == length_temp_arr:
            print("array index ==>>> " + str(array_index))
            array_index = 0
        elif array_index == length_temp_arr + 1:
            array_index = 1
        print("array_index ====>>>> " + str(array_index))
    
if __name__=="__main__":
    input = [line.strip() for line in open("./input.txt", 'r')]
    length = len(input)
    input_length = len(input)
    # 64
    slope1 = get_number_of_trees(1,0)
    # 284
    slope2 = get_number_of_trees(3,0)
    # 71
    slope3 = get_number_of_trees(5,0)
    # 68
    slope4 = get_number_of_trees(7,0)
    # 40
    slope5 = get_number_of_trees2(1,1)

    # refactoring
    # slope6 = get_number_of_trees3(1,1,1)

    tree_val = slope1 * slope2 * slope3 * slope4 * slope5
    print("TREE VAL TOTAL ====>>>>> " + str(tree_val))