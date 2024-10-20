# 3D circle slit
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift


def circle1(x, y):
    return np.where(x**2 + y**2 < 0.05 * 0.05, 1, 0)

def circle2(x, y):
    return np.where(x**2 + y**2 < 0.1 * 0.1, 1, 0)

def single1(x, y):
    return np.where(np.abs(x) < 0.05, 1, 0)

def single2(x, y):
    return np.where(np.abs(x) < 0.1, 1, 0)

def double1(x, y):
    slit_width = 0.05
    slit_distance = 0.1
    return np.where((np.abs(x + slit_distance) < slit_width / 2) |
                    (np.abs(x - slit_distance) < slit_width / 2), 1, 0)

def double2(x, y):
    slit_width = 0.08
    slit_distance = 0.1
    return np.where((np.abs(x + slit_distance) < slit_width / 2) |
                    (np.abs(x - slit_distance) < slit_width / 2), 1, 0)

def double3(x, y):
    slit_width = 0.05
    slit_distance = 0.15
    return np.where((np.abs(x + slit_distance) < slit_width / 2) |
                    (np.abs(x - slit_distance) < slit_width / 2), 1, 0)

slits = {
    "circle1": circle1,
    "circle2": circle2,
    "ss1": single1,
    "ss2": single2,
    "ds1": double1,
    "ds2": double2,
    "ds3": double3,
}


def plot(name, f):
    # 2D グリッドを作成
    N = 200  # グリッドサイズを大きくする
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, y)

    # 関数の評価
    Z = f(X, Y)

    # 2次元フーリエ変換を計算
    FZ = fft2(Z)

    # フーリエ変換の中心をシフト (視覚化のため)
    FZ_shifted = fftshift(FZ)

    # フーリエ変換の絶対値（振幅）を計算
    amplitude = np.abs(FZ_shifted)

    # 元の関数をプロット
    plt.figure()
    plt.imshow(Z, extent=(-1, 1, -1, 1))
    plt.colorbar()
    plt.show()
    plt.savefig(f"../figures/result/{name}_original_estimation.png")

    # フーリエ変換の振幅をプロット
    plt.figure()
    plt.imshow(amplitude, extent=(-N/2, N/2, -N/2, N/2))
    plt.colorbar()
    plt.show()
    plt.savefig(f"../figures/result/{name}_amplitude_estimation.png")

for name, f in slits.items():
    plot(name, f)
