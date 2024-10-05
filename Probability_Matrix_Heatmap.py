import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
from multiprocessing import Pool

csv_file = '/Users/yulin/Desktop/人流/data/CityA ground truth data.csv'
df = pd.read_csv(csv_file)

def plot_heatmap(matrix):
    # 確保矩陣大小為201x201
    # if matrix.shape != (201, 201):
    #     raise ValueError("矩陣大小必須為201x201")
    
    # 設定顏色映射範圍
    vmin = np.min(matrix)
    vmax = np.max(matrix)
    
    # 繪製熱度圖
    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='Blues', interpolation='nearest', origin='lower', vmin=vmin, vmax=vmax)
    
    # 添加顏色條
    plt.colorbar(label='Probability')
    
    # 設置標題和標籤
    plt.title('Heatmap of Matrix')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    
    # 顯示圖形
    plt.show()

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def calculate_probability_matrix(df, uid, d=None):
    df_uid = df[df['uid'] == uid]

    if d is not None:
        df_uid = df_uid[df_uid['d'] == d]

    grid_size = 201
    probability_matrix = np.zeros((grid_size, grid_size))

    for _, row in df_uid.iterrows():
        x, y = int(row['x']), int(row['y'])
        probability_matrix[x, y] += 1

    total_count = len(df_uid)
    if total_count > 0:
        probability_matrix /= total_count

    return probability_matrix


def get_sd(df, uid, d_cat, max_d):
    arr = np.empty((max_d//7, 201, 201))
    for d in range(d_cat, max_d, 7):
        arr[d//7] = calculate_probability_matrix(df, uid, d)*1000
    
    result = arr.std(axis=0)
    return result

def cal_mse(matrix: np.ndarray):
    return ((matrix**2).mean())**0.5

def get_uid_sd(u:int):
    print(u)
    day_lim = 14 ## <===調天數

    sd_arr = np.empty((7, ))
    for cat in range(7):
        sd_arr[cat] = cal_mse(get_sd(df, u, cat, day_lim))

    return sd_arr

if __name__ == "__main__":
    uids = range(10) ## <===調人數

    with Pool(multiprocessing.cpu_count()-1) as pool:
        uid_sds = pool.map(get_uid_sd, uids)

    plot_heatmap(np.array(uid_sds).mean(axis=0).reshape((1, 7)))
