import math

def calcSeat(word):
    row_nums = [num for num in range(128)]
    col_nums = [num for num in range(8)]
    for instr in word:
        if (instr == 'F'):
            l = len(row_nums)
            row_nums = row_nums[:int(l/2)]
        elif (instr == 'B'):
            l = len(row_nums)
            row_nums = row_nums[int(l/2):]
        elif (instr == 'L'):
            l = len(col_nums)
            col_nums = col_nums[:int(l/2)]
        elif (instr == 'R'):
            l = len(col_nums)
            col_nums = col_nums[int(l/2):]

    assert len(row_nums) == 1
    assert len(col_nums) == 1
    return row_nums[0] * 8 + col_nums[0]


with open("input.txt") as f:
    data = [l.strip("\n") for l in f]
    res_list = [calcSeat(l) for l in data]
    test = "FBFBBFFRLR"
    #calcSeat(test)
    #print(max(res_list))
    s_rest_list = sorted(res_list)
    missing = []
    for i in range(85, 890):
        if i not in s_rest_list:
            missing.append(i)
    print(missing)


    
