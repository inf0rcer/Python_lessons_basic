# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibb1 = fibb2 = 1
    fibb_par = []
    fibb_par.append(fibb1)
    for fibb in range(2, m):
        fibb1, fibb2 = fibb2, fibb1 + fibb2
        if fibb >= n:
            fibb_par.append(fibb1)
    fibb_par.append(fibb2)
    print(fibb_par)
    pass
fibonacci(1, 10)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    rep = 1
    while rep < len(origin_list):
        for i in range(len(origin_list)-rep):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
        rep = rep + 1
    print(origin_list)

    return origin_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def func(x):
    return res_func
def filter_clone(res_func, par2):
    result_list = []
    for i in range(len(par2)):
        if func(x) == true:
            result_list.append(res_func)
    return result_list



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check_parall(x1, y1, x2, y2, x3, y3, x4, y4):
    side1 = y2 - y1
    side2 = x3 - x2
    side3 = y3 - y4
    side4 = x4 - x1
    if side1 == side3 and side2 == side4:
        print('Oh, its a parallelogram')
    else:
        print('Thats not a parallelogram')
    pass

check_parall(1, 1, 1, 4, 4, 4, 4, 1)
