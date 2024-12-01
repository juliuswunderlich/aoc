from copy import copy

def runProgram(instructions, y):
    acc = 0
    i = 0
    while i < len(instructions):
        if instructions[i][2] == 1:
            return i, acc
        inst = instructions[i][0]
        if i == y:
            inst = "nop"
        val = instructions[i][1]
        instructions[i][2] += 1
        if inst == "nop":
            i += 1
        if inst == "acc":
            acc += val
            i += 1
        if inst == "jmp":
            i += val
    return "terminated: " + str(acc)



if __name__ == "__main__":
    list_of_nops = [1, 412 ,590 ,191 ,491 ,181, 517, 48, 548 ,258, 40, 578, 196, 403, 280, 281, 282, 487, 59, 235, 236]
    list_of_jmps = [4, 481, 274, 413, 144, 417, 591, 178, 33, 164, 529, 193, 462, 132, 499, 381, 345, 106, 493, 455, 93, 264, 183, 516, 518, 154, 394, 522, 290, 241, 49, 270, 441, 563, 469, 566, 541, 312, 316, 549, 552, 251, 137, 259, 400, 27, 161, 510, 427, 42, 167, 169, 579, 198, 158, 228, 405, 173, 283, 488, 58, 62, 201, 113, 212, 213, 357, 386, 150, 237, 97, 368]
    """
    for y in list_of_nops:
        with open("input.txt", 'r') as file:
            data = [l.strip("\n") for l in file]
            instructions = []
            for line in data:
                inst = line.split(' ')[0]
                val = int(line.split(' ')[1])
                counter = 0
                instructions.append( [inst, val, counter] )
            print(runProgram(instructions,y ))
            """
    for y in list_of_jmps:
        with open("input.txt", 'r') as file:
            data = [l.strip("\n") for l in file]
            instructions = []
            for line in data:
                inst = line.split(' ')[0]
                val = int(line.split(' ')[1])
                counter = 0
                instructions.append( [inst, val, counter] )
            print(runProgram(instructions, y))






