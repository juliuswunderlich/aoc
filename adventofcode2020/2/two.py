
def checkWord(nums, letter, chars):
    one = 1 if chars[nums[0]- 1] == letter else 0
    two = 1 if chars[nums[1] - 1] == letter else 0

    if one + two == 1:
        return True
    return False


with open("input.txt") as file:
    data = [l.strip("\n") for l in file]
    counter = 0
    for l in data:
        elements = l.split(" ")
        nums = elements[0].split("-")
        nums[0] = int(nums[0])
        nums[1] = int(nums[1])
        letter = elements[1].strip(":")
        chars = list(elements[2]) #string to chars
        if checkWord(nums, letter, chars):
            counter += 1
    print(counter)




        

