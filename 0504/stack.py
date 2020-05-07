

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.length() == 0:
            return None
        return self.items.pop()

    def length(self):
        return len(self.items)

class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.length() == 0:
            return None
        return self.items.pop(0)

    def length(self):
        return len(self.items)

stack = queue()
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)
stack.dequeue()
print(stack.items)
stack.dequeue()
stack.dequeue()
print(stack.items)
stack.dequeue()
print(stack.items)