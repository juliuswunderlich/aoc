import re

from builtins import any
cleaned_data = []

def checkFields(line):
    check_words = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    m_dict = {}
    for word in line:
        words = word.split(":")
        m_dict[words[0]] = words[1]

    byr = int(m_dict['byr'])
    iyr = int(m_dict['iyr'])
    eyr = int(m_dict['eyr'])
    hgt_str = m_dict['hgt']
    hgt_num = int(m_dict['hgt'].strip("cm").strip("in"))
    hcl = m_dict['hcl']
    ecl = m_dict['ecl']
    pid = m_dict['pid']

    if byr > 2002 or byr < 1920:
        return False
    if iyr > 2020 or iyr < 2010:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    if ('cm' not in hgt_str) and ('in' not in hgt_str):
        return False
    if ('cm' in hgt_str):
       if hgt_num > 193 or hgt_num < 150:
           return False
    if ('in' in hgt_str):
        if hgt_num < 59 or hgt_num > 76:
            return False
    if re.search("^#[0-9a-f]{6}$", hcl) == None:
        return False
    if ecl not in check_words:
        return False
    if re.search("^[0-9]{9}$", pid) == None:
        return False

    return True

with open("input.txt") as f:
    data = [l.strip('\n ') for l in f]
    i = 0
    for e in range(len(data)):
        if data[e] != '':
            i += 1
        else:
            myTuple = []
            for j in range(e-i, e):
                myTuple.append(data[j])
            i = 0
            cleaned_data.append(" ".join(myTuple))
    
    # append last line
    cleaned_data.append("byr:2001 hcl:#4784a2 hgt:161cm iyr:2014 eyr:2025 pid:955262336 ecl:amb")

    [print(l + " -END-") for l in cleaned_data]
    counter = 0
    for i in range(len(cleaned_data)):
        cleaned_data[i] = cleaned_data[i].split(' ')
        if (len(cleaned_data[i]) == 8):
            if (checkFields(cleaned_data[i])):
                counter += 1
        elif(len(cleaned_data[i]) == 7):
            test = "".join(cleaned_data[i])
            if 'cid:' not in test:
                if (checkFields(cleaned_data[i])):
                    counter += 1
                #print(test + ", " + str(counter))
    print(counter)



        
