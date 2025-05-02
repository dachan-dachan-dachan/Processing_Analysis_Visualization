from matplotlib import pyplot as plt
import math


def G(s):
    T = 0.1
    g = 1 / (T*s + 1)
    return g

def Decibels(omega):
    de = [20*math.log10( abs( G( (1j)*i ) ) ) for i in omega]
    return de

def Phase(omega):
    g = G( (1j)*omega[0] )
    ph = [math.degrees( math.atan2( g.imag, g.real) )]
    for i in range(len(omega)-1):
        g = G( (1j)*omega[i+1] )
        ph_tem = math.degrees( math.atan2( g.imag, g.real) )

        n = round( math.fabs( ph[-1] - ph_tem ) / 360 )
        if 0 < n:#前後の角度の差が180度より大きい場合．atan2の性質により不連続になってしまっている．
            if ph[-1] < ph_tem:#下から上に一気に飛んだ場合
                ph_tem = - (360*n - ph_tem)
            else:#上から下に一気に飛んだ場合
                ph_tem = (360*n + ph_tem)
        
        ph.append(ph_tem)

    return ph



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


    gain = Decibels(omega)
    ax_gain.plot(omega, gain)


    phase = Phase(omega)
    ax_phase.plot(omega, phase)

    #軸，罫線の設定
    ax_gain.set_xscale("log")
    ax_gain.set_ylabel("Gain [dB]")
    ax_gain.grid(which="major", linestyle="--")
    ax_gain.grid(axis="x", which="minor", linestyle="--")

    ax_phase.set_xscale("log")
    ax_phase.set_ylabel("Phase [deg]")
    ax_phase.set_xlabel("Angular velocity [rad/s]")
    ax_phase.grid(which="major", linestyle="--")
    ax_phase.grid(axis="x", which="minor", linestyle="--")

    #最大・最小，罫線の間隔の設定
    d = 20
    y_max = d*( int(max(gain))//d ) + d
    y_min = d*( int(min(gain))//d )
    ax_gain.set_ylim( y_min, y_max )
    ax_gain.set_yticks( [i for i in range( y_min, y_max+d, d )] )
    
    d = 45
    y_max = d*( int(max(phase))//d ) + d
    y_min = d*( int(min(phase))//d )
    ax_phase.set_ylim( y_min, y_max )
    ax_phase.set_yticks( [i for i in range( y_min, y_max+d, d )] )


    plt.show()


if __name__ == "__main__":
    main()
