f = open("input.txt", 'r')
numbers = [int(line) for line in f]
counter = 0
"""
for i in range(1, len(numbers)):
    if (numbers[i] - numbers[i-1]) > 0:
        counter += 1
print(counter)
"""
# part two
j = 2
sum1 = 0
while j < len(numbers):
    sum2 = (numbers[j] + numbers[j-1] + numbers[j-2])
    if (sum2 > sum1): counter += 1
    sum1 = sum2
    j += 1
print(counter - 1) # -1 because the first comparision is counted although it should not be




    


