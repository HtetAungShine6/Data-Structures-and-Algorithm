def is_operator(char):
    return char in '+-*/^'

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append('(' + operand1 + char + operand2 + ')')
    return stack.pop()

def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append('(' + operand1 + char + operand2 + ')')
    return stack.pop()

def prefix_to_postfix(expression):
    stack = []
    for char in reversed(expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand1 + operand2 + char)
    return stack.pop()

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
    return stack.pop()

# Example usage:
prefix_expression = "*+AB-CD"
postfix_expression = "359*+93+-"
print("Prefix to Postfix:", prefix_to_postfix(prefix_expression))
print("Postfix to Prefix:", postfix_to_prefix(postfix_expression))
print("Prefix to Infix:", prefix_to_infix(prefix_expression))
print("Postfix to Infix:", postfix_to_infix(postfix_expression))
