class Queue(object):
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self,value):
        self.queue.append(value)
        self.len_queue += 1
    
    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def __str__(self):
        if not self.empty():
            return '{}'.format(self.queue)
        return 'Empty'

q = Queue()

print(q)

q.push(5)
q.push(3)
q.push(2)
q.push(1)

print(q)

q.pop()
print(q)

q.pop()
print(q)