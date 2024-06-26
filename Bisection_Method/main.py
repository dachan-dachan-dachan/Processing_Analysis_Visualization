import matplotlib.pyplot as plt
import math

def func(x):
    y = math.sinh(x)
    y = x**3 - x**2 - 0.5
    return y


def x_on_0(func, d_error, x_min, x_max):#二分法
    max_calc_times = 10000
    calc_times = 0
    while ( abs(x_min - x_max) > d_error ) and (calc_times < max_calc_times):
        x_center = (x_min + x_max)/2
        y_on_center = func(x_center)
        if y_on_center == 0:
            x_mim = x_center
            x_max = x_center
            break
        elif y_on_center > 0:
            sign = 1
        else:
            sign = -1
        if func(x_min) * sign > 0:
            x_min = x_center
        else:
            x_max = x_center
        
        calc_times += 1
    
    if calc_times == max_calc_times:
        print("規定の計算回数では解が収束しませんでした")
    print(f"x = {x_center} , error = {abs(x_min - x_max)}")
    return x_center



x_min = -1
x_max = 2
N = 1000
d_error = 0.001

x = []
y = []
for i in range(N+1):
    tem = x_min + (x_max - x_min)*i/N
    #tem = 2*i/N
    x.append(tem)
    y.append(func(tem))


plt.plot(x, y, marker="p", linestyle="", markersize=1, zorder=1)
x_on_zero = x_on_0(func, d_error, x_min, x_max)
y_on_zeor = func(x_on_zero)
plt.plot(x_on_zero, y_on_zeor, marker="x", linestyle="", markersize=8, zorder=2, color="red")
plt.plot(x_on_zero, y_on_zeor, marker="+", linestyle="", markersize=12, zorder=2, color="red")
plt.xlabel("X axis", fontsize=10)
plt.ylabel("Y axis", fontsize=10)
plt.xlim(x_min, x_max)
#plt.axis("equal")
plt.grid()
plt.show()
