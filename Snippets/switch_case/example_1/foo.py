def switch_case(operator, x, y):
    if operator == 'add':
        return x+y
    elif operator == 'sub':
        return x-y
    elif operator == 'mult':
        return x*y
    elif operator == 'div':
        return x/y

print(switch_case('add',5,3))
print(switch_case('sub',5,3))
print(switch_case('mult',5,3))
print(switch_case('div',5,3))