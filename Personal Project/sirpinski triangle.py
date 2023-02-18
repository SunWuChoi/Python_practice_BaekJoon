import matplotlib.pyplot as plt
from tqdm import tqdm
import random

t1 = [-100, 0]
t2 = [100, 0]
t3 = [0, 173.2]


def pickone():
    r = random.randint(1, 3)
    if r == 1:
        return t1
    elif r == 2:
        return t2
    else:
        return t3


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def isInside(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


def sirpinski(last):
    curr_x = last[0]
    curr_y = last[1]

    pivot = pickone()
    pivot_x = pivot[0]
    pivot_y = pivot[1]

    new_x = (curr_x + pivot_x) / 2
    new_y = (curr_y + pivot_y) / 2
    return new_x, new_y


def generate_init_point():
    while True:
        randomPoint = [random.randint(-100, 100), random.randint(0, 173)]
        if isInside(t1[0], t1[1], t2[0], t2[1], t3[0], t3[1], randomPoint[0], randomPoint[1]):
            return randomPoint


first_point = generate_init_point()

x = [first_point[0]]
y = [first_point[1]]

fig, ax = plt.subplots()

ax.set_xlim([-130, 130])
ax.set_ylim([-30, 200])

for i in range(100000):

    last = [x[-1], y[-1]]
    new_point = sirpinski(last)
    x.append(new_point[0])
    y.append(new_point[1])
    if i % 5 == 0:
        ax.scatter(x, y, color='black', s=1)
        plt.pause(0.1)

#ax.scatter(x, y, color='black', s=0.01)
plt.show()





