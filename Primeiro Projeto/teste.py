#primeiro ele atribui o valor para o index e depois para o item, o item recebe o primeiro
#parametro do enumerate e o index o segundo;
for index, item in enumerate("abcdefghi", start=1):
    # print('index:',index)
    # print('item:',item)
    print(item, end=' ' if index % 3 else '\n') #hr q chega na 4 linha ele quebra, por ex;