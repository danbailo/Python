nums = [0, 1, 2, 3, 4, 5, 6]

#a cada remocao, a lista nums muda, por isso nao e removido
#0,1,2
#e sim
#0,2,4
for i in range(3):
    print(nums.pop(i))

print(nums)

nums.insert(1, nums.index(3))

print(nums)