

def part_1(first, second, letter, password):
    if first <= password.count(letter) <= second:
        # print("true")
        return True
    return False

def part_2(first, second, letter, password):
    if list(password)[first-1] == letter and list(password)[second-1] == letter:
        return False
    elif list(password)[first-1] != letter and list(password)[second-1] != letter:
        return False
    return True

if __name__=="__main__":
    inputs = set([str(line.strip()) for line in open("./input.txt")])
    x = list(inputs)
    length = len(x)
    count1 = 1
    count2 = 0
    # print("count1 top ===> " + str(count1))
    for i in range(length):
        first = int(x[i].split()[0].split('-')[0])
        second = int(x[i].split()[0].split('-')[1])
        letter = x[i].split()[1].split('-')[0].split(':')[0]
        password = x[i].split()[2].split('-')[0]
        # print(type(password.count(letter)))
        if part_1(first, second, letter, password):
            count1 = count1 + 1
            print("count1 = " + str(count1))
        if part_2(first, second, letter, password):
            count2 = count2 + 1
            print("count2 = " + str(count2))