import numpy as np
import random
import matplotlib.pyplot as plt
import time
import NN
y = np.array([])
rr = 0
r = []
rrr = []
def learn(k):
    global y, r, rr, rrr
    for i in range(1000):
        while True:
            # time.sleep(0.1)
            NN.pk(k)
            if NN.tr == 1:

                rr += 1  # x
                rrr.append(rr)
                r.append(NN.ct)  # y
                break

    x = np.array(rrr)
    y = np.array(r)  # Шаги до цели
    data = np.column_stack((x, y))
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
    ax.set_xlabel('$эпоха$')
    ax.set_ylabel('$количество шагов до сыра$')
    # plt.show()

    f = open('sourse/'+str(int(np.mean(r))).split('.')[0]+'.txt', 'w')
    # for i in NN.matrix:
    #     f.write(str(i))
    print(np.mean(r))

    for i in NN.matrix:
        for _ in range(NN.N):
            f.write(str(i[_])+' ')
        f.write('\n')
    f.close()
    r.clear()
    rr = 0
    rrr.clear()
    y = 0
    x = 0
    data = 0


def chek():
    # global NN.matrix
    ct = -1
    ct1 = -1
    f = open('sourse/30.txt', 'r')
    for i in f.read().split("\n"):
        i.strip()
        ct += 1  # строка
        i = i.split(' ')
        i.pop()
        # print(i)
        for _ in i:
            NN.matrix[ct][ct1] = int(_)
            ct1 += 1
        ct1 = -1
    NN.pk(0)
    # NN.render(2)


def test(k):
    # chek()  # подгружаем нужную матрицу из файла
    NN.render(0)
    for i in range(k):
        NN.F()  # вызывем функцию обучения (создания матрицы)
        learn(0)  # производим проверку сгенерированной матрицы 1000 раз
        # NN.render(2)
test(1000)