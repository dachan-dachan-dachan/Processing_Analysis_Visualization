import math
import matplotlib.pyplot as plt

def Taylor_Expansion(a, n, func, h, x):#aは中心，nは展開する最大次数，hは微分時の幅
  
    def nd_order_central_differences(xx, nd):
        if nd == 1:
            return ( func(xx+h) - func(xx-h) )/(2*h)
        else:
            return ( nd_order_central_differences(xx+h, nd-1) - nd_order_central_differences(xx-h, nd-1) ) / (2*h)
  
    n_Taylor_x_a = func(a)
    for i in range(n):
        n_Taylor_x_a += nd_order_central_differences(a, i+1) * math.pow(x-a, i+1) / math.factorial(i+1)

    return n_Taylor_x_a



x_min = 0
x_max = 3
T = 100
x = [i/T for i in range(x_min*T, x_max*T)]

def func(x):
    return math.sin(math.pi*x)

y_true = [func(i) for i in x]
a = 1
n = 5
h = 0.1
y_Taylor = [Taylor_Expansion(a, n, func, h, i) for i in x]

plt.plot(x, y_true, marker="", linestyle="-", linewidth=6, label="True")
plt.plot(x, y_Taylor, marker="", linestyle=":", linewidth=6, label=f"Taylor {a=} {n=} {h=}")
plt.xlim(x_min, x_max)
plt.ylim(-2, 2)
plt.grid()
plt.legend()
plt.show()
