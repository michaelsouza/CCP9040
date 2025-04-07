a = 1

def func():
    global a
    b = 2
    a = a + 3
    return a + b

print(f"a = {a}")
print(f"func(a) = {func()}")
print(f"func(a) = {func()}")
print(f"func(a) = {func()}")