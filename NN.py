import random
import math
import time

n = 0
y = 0
q = 0
h = 0
ER = 0
ct = 0
t = 0
tr = 0
MM = [0, 0]  # (начальное) положение мыши
MM1 = [0, 0]
vector = []
vec = []
N = 10  # матрица NхN
nn = 500000  # количество эпох

'''Генерация матрицы NхN'''
matrix = []
for i in range(N):
    matrix.append([])
    for _ in range(N):
        # matrix[i].append(random.random())
        matrix[i].append(0)


# print(matrix)


def exploration_rate(n, min_rate=0.1):
    """ Метод для вычисления коэффициента 'любопытства'.
        Чем дольше мы обучаемся, тем больше мы опираемся на политику и меньше на рандом."""
    if random.uniform(0, 1) >= max(min_rate, min(1, 1.0 - math.log10(
            (n + 1) / (nn / 10)))):  # Чем меньше число, тем больший рандом
        return action()
    else:
        return Random()


''' функция проверки возможности хода в нужную сторону '''


def go(y):
    global MM
    if y == 1:
        if MM[1] - 1 >= 0:  # смотрим значение слева
            # print('1) MM в go:', MM, MM[1] - 1)
            return y
    elif y == 2:
        if MM[0] - 1 >= 0:  # смотрим значение сверху
            # print('2) MM в go:', MM, MM[0] - 1)
            return y
    elif y == 3:
        if MM[1] + 1 < N:  # смотрим значение справа
            # print('3) MM в go:', MM, MM[1] + 1)
            return y
    elif y == 4:
        if MM[0] + 1 < N:  # смотрим значение снизу
            # print('4) MM в go:', MM, MM[0] + 1)
            return y
    else:
        # print('return 0')
        return 0


'''Функция принятия рандомного действия'''


def Random():
    global MM, h, q
    q = random.randint(1, 4)
    # print('рандом =', q)
    h = go(q)
    # print('h = go(q)', h)
    if h in [1, 2, 3, 4]:
        return h
    else:
        Random()


'''Функция принятия осознанного действия'''


def action():  # вычисляется оптимальный ход, выводит значение от 1 до 4, в зависимости от того куда стоит сделать ход
    global MM, MM1
    # print('action')
    vector.clear()
    MM1 = [0, 0]  # временное положение мыши для вычислений
    if go(1) in [1, 2, 3, 4]:  # смотрим значение слева
        MM1 = MM[:]
        MM1[1] -= 1
        # print('1) MM1 в action:', MM1)
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector первым значением запишем слева от мыши
    else:
        vector.append(0)
    if go(2) in [1, 2, 3, 4]:  # смотрим значение сверху
        MM1 = MM[:]
        MM1[0] -= 1
        # print('2) MM1 в action:', MM1)
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector вторым значением запишем сверху от мыши
    else:
        vector.append(0)
    if go(3) in [1, 2, 3, 4]:  # смотрим значение справа

        MM1 = MM[:]
        MM1[1] += 1
        # print('3) MM1 в action:', MM1)
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector третьим значением запишем справа от мыши
    else:
        vector.append(0)
    if go(4) in [1, 2, 3, 4]:  # смотрим значение снизу
        MM1 = MM[:]
        MM1[0] += 1
        # print('4) MM1 в action:', MM1)
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector четвёртым значением запишем снизу от мыши
    else:
        vector.append(0)
    # if go(vector.index(max(vector))) != 0:
    # print('vector:', vector, max(vector), 1 + vector.index(max(vector)))
    if max(vector) == 0:
        vector[vector.index(max(vector))] = -100000000000
        if max(vector) == 0:
            if True:
                # print(vector.index(max(vector)))
                # vec = vector[:]
                vector[vector.index(max(vector))] = -100000000000
                # print(vector)
    # print('vector:', vector, max(vector), 1 + vector.index(max(vector)))
    return 1 + int(vector.index(max(vector)))  # так как список значений имеет вид 0-3,
    # а действия в системе обозначены как 1-4


'''Функция рендора матрицы в виде картинки и в числовом представлении'''


def render(x):
    global matrix, MM
    if x == 3 or x == 1:
        for i in range(N):
            for _ in range(N):
                if MM[0] == i and MM[1] == _:
                    print('.', end=' ')
                else:
                    print('#', end=' ')
            print()
    if x == 3 or x == 2:
        for i in matrix:
            for _ in range(N):
                print(round(i[_] / matrix[N - 1][N - 1], 5), end=' ')
            print()


'''основной цикл просчета пути'''

for i in range(nn):  # MM => [строка, столбец]
    # time.sleep(0.1)
    ER = exploration_rate(i)
    # print(MM)
    # print(ER)
    if ER == 1:
        MM[1] -= 1
    elif ER == 2:
        MM[0] -= 1
    elif ER == 3:
        MM[1] += 1
    elif ER == 4:
        MM[0] += 1
    # print(MM)

    # render()
    # print(MM)
    # print(matrix)
    ct += 500
    # float(matrix[MM[0]][MM[1]]) - float(ct)
    # matrix[MM[0]][MM[1]] = float(matrix[MM[0]][MM[1]]) + 0.05

    """опишем поощирения"""
    if MM[0] == N - 1 and MM[1] == N - 1:  # положение сыра в клетке NxN
        # print('really???')
        matrix[N - 1][N - 1] = matrix[N - 1][N - 1] + 5000
        MM = [0, 0]
        MM1 = [0, 0]
        ct = 0
    # matrix[MM[0]][MM[1]] = matrix[MM[0]][MM[1]] + 5
    matrix[MM[0]][MM[1]] = matrix[MM[0]][MM[1]] - ct

render(2)


def pk(k):
    global MM, MM1, ER, ct
    ct = 0
    MM = [0, 0]
    for i in range(1000):
        ct += 1
        # time.sleep(0.5)
        ER = exploration_rate(i + (nn // 3))
        # print(action())
        # print(MM)
        # print(ER)
        if ER == 1:
            # print(ER, MM[0])
            MM[1] -= 1
        elif ER == 2:
            # print(ER, MM[0])
            MM[0] -= 1
        elif ER == 3:
            # print(ER, MM[0])
            MM[1] += 1
        elif ER == 4:
            # print(ER, MM[0])
            MM[0] += 1

        render(k)
        # print()

        if MM[0] == N - 1 and MM[1] == N - 1:  # положение сыра в клетке NxN
            # print(ct)
            break
            # MM = [0, 0]
            # MM1 = [0, 0]

tr = 1


# pk(1)
