class Stack:
    def __init__(self, capacity):
        self.capacity = capacity #Chứa Max
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.isEmpty():
            print("danh sach trong! khong the bo")
        return self.stack.pop()

    def push(self, value):
        if self.isFull():
            print("danh sach day! khong the them")
        self.stack.append(value)

    def top(self):
        if self.isEmpty():
            print("danh sach trong! khong the bo")
        return self.stack[-1]

Stack1 = Stack(5)
Stack1.push(1)
Stack1.push(2)
Stack1.push(3)

print(Stack1.isFull())
print(Stack1.top())
print(Stack1.pop())
print(Stack1.top())
print(Stack1.pop())
print(Stack1.top())
print(Stack1.pop())
print(Stack1.isEmpty())