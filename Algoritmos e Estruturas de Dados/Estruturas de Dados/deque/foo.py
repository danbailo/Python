#deque - double-ended queue
#index = len - 1

class Deque(object):
    
    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False
    
    def push_front(self, value):
        self.deque.insert(0, value)
        self.len += 1

    def push_back(self, value):
        self.deque.insert(self.len, value)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1
    
    def pop_back(self):
        if not self.empty():
            self.deque.pop(-1) #it's same (len-1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def __str__(self):
        if not self.empty():
            return '{}'.format(self.deque)
        return 'Empty'

d = Deque()

d.push_front(3)
d.push_front(4)
d.push_front(5)
d.push_front(2)

d.push_back(0)
d.push_back(9)
d.push_back(8)
d.push_back(7)

# d.pop_front()
d.pop_back()

# print('front is %d'%d.front())
# print('back is %d'%d.back())

print(d)
print('len is %d'%d.len)

d.pop_back()
print(d)
print('len is %d'%d.len)

d.pop_front()
print(d)
print('len is %d'%d.len)

d.pop_back()
d.pop_back()
d.pop_back()
print(d)
print('len is %d'%d.len)

d.pop_front()
d.pop_front()
print(d)
print('len is %d'%d.len)

d.pop_front()
print(d)
print('len is %d'%d.len)