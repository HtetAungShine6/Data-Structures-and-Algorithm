def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def pop(lt):
    value = lt[-1]
    del lt[-1]
    return float(value)

stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        stack.append(token)
    else:
        first = pop(stack)
        second = pop(stack)
        switcher ={'+':second + first, '-':second-first, '*':second * first,'/':second / first, '^':second**first, "%": second % first}
        stack.append(switcher.get(token))

print('%.1f' % stack[0])