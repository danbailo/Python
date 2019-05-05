def switch_case(operator, x, y):
    return {
        'add' : lambda: x+y,
        'sub' : lambda: x-y,
        'mult' : lambda: x*y,
        'div' : lambda: x/y
    }.get(operator, lambda: None)()

print(switch_case('add',5,3))
print(switch_case('sub',5,3))
print(switch_case('mult',5,3))
print(switch_case('div',5,3))