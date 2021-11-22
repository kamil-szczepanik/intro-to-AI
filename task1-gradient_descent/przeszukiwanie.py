from matplotlib import pyplot as plt
import numpy as np

# # funkcja 1
# def funciton(x):
#     return x**2 + x*3 + 8

# def function_prim(x):
#     return 2*x + 3

# # funkcja 2
def funciton(x):
    return x**4 - 5*x**2 - 3*x

def function_prim(x):
    return 4*x**3 - 10*x - 3

def find_minimum(start_point, wsp_ucz, max_iters, accuracy):

    x_k = start_point
    d = function_prim(x_k)

    x_points = [x_k]
    i = 0

    while (i < max_iters and abs(d)> accuracy):
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
    # x = np.arange(-3.5,1,0.1) # dla funkcji 1 (żeby wykresy były dobrze widoczne)
    x = np.arange(-2.5,3,0.1) # dla funkcji 2
    y = funciton(x)
    plt.plot(x,y, label='Przykładowa funkcjia zmienna')
    plt.plot(x_points, y_points, marker="o", markersize=4, linestyle='dashed', label='Wyniki w kolejnych iteracjach', linewidth=1)
    plt.plot(x_points[-1], y_points[-1], marker="o", markersize=6, color="r" , label=('Wynik przeszukiwania: ' + str(x_k)))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Przeszukiwanie metodą gradientu prostego dla funkcji zmiennej')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    # start_point = 0.5
    # wsp_ucz = 0.1
    # max_iters = 100
    # accuracy = 0.0001

    start_point = -0.5
    wsp_ucz = 0.05
    max_iters = 1000
    accuracy = 0.0001

    x, x_points, y_points = find_minimum(start_point, wsp_ucz, max_iters, accuracy)
    wykres(x, x_points, y_points)


