import random
import math
import timeit
import matplotlib.pyplot as plt
TESTING_MODE = True


## Данное задание было мною переделано в task3.py из-за невозможность точного анализа асимптотики алгоритмов

def alg_3n(n):
    # создание массива, вывод его, вывод максимального значения  - неоптимальный метод
    mas = []
    count=0 # для проведения тестирования, вместо вывода будет использоваться операция увеличения счётчика
    # --n
    for i in range(n):
        mas.append(random.randint(0, 100))
    # --n
    for i in range(n):
        if not TESTING_MODE:
            print(mas[i], end=" ")
        else:
            count+=1
    if not TESTING_MODE:
        print()
    # --n
    maxx = mas[0]
    for i in range(1, n):
        if maxx < mas[i]:
            maxx = mas[i]

    if not TESTING_MODE:
        print(maxx)
    else:
        count += 1


def alg_nlogn(n,x):
    # Создание упорядоченного массива и вывод наличия в нём числа x
    mas = []
    # --n
    for i in range(n):
        mas.append(i)

    left=0
    right=0
    step=0
    while step<= math.log2(n):
        median = (left+right)//2
        if mas[median]==x:
            return True
        if mas[median]>x:
            right=median
        if mas[median]<x:
            left = median
        step+=1
    if TESTING_MODE:
        return False
    else:
        print("нету туть такого числа ^_^")


def alg_nfact(n):
    # Вычисление факториала сааааамым медленным способом
    count =1
    temp=0
    gc=1
    while gc<=n:
        temp=count
        for i in range(gc-1):
            for j in range(temp):
                count+=1
        gc+=1

    if TESTING_MODE:
        return count
    else:
        print(count)


def alg_ncube(n):
    a=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a+=1
    return a


def alg_3logn(n,x,y):
    mas = []
    # --n ---------------- условность, что у нас уже есть отсортированный массив
    for i in range(n):
        mas.append(i)

    first,second=False,False

    left = 0
    right = 0
    step = 0
    while step <= math.log2(n):
        median = (left + right) // 2
        if mas[median] == x:
            first=True
        if mas[median] > x:
            right = median
        if mas[median] < x:
            left = median
        step += 1

    left = 0
    right = 0
    step = 0
    while step <= math.log2(n):
        median = (left + right) // 2
        if mas[median] == y:
            second = True
        if mas[median] > y:
            right = median
        if mas[median] < y:
            left = median
        step += 1

    if TESTING_MODE:
        return first,second
    else:
        print(first,second)

if __name__ == '__main__':
    #Проверяем время выполнения программ
    iteration = 100
    mas_times=[]
    for i in range(1,iteration):
        print(int(i/iteration*100),"%")
        mas_times.append(timeit.timeit(f"alg_3n({i})", globals=globals()))
    #print(mas_times)
    plt.plot(list(range(1, iteration)), mas_times)
    plt.show()

