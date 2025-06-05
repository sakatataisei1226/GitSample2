import numpy as np

def calculate_electric_field(potential, dx, dy):
    """
    電位から電場を計算する関数
    
    Parameters:
    -----------
    potential : numpy.ndarray
        電位の2次元配列
    dx : float
        x方向の格子間隔
    dy : float
        y方向の格子間隔
    
    Returns:
    --------
    Ex : numpy.ndarray
        x方向の電場成分
    Ey : numpy.ndarray
        y方向の電場成分
    """
    # 電場の計算（中心差分法）
    Ex = -(potential[1:, :] - potential[:-1, :]) / dx
    Ey = -(potential[:, 1:] - potential[:, :-1]) / dy
    
    return Ex, Ey

def plot_electric_field(x, y, Ex, Ey, potential):
    """
    電場と電位をプロットする関数
    
    Parameters:
    -----------
    x : numpy.ndarray
        x座標の配列
    y : numpy.ndarray
        y座標の配列
    Ex : numpy.ndarray
        x方向の電場成分
    Ey : numpy.ndarray
        y方向の電場成分
    potential : numpy.ndarray
        電位の2次元配列
    """
    import matplotlib.pyplot as plt
    
    # 電場のプロット
    plt.figure(figsize=(12, 5))
    
    # 電位の等高線
    plt.subplot(121)
    plt.contour(x, y, potential, levels=20, cmap='viridis')
    plt.colorbar(label='電位 [V]')
    plt.title('電位分布')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    
    # 電場ベクトル
    plt.subplot(122)
    plt.quiver(x[:-1, :-1], y[:-1, :-1], Ex, Ey, scale=50)
    plt.title('電場ベクトル')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    
    plt.tight_layout()
    plt.show()

# 使用例
if __name__ == "__main__":
    # 座標の設定
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # 点電荷による電位の計算（例：原点に点電荷がある場合）
    k = 9e9  # クーロン定数
    q = 1e-9  # 電荷量
    r = np.sqrt(X**2 + Y**2)
    potential = k * q / r
    
    # 電場の計算
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    Ex, Ey = calculate_electric_field(potential, dx, dy)
    
    # 結果のプロット
    plot_electric_field(X, Y, Ex, Ey, potential) 