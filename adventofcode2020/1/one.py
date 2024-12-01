from itertools import combinations

with open("input.txt") as file:
    data = [l.rstrip("\n") for l in file]
    for pair in combinations(data, 2):
        if int(pair[0]) + int(pair[1]) == 2020:
            n0 = int(pair[0])
            n1 = int(pair[1])
            print("multiplication:")
            print(n0 * n1)
    for triple in combinations(data, 3):
        n0 = int(triple[0])
        n1 = int(triple[1])
        n2 = int(triple[2])
        if (n0+n1+n2) == 2020:
            print(n0*n1*n2)





