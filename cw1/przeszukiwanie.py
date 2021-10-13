from matplotlib import pyplot as plt
import numpy as np


def funciton(x):
    return x**2 + x*3 + 8

def function_prim(x):
    return 2*x + 3

def find_minimum(start_point, wsp_ucz, max_iters, accuracy):

    x_k = start_point
    d = function_prim(x_k)

    x_points = [x_k]
    i = 0

    while (i < 100 and abs(d)> accuracy):
        d = function_prim(x_k)
        x_k = x_k - wsp_ucz*d
        i += 1
        x_points.append(x_k)

    y_points = []
    for x_point in x_points:
        y_points.append(funciton(x_point))

    print("Wynik: ", x_k)
    print("Liczba iteracji: ", i)

    return x_k, x_points, y_points


def wykres(x_k, x_points, y_points):
    x = np.arange(-3.5,1,0.1)
    y = funciton(x)
    plt.plot(x,y, label='Przykładowa funkcjia zmienna')
    plt.plot(x_points, y_points, marker="o", markersize=4, linestyle='dashed', label='Wyniki w kolejnych iteracjach')
    plt.plot(x_points[-1], y_points[-1], marker="o", markersize=6, color="r" , label=('Wynik przeszukiwania: ' + str(x_k)))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Przeszukiwanie metodą gradientu prostego dla funkcji zmiennej')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x, x_points, y_points = find_minimum(-3, 0.9, 100, 0.0001)
    wykres(x, x_points, y_points)


