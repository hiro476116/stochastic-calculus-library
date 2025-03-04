import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(T, N, mu=0, sigma=1):
    """
    ブラウン運動（ウィーナー過程）のシミュレーション
    T: 総時間
    N: ステップ数
    mu: ドリフト項（通常は0）
    sigma: 拡散項
    """
    dt = T / N
    t = np.linspace(0, T, N+1)
    increments = np.random.normal(loc=mu*dt, scale=sigma*np.sqrt(dt), size=N)
    W = np.empty(N+1)
    W[0] = 0
    W[1:] = np.cumsum(increments)
    return t, W

def ornstein_uhlenbeck_process(T, N, theta=1, mu=0, sigma=1, X0=0):
    """
    オーンシュタイン‐ウーレンベック過程のシミュレーション
    T: 総時間
    N: ステップ数
    theta: 平均回帰速度
    mu: 長期平均値
    sigma: 拡散項
    X0: 初期値
    """
    dt = T / N
    t = np.linspace(0, T, N+1)
    X = np.empty(N+1)
    X[0] = X0
    for i in range(1, N+1):
        dW = np.random.normal(scale=np.sqrt(dt))
        X[i] = X[i-1] + theta*(mu - X[i-1])*dt + sigma*dW
    return t, X

def plot_processes(save_path='plot.pdf'):
    T = 10.0    # 総時間
    N = 100000   # シミュレーションのステップ数
    
    # 各確率過程のシミュレーション
    t, W = brownian_motion(T, N)
    t_ou, X = ornstein_uhlenbeck_process(T, N)
    
    # プロットの作成
    plt.figure(figsize=(12, 6))
    
    # ブラウン運動のプロット
    plt.subplot(1, 2, 1)
    plt.plot(t, W, label='Brownian Motion')
    plt.title("Brownian Motion")
    plt.xlabel("time")
    plt.ylabel("W(t)")
    plt.legend()
    plt.tight_layout()
    # PDFファイルとして保存
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    # "my_plot.pdf" にプロットを保存します
    plot_processes('./visualize/visuzlize.pdf')
