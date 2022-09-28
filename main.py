import timeit

def Multiply_matrix(user=0):
    mat1 = matrix_input()
    mat2 = matrix_input()
    ylen1 = len(mat1)
    xlen1 = len(mat1[0])
    ylen2 = len(mat2)
    xlen2 = len(mat2[0])

    if (xlen1 != ylen2):
        inp = 0
        if user:
            inp = input("Умножение таких матриц невозможно!\n Повторить операцию при других значениях?\n 1-Да 0-Нет\n")
        if inp == "1":
            return Multiply_matrix(user=1)
        else:
            return "Умножение отменено (во славу имератора конечно!)  "

    c = []
    for y in range(ylen1):
        c.append([])
        for x in range(xlen2):
            c[y].append(0)

    for y in range(ylen1):
        for x in range(xlen2):
            for g in range(xlen1):
                c[y][x] += mat1[y][g] * mat2[g][x]

    return c
def Create_matrix_with_form(matrix, xr, yr):
    lx = len(matrix[0])
    ly = len(matrix)
    gc = -1  # xxx
    temp_matrix = []

    for y in range(ly - 1):
        temp_matrix.append([])
        for x in range(lx - 1):
            temp_matrix[y].append(0)

    # print(*matrix)
    gc = -1
    gc2 = -1
    while (True):
        gc += 1
        gc_x = gc % lx
        gc_y = gc // lx
        if (gc_x != xr) and (gc_y != yr):
            gc2 += 1
            gc_x2 = gc2 % (lx - 1)
            gc_y2 = gc2 // (lx - 1)
            temp_matrix[gc_y2][gc_x2] = matrix[gc_y][gc_x]
            # print(gc_x2,gc_y2)
            if gc2 == ((lx - 1) * (ly - 1)) - 1:
                break

    return temp_matrix
def Transponse_matrix(mat):
    ylen = len(mat)
    xlen = len(mat[0])
    tmat = []
    for y in range(xlen):
        tmat.append([])
        for x in range(ylen):
            tmat[y].append(0)

    for x in range(xlen):
        for y in range(ylen):
            tmat[x][y] = mat[y][x]

    return tmat
def Determinant_matrix(matrix):
    l = len(matrix)
    if l == 1:
        return matrix[0][0]
    if l == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    if l >= 3:
        c = 0
        # print(*matrix)
        for k in range(l):  # CAN BE REPLACE BY Create_matrix_with_form()
            # print(*temp_matrix)
            c += matrix[0][k] * ((-1) ** (k + 2)) * Determinant_matrix(Create_matrix_with_form(matrix, k, 0))

        return c
Max_rank = 0
def Rang_of_matrix(matrix):
    global Max_rank

    x_len = len(matrix[0])
    y_len = len(matrix)

    if x_len == y_len:
        if x_len == 1 and matrix[0][0] != 0:
            return 1
        if x_len == 1 and matrix[0][0] == 0:
            return 0
    # print(str(matrix).replace("],", "]\n"))

    if y_len < x_len:
        matrix = Transponse_matrix(matrix)
        y_len, x_len = x_len, y_len

    old_mat = matrix.copy()
    for yy in range(y_len-x_len+1):
        matrix=old_mat[yy:yy+x_len][0:x_len]
        #print("...",matrix)
        if Determinant_matrix(matrix) != 0:
            Max_rank = max(Max_rank, x_len)
            return x_len

        else:
            for y in range(x_len):
                for x in range(x_len):
                    Rang_of_matrix(Create_matrix_with_form(matrix,x,y))
def Reverse_of_matrix(matrix):
    q = 1/Determinant_matrix(matrix)

    x_len=len(matrix[0])
    y_len = len(matrix)

    r_mat = matrix.copy()
    r_mat=Transponse_matrix(r_mat)
    for y in range(y_len):
        for x in range(x_len):
            r_mat[x][y] = q*((-1)**(x+y))*Determinant_matrix(Create_matrix_with_form(matrix,x,y))

    #print(r_mat)
    return r_mat
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

#print(timeit.timeit('Reverse_of_matrix([[5,4],[1,1]])', globals=globals(),number=1000000))                             # РАСКОММЕНТИРОВАТЬ ДЛЯ ПОЛУЧЕНИЯ РЕЗУЛЬТАТА БЫСТРОДЕЙСТВИЯ ПРОГРАММЫ
#breakpoint()

while True:
    action = Welcome_func()
    if action == 1:
        a = Transponse_matrix(matrix_input())
        for i in range(len(a)):
            print(*a[i])
    if action == 2:
        a = (Multiply_matrix(user=1))
        print("Результат умножения матриц:")
        for i in range(len(a)):
            print(*a[i])

    if action == 3:
        Rang_of_matrix(matrix_input())
        print(f"Максимальный ранг матрицы: {Max_rank}")
        Max_rank=0

    if action == 4:
        a =Reverse_of_matrix(matrix_input())
        print("\nОбратная матрица:\n")
        for i in range(len(a)):
            print(*a[i])
    print()

