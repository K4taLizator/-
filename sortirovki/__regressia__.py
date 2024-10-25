import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt





square = lambda x: -x ** 2 + 4 * x - 2
nlogn = lambda x: x * np.log2(x)
n32 = lambda x: x ** 1.5
nlog2n = lambda x: x * np.log2(x) ** 2
line = lambda x: x
n43 = lambda x: x * (4 / 3)
n54 = lambda x: x * (5 / 4)

functions = [
    (square, 'O(n^2)', 'Время выполнения с квадратичной асимптоткой'),
    (line, 'O(n)', 'Время выполнения с линейной асимптоткой'),
    (n32, 'O(n^(3/2))', 'Время выполнения с n^(3/2) асимптоткой'),
    (n43, 'O(n^(4/3))', 'Время выполнения с n^(4/3) асимптоткой'),
    (n54, 'O(n^(5/4))', 'Время выполнения с n^(5/4) асимптоткой'),
    (nlogn, 'O(n log n)', 'Время выполнения с n log n асимптоткой'),
    (nlog2n, 'O(n log^2 n)', 'Время выполнения с n log^2 n асимптоткой')
]


def draw_plot(x, func1, func2, func3, name):
    plt.figure(figsize=(9, 6))
    # Параметры графика
    plt.ylim(0, 1e4)  # Ограничение по оси Y, чтобы лучше визуализировать
    # plt.xscale('log')  # Логарифмическая шкала по оси X
    # Добавляем каждую функцию на график
    plt.plot(x, func1(x), label='Worst')
    plt.plot(x, func2(x), label='AVG')
    plt.plot(x, func3(x), label='Best')

    # Настройка графика
    plt.title('Временная сложность алгоритма {0}'.format(name))
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения')
    plt.legend()
    plt.grid()
    plt.show()


def func2(x, a, b, c, d):
    return a * x * x + b * x + c


def func1(x, a, b, c, d):
    return a * x + b


def funcn2log(x, a, b, c, d):
    return a * x ** 2 * (np.log2(x)) ** 2


def funcnlog(x, a, b, c, d):
    return a * x * np.log2(b * x) + c * x + d


def funcx(x, a, b, c, d):
    return a * x * x * x + b * x * x + c * x + d


x = np.linspace(1, 100, 1000)
y1 = lambda x: x * np.log2(x)
y2 = lambda x: x * np.log2(x) ** 2
y3 = lambda x: x ** 2
draw_plot(x, y1, y2, y2, "Shell(Pratt)")


def draw_regres(func, x, y_data):
    for j in range(4):
        y = [y_data[i] for i in range(j, len(y_data), 4)]
        popt, _ = opt.curve_fit(func, x, y)
        print(popt)
        plt.figure()
        plt.scatter(x, y, marker=".", color="red")
        plt.plot(x, func(x, popt[0], popt[1], popt[2], popt[3]))
        if (j == 0):
            plt.title('Регрессионная кривая для случаного порядка')
        if (j == 1):
            plt.title('Регрессионная кривая для отсортированного массива')
        if (j == 2):
            plt.title('Регрессионная кривая для отсортирвоанного 90/10')
        if (j == 3):
            plt.title('Регрессионная кривая для отсортированного наоборот')
        plt.xlabel('Размер массива (логарифмическая шкала)')
        plt.ylabel('Время выполнения')
        plt.grid()
        plt.show()


"""
y = [
0.0000002, 0.0000002, 0.0000002, 0.0000002, 0.0581659, 0.0556675, 0.0592483, 0.0638467, 0.3344542, 0.3351591, 0.3474805, 0.3764946, 0.8648363, 0.8612647, 0.884697, 0.9562668, 1530004, 1.6858325, 1.7092919, 1.8296632, 2.2465844, 2.2104369, 2.3684375, 2.5493482, 3.4128266, 3.350304, 3.6182455, 3.8342186, 4.3358004, 4.2978392, 4.4791767, 4.8609024, 5.5018545, 5.2758541, 5.7286825, 5.9968467, 7.1117992, 7.0023098, 7.2941484, 7.9411819, 10.1281776, 9.8459571, 10.0628369, 10.8815507, 14.1935413, 14.0552624, 14.3264987, 15.7065545
]
x = np.array([100,2000,5000,8000,11000,13000,16000,18000,20000,23000,27000,32000])
#x = np.arange(0, 1000001, 50000)
#x= np.array([0, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1300, 1500, 1700, 1900, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000])
#x = np.array([i*1000 for i in x])
draw_regres(funcx, x, y)
"""


