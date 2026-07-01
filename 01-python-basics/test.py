for i in range(2):
    for j in range(2):
        print(i, j)


def info(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    print(kwargs)

info(name="小明", age=18)   # {'name': '小明', 'age': 18}

def sum_all(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

sum_all(1, 2, 3)   # args = (1, 2, 3) → 6
sum_all()          # args = () → 0
sum_all(1, 2, 3, 4, 5)  # args = (1, 2, 3, 4, 5) → 15

print("----")
def sum_all2(*args):
    print(type(args))
    return sum(args)

sum_all2(1,2)
print(sum_all2())

def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n

print(f(4))
