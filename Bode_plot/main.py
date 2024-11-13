from matplotlib import pyplot as plt
import math


def G(s):
    T = 10
    g = 1 / (T*s + 1)
    return g

def Decibels(g):
    return 20*math.log10(abs(g))

def Phase(g):
    return math.degrees( math.atan2(g.imag, g.real) )



def main():
    fig, (ax_gain, ax_phase) = plt.subplots(2, 1, figsize=(8, 10))
    
    ax_gain.set_xscale("log")
    ax_gain.set_ylabel("Gain [dB]")

    ax_phase.set_xscale("log")
    ax_phase.set_ylabel("Phase [deg]")
    ax_phase.set_xlabel("Angular velocity [rad/s]")


    x_min = 10 ** -2
    x_max = 10 ** 3

    ax_gain.set_xlim(x_min, x_max)
    ax_phase.set_xlim(x_min, x_max)


    omega = []
    r = 1.2
    tem = x_min
    while tem < x_max:
        tem *= r
        omega.append(tem)


    gain = [Decibels( G((1j)*i) ) for i in omega]
    ax_gain.plot(omega, gain)


    phase = [Phase( G(1j*i) ) for i in omega]
    ax_phase.plot(omega, phase)

    plt.show()


if __name__ == "__main__":
    main()
