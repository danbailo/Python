array_one = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

array_two = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

total = [[0,0,0],[0,0,0],[0,0,0]]

total = array_one + array_two

# print(total)

for i in range(len(array_one)):
    for j in range(len(array_one[0])):
        total[i][j] = array_one[i][j] + array_two[i][j]

for num in total:
    print(num)
    pass
