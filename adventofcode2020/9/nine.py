from itertools import combinations
from more_itertools import chunked

def checkNum(number, data):
    for i in range(len(data)):
        if i >= 25:
            pairs = combinations(data[i-25:i], 2)
            sum_pairs = [i[0] + i[1] for i in pairs]
            print(sorted(sum_pairs))
            if data[i] not in sum_pairs:
                print(data[i])
                return None
    return True
    

def checkNum2(number, data):
    tuples = []
    num = 466456641
    left_pointer = 0
    right_pointer = 1
    cum_total = data[left_pointer] + data[right_pointer]

    while right_pointer < len(data):
        if cum_total > num:
            cum_total -= data[left_pointer]
            left_pointer += 1

        elif cum_total < num:
            right_pointer += 1
            cum_total += data[right_pointer]
        else:
            return data[left_pointer:right_pointer + 1]

    return -1


if __name__ == "__main__":
    test_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    with open("input.txt") as f:
        data = [int(l.strip("\n")) for l in f]
        #checkNum(0, data)
        #checkNum2(0, data[:612])
        l = checkNum2(0, data)
        print(l[0] + l[-1])
                


