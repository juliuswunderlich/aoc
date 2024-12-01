import re

def extraxtNewColorAndNum(line, old_color):
    num = 0
    new_color = ""
    r_old = "\d " + old_color
    print(line)
    print(old_color)
    if re.search(r_old, line) != None:
        new_color = line.split(' ')[0] + " " + line.split(' ')[1]
        num = int(re.findall("\d " + r_old)[0])
    assert num != 0
    assert new_color != ""
    return num, new_color

def loop_data(data, regex):
    new_lines = []
    if len(data) > 0:
        for line in data:
            if re.search(regex, line) != None:
                num, color = extraxtNewColorAndNum(line, regex)
                print(str(num) + " " + color )
                new_lines.append(line)
        





with open("input.txt") as f:
    data = [l.strip("\n") for l in f]
    regex = "\d shiny gold"
    loop_data(data, regex)
    