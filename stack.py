"""
push
pop
is_empty
"""
def length(item):
    l = 0
    for _ in item:
        l += 1
    return l
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.remove(self.items[-1])
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def get_stack(self):
        return self.items
class list():
    def __init__(self):
        self.items = []
    def append(self, item):
        self.items[length(self.items) + 1] = item
        return self.items
    def remove(self, item):
        self.items[self.items.index(item)] = ''
        return self.items
    def index(self, item):
        return
s = Stack()
s.push("1")
s.push("2")
s.push("3")
s.push("4")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())