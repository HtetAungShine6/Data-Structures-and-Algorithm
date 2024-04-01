class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.push(result)

    return stack.pop()

def evaluate_prefix(expression):
    stack = Stack()
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in reversed(expression):
        if token.isdigit():
            stack.push(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.push(result)

    return stack.pop()

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []

    for token in expression:
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    prefix = []

    for token in reversed(expression):
        if token.isdigit():
            prefix.append(token)
        elif token == ')':
            stack.push(token)
        elif token == '(':
            while not stack.is_empty() and stack.peek() != ')':
                prefix.append(stack.pop())
            stack.pop()  # Remove ')'
        else:
            while not stack.is_empty() and precedence.get(stack.peek(), 0) > precedence[token]:
                prefix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        prefix.append(stack.pop())

    return ''.join(reversed(prefix))

# Example usage:
# infix_expression = "(3+4)*2"
infix_expression = "((36*3)-(36/(9-5)))"
postfix_expression = infix_to_postfix(infix_expression)
prefix_expression = infix_to_prefix(infix_expression)

postfix_result = evaluate_postfix(postfix_expression)
prefix_result = evaluate_prefix(prefix_expression)

print("Infix expression:", infix_expression)
print("Postfix expression:", postfix_expression, " Result:", postfix_result)
print("Prefix expression:", prefix_expression, " Result:", prefix_result)
