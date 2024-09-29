import math
import matplotlib.pyplot as plt


def Transfer_Function(u, a):
    y = math.exp(u) - 1
    return y

def func(x, A, n):
    omega = math.pi / n
    u = A * math.sin(omega*x)
    return u


if __name__ == "__main__":
    x_min = 0
    x_max = 100
    T = 1000
    a = 0.8
    A = 1.2
    n = 3

    x = [i/T for i in range(int(x_min*T), int(x_max*T))]
    u = [func(i, A, n) for i in x]
    y = [Transfer_Function(i, a) for i in u]
    
    S = 0
    s = []
    for i in range(len(x) - 1):
        S += (y[i] + y[i+1])*(x[i+1] - x[i])/2
        if i == 0:
            tem = 0
        else:
            tem = S/(x[i] - x[0])
        s.append(tem)
    
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.plot(x, u, marker="", linestyle="--", linewidth=3, label="input" + " : " + r"$u = A\sin\frac{x}{n}$" + "   " + f"({A = } , {n = })", zorder=2)
    ax.plot(x, y, marker="", linestyle="-", linewidth=3, label="output" + " : " + r"$y = e^u - 1$", zorder=1)
    ax.plot(x[:len(x)-1], s, marker="", linestyle="-.", linewidth=3, label="Time average" + " : " + r"$\bar y = \frac{1}{x}\int_{0}^{x}ydx$", zorder=3)

    ax.set_xlim(x_min, x_max)
    ax.set_xlabel("x [Time]")
    min_y = min( min(y) , min(u) )
    max_y = max( max(y) , max(u) )

    tem = (A**2)/4
    d = 1 / ( max_y - min_y )
    ytick = []
    ytick_label = []
    ytick_2 = []
    ytick_label_2 = []
    for i in range( int( min_y - 1 ) , int( max_y + 2 ) ):
        if i <= tem and tem < i+1:
            if tem < i + d:
                ytick.append(tem)
                ytick_label.append(r"$\frac{A^2}{4}$")
            else:
                ytick.append(tem)
                ytick_label.append(r"$\frac{A^2}{4}$")
                ytick.append(i)
                ytick_label.append(f"{i:.0f}")
        else:
            ytick.append(i)
            ytick_label.append(f"{i:.0f}")
        

        if i <= s[-1] and s[-1] < i+1:
            ytick_2.append(s[-1])
            ytick_label_2.append(f"{s[-1]:.2f}")
        else:
            ytick_2.append(i)
            ytick_label_2.append("")
        
    ax.set_yticks(ytick)
    ax.set_yticklabels(ytick_label)
    ax2.set_yticks(ytick_2)
    ax2.set_yticklabels(ytick_label_2)
    ax.grid()
    ax.legend()
    plt.show()
