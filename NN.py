import random
import math

n = 0  # количество эпох
MM = [3, 3]  # положение мыши
MM1 = [0, 0]
vector = []
N = 4

'''Генерация матрицы NхN'''
matrix = []
for i in range(N):
    matrix.append([])
    for _ in range(N):
        matrix[i].append(random.random())
print(matrix)


def exploration_rate(n, min_rate=0.1):
    """ Метод для вычисления коэффициента 'любопытства'.
        Чем дольше мы обучаемся, тем больше мы опираемся на политику и меньше на рандом."""
    if random.uniform(0, 1) >= max(min_rate, min(1, 1.0 - math.log10((n + 1) / 25))):
        return action()
    else:
        return Random()


def go(y):
    global MM
    if y == 1:
        if MM[1] - 1 >= 0:  # смотрим значение слева
            return y
    elif y == 2:
        if MM[0] - 1 >= 0:  # смотрим значение сверху
            print('2 как блять?', MM[0] - 1)
            return y
    elif y == 3:
        if MM[1] + 1 < N:  # смотрим значение справа
            if MM[1] + 1 < N:
                print('я дурак или лыжи не едут?', MM[1],MM[1] + 1)
                return y
    elif y == 4:
        if MM[0] + 1 < N:  # смотрим значение снизу
            if MM[0] + 1 < N:
                print("да ну", MM[0] + 1)
                return y
    else:
        print('return 0')
        return 0


'''Функция принятия рандомного действия'''
def Random():
    global MM
    print('рандом')
    q = random.randint(1, 4)  # генерируем случайное действие
    if q == 1:
        if MM[1] - 1 >= 0:  # смотрим значение слева
            return q
    elif q == 2:
        if MM[0] - 1 >= 0:  # смотрим значение сверху
            return q
    elif q == 3:
        if MM[1] + 1 < N:  # смотрим значение справа
            return q
    else:
        if MM[0] + 1 < N:  # смотрим значение снизу
            return q
    return Random()


def action():  # вычисляется оптимальный ход, выводит значение от 1 до 4, в зависимости от того куда стоит сделать ход
    global MM, MM1
    vector.clear()
    MM1 = [0, 0]  # временное положение мыши для вычислений
    if go(1) !=0:  # смотрим значение слева
        MM1 = MM
        MM1[1] -= 1
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector первым значением запишем слева от мыши
    else:
        vector.append(0)
    if go(2) !=0:  # смотрим значение сверху
        MM1 = MM
        MM1[0] -= 1
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector вторым значением запишем сверху от мыши
    else:
        vector.append(0)
    if go(3) !=0:  # смотрим значение справа
        MM1 = MM
        MM1[1] += 1
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector третьим значением запишем справа от мыши
    else:
        vector.append(0)
    if go(4) !=0:  # смотрим значение снизу
        MM1 = MM
        MM1[0] += 1
        vector.append(matrix[int(MM1[0])][int(MM1[1])])  # в вектор vector четвёртым значением запишем снизу от мыши
    else:
        vector.append(0)
    # if go(vector.index(max(vector))) != 0:
    print('vector:', vector, max(vector), 1 + vector.index(max(vector)))
    return 1 + vector.index(max(vector)) # так как список значений имеет вид 0-3, а действия в системе обозначены как 1-4
    # else:



'''основной цикл просчета пути'''
for i in range(5000):  # MM => [строка, столбец]
    n = i
    # while (MM[0] != N - 1 and MM[1] != N - 1):
    #     pass
    ER = exploration_rate(n)
    print(MM)
    print(ER)
    if ER == 1:
        MM[1] -= 1
    elif ER == 2:
        MM[0] -= 1
    elif ER == 3:
        MM[1] += 1
    else:
        MM[0] += 1

    print(MM)
    # print(matrix)
    # for _ in matrix:
    #     print(_)

    print()

    for i in range(N):
        print()
        for _ in range(N):
            if MM[0] == i and MM[1] == _:
                print('#', end='')
            else:
                print('*', end='')

    """опишем поощирения"""
    # пока не описал
    if MM[0] == N - 1 and MM[1] == N - 1:  # положение сыра в клетке NxN
        print('really???')