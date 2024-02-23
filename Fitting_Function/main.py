import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import math


######################################################
def func(x):#両対数における折れ線近似
    if x < 100:
        return 101*(x**(-0.85))
    else:
        return 35*(x**(-0.62))

pict_name = "HOGE.png"#データシートのグラフの画像
x_min = 0.1
x_max = 100000
y_min = 0.01
y_max = 10
base = 10#ログの底
######################################################


if __name__ == "__main__":

    #<データシードの画像を背景に設定する>
    background_image = mpimg.imread(pict_name)#画像の読み込み
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect("equal", adjustable="box")
    ax.imshow(background_image, extent=[0, 100, 0, 100], aspect="auto", alpha=1)#画像を背景に設定
  
    #axの軸の数値を非表示
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True)
    #</データシードの画像を背景に設定する>

    #<自分で設定した関数を描画する>
    #両対数軸を追加
    ax_log = fig.add_axes(ax.get_position(), frameon=False)
    ax_log.set_xscale("log" ,base=base)
    ax_log.set_yscale("log" ,base=base)
    ax_log.set_xlim(x_min, x_max)
    ax_log.set_ylim(y_min, y_max)
    
    #関数を描写
    N = 100000#分割回数
    x_values = np.logspace(math.log(x_min, base), math.log(x_max, base), N, base=base)
    y_values = []
    for i in x_values:
        y_values.append(func(i))
    ax_log.plot(x_values, y_values, label="func", color="blue", linestyle="--")
    ax_log.grid(True)
    #</自分で設定した関数を描画する>
    
    
    # グラフの表示
    plt.show()
