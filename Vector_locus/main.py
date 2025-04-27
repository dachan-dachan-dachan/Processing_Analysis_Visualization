from matplotlib import pyplot as plt
import numpy as np
import math


def G(s):
    g = 60 / ( ( s * (s+2) * (s+6) ) + 60 )
    return g

def add_circle():
    omega = np.linspace(0, 2, 100)
    x = np.cos(np.pi*omega)
    y = np.sin(np.pi*omega)
    plt.plot(x, y, marker="", linestyle="--", linewidth=1, color="gray")


def main():

    omega_min = 10 ** -1
    omega_max = 10 ** 4

    Re_Im_zero = None
    Abs_one = None

    r = 1.001
    tem = omega_min
    Re_G = []
    Im_G = []
    while tem <= omega_max:
        G_tem = G(tem*(1j))
        Re_G.append(G_tem.real)
        Im_G.append(G_tem.imag)

        tem *= r

        if Im_G[-1] <= 0 and 0 <= G(tem*(1j)).imag and Re_Im_zero == None:
            Re_Im_zero = G(tem*(1j)).real
            plt.plot([Re_Im_zero], [G(tem*(1j)).imag], marker="o", linestyle="", markersize=7, color="blue")
            print(f"{Re_Im_zero = } , GM = {math.fabs(1/Re_Im_zero)}")
        
        if 1 <= abs( Re_G[-1] + (Im_G[-1]*(1j)) ) and abs(G(tem*(1j))) <= 1 and Abs_one == None:
            Abs_one = [G(tem*(1j)).real , G(tem*(1j)).imag]
            plt.plot([Abs_one[0], 0], [Abs_one[1], 0], marker="o", linestyle="--", markersize=7, linewidth=1, color="black")
            print(f"{Abs_one = } , angle = {math.degrees( math.atan2(Abs_one[1], Abs_one[0]) )} degree , PM = {math.degrees( math.atan2(Abs_one[1], Abs_one[0]) ) - 180}")

    plt.plot(Re_G, Im_G, marker="", linestyle="-", linewidth=2, color="green")


    plt.plot([-1], [0], marker="o", linestyle="", markersize=7, color="red")
    add_circle()
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
