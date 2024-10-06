import pandas as pd
import matplotlib.pyplot as plt
import os

# 讀取資料
city_name = 'CityA'
data = pd.read_csv('/Users/yulin/Desktop/人流/data/'+city_name+' ground truth data.csv')

# Filter out rows where both x and y are equal to 999
filtered_data = data[(data['x'] != 999) | (data['y'] != 999)]

# 將 (x, y) 轉換為 location_id
data['location_id'] = data['x'].astype(str) + '_' + data['y'].astype(str)

# 定義一個函數來計算每個使用者最常去的前兩個地點的佔比
def calculate_top2_ratios(group):
    loc_counts = group['location_id'].value_counts()
    if len(loc_counts) >= 2:
        top1, top2 = loc_counts.iloc[0], loc_counts.iloc[1]
    elif len(loc_counts) == 1:
        top1, top2 = loc_counts.iloc[0], 0
    else:
        top1, top2 = 0, 0
    total = loc_counts.sum()
    return pd.Series({'top1_ratio': top1 / total, 'top2_ratio': top2 / total})

# 對每個使用者計算 top1 和 top2 的比例
ratios = data.groupby('uid').apply(calculate_top2_ratios)

# 設定圖片儲存路徑
save_path = '/Users/yulin/Desktop/人流/img/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 畫出 top1_ratio 和 top2_ratio 的散佈圖
plt.figure(figsize=(8, 6))
plt.scatter(ratios['top1_ratio'], ratios['top2_ratio'], alpha=0.5, s=.5)
plt.title(city_name+'Location Visit Ratios')
plt.xlabel('Top1 Ratio')
plt.ylabel('Top2 Ratio')
plt.grid(True)

# 儲存圖片
file_name=city_name+'_top.png'
plt.savefig(os.path.join(save_path, file_name))

plt.show()

