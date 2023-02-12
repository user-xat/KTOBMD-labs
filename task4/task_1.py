############ Задача 1. Аппроксимация функции #############
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


# Исхоодная функция
def f(x: np.ndarray) -> np.ndarray:
    return np.sin(x/5) * np.exp(x/10) + 5*np.exp(-x/2)


# Вычисление приближения через многочлен
def f_approx(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    y = np.array([0]*x.size, dtype=np.float64)
    for i in range(x.size):
        n = 0
        for wi in w:
            y[i] += wi * x[i]**n
            n += 1
    return y


# Возвращает матрицу коэффициентов A
def get_A(x: np.ndarray) -> np.ndarray:
    a = np.zeros((x.size, x.size))
    for i in range(x.size):
        for j in range(x.size):
            a[i, j] = x[i]**j
    return a


if __name__ == '__main__':
    # отрезок на котором функция f(x) определена
    x_beg, x_end = 1, 15

    # Многочлен 1 степени
    x = np.linspace(x_beg, x_end, 2)
    A = get_A(x)
    b = f(x)
    w_1 = linalg.solve(A, b)

    # Многочлен 2 степени
    x = np.linspace(x_beg, x_end, 3)
    A = get_A(x)
    b = f(x)
    w_2 = linalg.solve(A, b)

    # Многочлен 3 степени
    x = np.linspace(x_beg, x_end, 4)
    A = get_A(x)
    b = f(x)
    w_3 = linalg.solve(A, b)

    # Вывод резултата в файл
    with open('submission-2.txt', 'w') as fout:
        fout.write('{} {} {} {}'.format(w_3[0], w_3[1], w_3[2], w_3[3]))

    # Настройка рисунка
    plt.figure(figsize=(10, 8))
    plt.xlabel("Ось x")
    plt.ylabel("Ось y")
    plt.title("Аппроксимация", fontsize=20)
    plt.xticks(np.arange(0, 15.1, 1))
    plt.yticks(np.arange(0, 4, 0.25))
    plt.grid()

    x = np.linspace(1, 15, 1000, dtype=np.float64)
    # Оригинальная функция
    plt.plot(x, f(x), lw=2.3, label="y=sin(x/5)*exp(x/10) + 5*exp(-x/2)")
    # Приближения
    plt.plot(x, f_approx(x, w_1), color="orange",
             linestyle=":", label="y={:.3f}+{:.3f}*x".format(w_1[0], w_1[1]))
    plt.plot(x, f_approx(x, w_2), color="green",
             linestyle="--", label="y={:.3f}+{:.3f}*x+{:.3f}*x^2".format(w_2[0], w_2[1], w_2[2]))
    plt.plot(x, f_approx(x, w_3), color="red",
             linestyle="-.", label="y={:.3f}+{:.3f}*x+{:.3f}*x^2+{:.3f}*x^3".format(w_3[0], w_3[1], w_3[2], w_3[3]))

    # Отображение
    plt.legend()
    plt.show()
