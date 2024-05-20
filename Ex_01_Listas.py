def sum_elements_sublists(list):
    sum = 0
    for number in list:
        sum += number
    return sum

list = [[1, 2], [3], [4, 5, 6]]
sum = 0

for sublist in list:
    sum += sum_elements_sublists(sublist)

print(sum)