coins = [1, 3, 7, 9, 11]
def change(v):
    if v == 0: return 0
    if v in coins: return 1
    if v < 0: return float('inf')
    x = min([change(v-i) for i in coins])+1
    if x: return 1

r = [False for i in range(10000)]
def change_dinamic(v):
    if v == 0: return 0
    if v in coins: return 1
    if v < 0: return float('inf')
    if r[v] != False: return r[v]
    r[v] = min([change_dinamic(v-i) for i in coins])+1
    return r[v]

moedas={1, 3, 7, 9, 11}
mem=dict(zip(list(moedas),[1]*len(moedas)))

def troco(v):
    if v == 0: return 0
    if v<0:return float("inf")
    ans=mem.get(v,None)
    if ans:return ans
    ans=min([troco(v-m)for m in moedas])+1
    mem[v]=ans
    return ans

while True:
    try:
        v = int(input('input any number: '))
        print(change(v))
    except EOFError:
        print(flush=True)
        exit(-1)
    # print(change_dinamic(v))