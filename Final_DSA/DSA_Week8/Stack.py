class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after pop:", stack.items)
