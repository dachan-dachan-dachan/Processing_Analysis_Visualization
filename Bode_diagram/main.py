from matplotlib import pyplot as plt
import math


def G(s):
    T = 0.1
    g = 1 / (T*s + 1)
    return g

def Decibels(g):
    return 20*math.log10(abs(g))

def Phase(g):
    return math.degrees( math.atan2(g.imag, g.real) )



def main():
    fig, (ax_gain, ax_phase) = plt.subplots(2, 1, figsize=(8, 10))

    x_min = 10 ** -1
    x_max = 10 ** 4

    ax_gain.set_xlim(x_min, x_max)
    ax_phase.set_xlim(x_min, x_max)


    r = 1.2
    tem = x_min
    omega = [tem]
    while tem < x_max:
        tem *= r
        omega.append(tem)


    gain = [Decibels( G((1j)*i) ) for i in omega]
    ax_gain.plot(omega, gain)


    phase = [Phase( G(1j*i) ) for i in omega]
    ax_phase.plot(omega, phase)


    #軸の設定
    ax_gain.set_xscale("log")
    ax_gain.set_ylabel("Gain [dB]")
    ax_gain.grid(which="major", linestyle="--")
    ax_gain.grid(axis="x", which="minor", linestyle="--")

    ax_phase.set_xscale("log")
    ax_phase.set_ylabel("Phase [deg]")
    ax_phase.set_xlabel("Angular velocity [rad/s]")
    ax_phase.grid(which="major", linestyle="--")
    ax_phase.grid(axis="x", which="minor", linestyle="--")


    #縦軸の上限下限調整
    d = 20
    y_lim_max = d * ( ( max(gain) // d ) + 1 )
    y_lim_min = d * ( min(gain) // d )
    width = y_lim_max - y_lim_min
    tem_y = y_lim_min
    tem = [tem_y]
    while tem_y < y_lim_max:
        tem_y += d
        tem.append(tem_y)

    if y_lim_max - max(gain) < 0.1 * width:
        y_lim_max += 0.1 * width
    if  min(gain) - y_lim_min < 0.1 * width:
        y_lim_min -= 0.1 * width

    ax_gain.set_ylim(y_lim_min, y_lim_max)
    ax_gain.set_yticks(tem)


    d = 45
    y_lim_max = d * ( ( max(phase) // d ) + 1 )
    y_lim_min = d * ( min(phase) // d )
    width = y_lim_max - y_lim_min
    tem_y = y_lim_min
    tem = [tem_y]
    while tem_y < y_lim_max:
        tem_y += d
        tem.append(tem_y)

    if y_lim_max - max(phase) < 0.1 * width:
        y_lim_max += 0.1 * width
    if  min(phase) - y_lim_min < 0.1 * width:
        y_lim_min -= 0.1 * width

    ax_phase.set_ylim(y_lim_min, y_lim_max)
    ax_phase.set_yticks(tem)


    plt.show()


if __name__ == "__main__":
    main()
