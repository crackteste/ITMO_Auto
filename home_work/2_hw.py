def task_1():
    a: int = 1
    b: float = 1.5
    c: str = 'pride'
    d: list = [1,2,3,4,5]
    e: bool = True

def task_2(a=[1,2,3,5,8,13,21]) ->list:
    return a[0:3]
print(task_2())

def task_3(a) ->int:
    return a*a
print(task_3(2))