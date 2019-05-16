r={}
price = [
    [20,15,30,45],
    [100,150,200],
    [20,25,30,40]]
def shop(index,money):
    if money<0:return float('-inf')
    if index==len(price):return 0
    ans=r.get((index,money),None)
    if ans!=None:return ans
    greater=float('-inf')
    for i in range(len(price[index])):
        greater = max(greater, price[index][i] + shop(index + 1, money - price[index][i]))
    r[(index,money)] = greater;      
    return greater;

# genVec=lambda n:[-1 for _ in range(n)]
# r=[genVec(300) for _ in range(200)]
# def shop(id,money):
#     if money<0:return -float("inf")
#     if id==3:return 0
#     if r[id][money]!=-1:return r[id][money]
#     maior=-float("inf")
#     for i in range(len(price[id])):
#         maior = max(maior, price[id][i] + shop(id + 1, money - price[id][i]))
#     r[id][money] = maior;
#     return maior;
# price=[
# [20,15,30,45],
# [100,150,200],
# [20,25,30,40]
# ]
# print(shop(0,190))

if __name__ == "__main__":
    
    print(shop(0,150))
    print(shop(0,160))
    print(shop(0,200))
    print(shop(0,340))
