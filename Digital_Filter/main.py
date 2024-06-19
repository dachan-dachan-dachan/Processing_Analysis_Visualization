from matplotlib import pyplot as plt
import math


def low_path_filter(x, a):
    y = []
    for i in range(len(x)):
        if i == 0:
            tem = x[0]
        else:
            tem = a*y[i-1] + (1-a)*x[i]
        y.append(tem)
    return y

def high_path_filter(x, a):
    y = []
    for i in range(len(x)):
        if i == 0:
            tem = x[0]
        else:
            tem = ( x[i] - a*x[i-1] )/(1-a)
        y.append(tem)
    return y


def func(t):
    a = 10
    b = 0.1
    return 0.3*math.sin(a*t) + math.sin(b*t)

t = []
x = []
N = 10000
start = 0
end = 100
for i in range(N+1):
    tem = start + (i/N)*( end - start )
    t.append(tem)
    x.append( func(tem) )

a = 0.99
plt.ylim(-2,2)
linewidth = 2.5
plt.plot(t, x, marker="", linestyle="-", linewidth=linewidth, label="Original", zorder=1)

l = low_path_filter(x, a)
#l = high_path_filter(x, a)
#l = low_path_filter(l, a)
plt.plot(t, l, marker="", linestyle="-", linewidth=linewidth, label="low path filter", zorder=2)


l = low_path_filter(l, a)
plt.plot(t, l, marker="", linestyle="-", linewidth=linewidth, label="2 times low path filter", zorder=3)

"""
low_path = low_path_filter(x, a)
#plt.plot(t, low_path, label="low path filter")
for i in range(10):
    low_path = low_path_filter(low_path, a)
plt.plot(t, low_path, label="low path filter")
"""

"""
high_path = high_path_filter(x, a)
#plt.plot(t, high_path, label="high path filter")
for i in range(2):
    high_path = high_path_filter(high_path, a)
plt.plot(t, high_path, label="high path filter")
"""
plt.legend()
plt.show()

