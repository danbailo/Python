# lista = [0,1,2,3,4,5]
# print(len(lista))
# print(lista[6-1]) 
# mostrando ultimo elemento da lista

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, e):
        self.stack.append(e)
    
    def pop(self):
        if not self.empty(): #se a pilha nao estiver vazia remove, pois empty retorna true se estiver vazio, logo, se estiver vazio ele nao entra ai!
            self.stack.pop(len(self.stack)-1)
        else:
            print('Stack has empty!')
             
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None
    def empty(self):
        if (len(self.stack) == 0):
            return True
        return False

    def lenght(self):
        if not self.empty():
            return len(self.stack)
        else:
            return 0

    def __str__(self):
        return '{}'.format(self.stack)

stack = Stack()
stack.pop()
stack.push(5)
stack.push(3)
stack.push(6)
print(stack)
print('len is %d'%stack.lenght())

print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())
print('len is %d'%stack.lenght())
