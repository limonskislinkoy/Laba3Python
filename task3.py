import random
import math
import timeit
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
TESTING_MODE = True

def alg_logn(n):
    count=0
    for i in range(round(math.log2(n))):
        count+=1
    return  count

def alg_const(n=1):
    return 1

def alg_n2(n):
    count =0
    for i in range(n):
        for j in range(n):
            count+=1
    return count

def alg_n3(n):
    count =0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count+=1
    return count

def alg_2pown(n):
    count=0
    for i in range(2**n):
        count+=1
    return  count

def alg_nfact(n):
    count =0
    for i in range(math.factorial(n)):
        count+=1
    return count

def alg_3n(n):
    count = 0
    for i in range(3*n):
        count+=1
    return count

def alg_3logn(n):
    count = 0
    for i in range(round(3*math.log2(n))):
        count += 1
    return count

def alg_nlogn(n):
    count = 0
    for i in range(round(n*math.log2(n))):
        count += 1
    return count



if __name__ == '__main__':
    #Проверяем время выполнения программ
    iteration = 9
    mas_times=[]
    for i in range(0+1,iteration+1):
        #os.system("cls")
        print(int(i/iteration*100),"%")
        mas_times.append(timeit.timeit(f"alg_nfact({i})", globals=globals(),number=10000))
    #print(mas_times)
    #mas_times=smooth_mas(mas_times)
    #print(mas_times)
    x = np.linspace(0, iteration, num=iteration, endpoint=True)
    mas_times =interp1d(x, mas_times, kind="cubic")

    xnew = np.linspace(0, iteration, num=iteration*1000, endpoint=True)
    plt.plot( xnew,mas_times(xnew))
    plt.grid()
    #plt.ylim([mas_times[0]-0.1,mas_times[0]+0.1])
    #plt.plot(x, mas_times)
    plt.show()

