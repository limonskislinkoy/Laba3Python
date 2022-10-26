import  random
import os
import matplotlib.pyplot as plt
import numpy as np
def Create_random_mas(n):
    m=[]
    for i in range(n):
        m.append(n-i)
    return m

def BubleSort(mas):
    for i in range(len(mas)-1):
        for j in range(len(mas)-i-1):
            if mas[j+1] < mas[j]:
                mas[j],mas[j+1]=mas[j+1],mas[j]
    return mas

def Medium_of_mas(mas):
    return sum(mas)/len(mas)

user_input=False
if user_input:
    print("Введите массив:\n")
    mas_not_sorted = list(map(int, input().split()))
    mas_sorted = BubleSort(mas_not_sorted)
    print(*mas_sorted)


iteration =40
if not user_input:
    gc=0
    ggc=0
    mas_of_times_of_iter = []
    while ggc<iteration:
        print(ggc)
        gc+=100
        ggc+=1

        mas_not_sorted= Create_random_mas(gc)
        a = os.times().user
        BubleSort(mas_not_sorted)
        mas_of_times_of_iter.append(os.times().user-a)
        #print(Medium_of_mas(mas_of_times_of_iter))

    plt.plot(list(range(0,iteration)),mas_of_times_of_iter)
    plt.show()