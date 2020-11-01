import numpy as np
import random
import matplotlib.pyplot as plt
import time
import NN
y = np.array([])
rr = 0
r = []
rrr = []
for i in range(1000):
    while True:
        # time.sleep(0.1)
        NN.pk(0)
        if NN.tr == 1:

            rr += 1  # x
            rrr.append(rr)
            r.append(NN.ct)  # y
            break
x = np.array(rrr)
y = np.array(r)
# print(x, y)
# for i in range(10):
    # y.append(random.randint(1,10))
data = np.column_stack((x, y))
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')

ax.set_xlabel('$эпоха$')
ax.set_ylabel('$количество шагов до сыра$')

plt.show()