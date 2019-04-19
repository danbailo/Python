list1 = [x**2 for x in range(5)]

list2 = [x**2 for x in [3,5,9]]

list3 = [x**2 for x in range(5) if x > 2]

print(list1)
print(list2)
print(list3)

#[0, 1, 4, 9, 16]
#[9, 25, 81]
#[9, 16]