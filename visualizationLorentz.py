'''
Created on 2016/06/19
visualization by python
@author: Hitoshi_Nakamura
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from scipy.stats import sem

# 粒子のヒストグラムを見る際，何回目の結果を見たいか
whenOfPartDist1 = 1000
whenOfPartDist2 = 4000
whenOfPartDist3 = 7000
whenOfPartDist4 = 9000
# データ取得
df = pd.read_csv('C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/result.csv')
# アンサンブルの集合データを取得
# df_ensamble = pd.read_csv( 'C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/ensambleresult.csv' )
plt.plot(df.iloc[:, 0], df.iloc[:, 1], label='true_x1')  # x1の真値
plt.plot(df.iloc[:, 0], df.iloc[:, 2], label='estimate_x1')  # x1の推定値
plt.plot(df.iloc[:, 0], df.iloc[:, 3], label='true_x2')  # x2の真値
plt.plot(df.iloc[:, 0], df.iloc[:, 4], label='estimate_x2')  # x2の推定値
plt.plot(df.iloc[:, 0], df.iloc[:, 5], label='true_x3')  # x3の真値
plt.plot(df.iloc[:, 0], df.iloc[:, 6], label='estimate_x3')  # x3の推定値
plt.grid(True)
plt.xlabel('Value')
plt.ylabel('Time Series')
plt.title('Target & Estimate of PF')
plt.xlim([0, len(df.iloc[:, 1])])  # x軸の範囲
plt.ylim([-50, 50])  # y軸の範囲
plt.legend(loc='best')  # 凡例
# plt.savefig( trialName + prob + 'paratofront.pdf' );

# 第1成分の誤差
errorSequenceOfElement1 = np.array(
    [(df.iloc[i, 1] - df.iloc[i, 2]) * (df.iloc[i, 1] - df.iloc[i, 2]) for i in range(len(df.iloc[:, 1]))])
MSEOfElement1 = errorSequenceOfElement1.mean()
# 第2成分の誤差
errorSequenceOfElement2 = np.array([(df.iloc[i, 3] - df.iloc[i, 4]) * (df.iloc[i, 3] - df.iloc[i, 4]) for i in
                                    range(len(df.iloc[:, 3]))])
MSEOfElement2 = errorSequenceOfElement2.mean()
# 第3成分の誤差
errorSequenceOfElement3 = np.array([(df.iloc[i, 5] - df.iloc[i, 6]) * (df.iloc[i, 5] - df.iloc[i, 6]) for i in
                                    range(len(df.iloc[:, 5]))])
MSEOfElement3 = errorSequenceOfElement3.mean()
print(MSEOfElement1)
print(MSEOfElement2)
print(MSEOfElement3)