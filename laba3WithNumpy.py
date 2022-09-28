import numpy as np
import timeit


def Transponse(a):
    return np.transpose(a)
def Multiply(a,b):
    return np.dot(a,b)
def Rang(a):
    return np.linalg.matrix_rank(a)
def Reverse(a):
    return np.linalg.inv(a)
def matrix_input():
    print("Введите матрицу по одной строке (если вы хотите закончить ввод - нажмите Enter ):")

    size_x = -1
    matrix = []
    while (True):
        inp = input("")
        if inp == "":
            print("----")
            break
        inp = inp.split()
        if size_x == -1:
            size_x = len(inp)
        else:
            if len(inp) != size_x:
                print(
                    "Некорректный ввод - количество столбцов не соответствует предыдущим показаниям!\n Введите эту строку еще раз!")
                continue
        matrix.append(list(map(int, inp)))
    matrix=np.array(matrix)
    # print(matrix)
    return matrix
def Welcome_func():
    action = -1
    while (True):
        inp = input(
            "Введите желаемое действие:\n1 - Транспонирование матрицы  2- Умножение матриц  3- Определение ранга матрицы  4-Обратная матрица\n")
        if (inp == "1" or inp == "2" or inp == "3" or inp == "4"):
            action = int(inp)
            break
    return action

a=np.array([[5,4],[1,1]])
#print(timeit.timeit('Reverse(np.array(a))', globals=globals(),number=1000000))                                          # РАСКОММЕНТИРОВАТЬ ДЛЯ ПОЛУЧЕНИЯ РЕЗУЛЬТАТА БЫСТРОДЕЙСТВИЯ ПРОГРАММЫ
#breakpoint()

while True:
    action = Welcome_func()
    if action == 1:
        print(f"Результат транспонирования матрицы:\n {Transponse(matrix_input())}")

    if action == 2:
        print(f"Результат умножения матриц:\n {Multiply(matrix_input(),matrix_input())}")

    if action == 3:
        print(f"\nРанг матрицы:\n{Rang(matrix_input())}")

    if action == 4:
        print(f"\nОбратная матрица:\n{Reverse(matrix_input())}")

    print()