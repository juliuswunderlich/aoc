

def num_answers(group):
    letters = []
    d = {}
    i = 0
    answers = group.split(' ')
    for a in answers:
        for c in a:
            letters.append(c)
    letters = list(set(letters))

    for l in letters:
        d[l] = 0
    for l in letters:
        for a in answers:
            if l in a:
                d[l] += 1
    for key in d.keys():
        if d[key] >= len(answers):
            i += 1

    #print(d.items())
    print(answers)
    print(i)
    return i






with open("input.txt") as f:
    data = [l.strip('\n ') for l in f]
    i = 0
    cleaned_data = []
    for e in range(len(data)):
        if data[e] != '':
            i += 1
        else:
            myTuple = []
            for j in range(e-i, e):
                myTuple.append(data[j])
            i = 0
            cleaned_data.append(" ".join(myTuple))

    cleaned_data.append("tal tal a al daevb")
    nums = [num_answers(l) for l in cleaned_data]
    print(sum(nums))




