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
from matplotlib.pyplot import boxplot

# Lorentz実験において，複数実行した結果をとる．

# 試行回数
trialNo = 30
# タイムステップ
timestep = 300

# 試行の結果を追加してゆく箱
MSEs = []

# データ取得
df = pd.read_csv('C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/result.csv')
# 全trialNo分のログ
# 第1成分
totalerrorSequenceOfElement1 = []
# 第2成分
totalerrorSequenceOfElement2 = []
# 第3成分
totalerrorSequenceOfElement3 = []
# 第1~3成分
totalerrorSequenceOfElement = []
for trial in range(trialNo):
    # 第1成分の誤差
    errorSequenceOfElement1 = np.array(
        [(df.iloc[i, 1] - df.iloc[i, 2]) * (df.iloc[i, 1] - df.iloc[i, 2]) for i in
         range(timestep * trial, (timestep * trial + timestep))])
    MSEOfElement = errorSequenceOfElement1.mean()
    totalerrorSequenceOfElement1.append(MSEOfElement)
    # 第2成分の誤差
    errorSequenceOfElement2 = np.array(
        [(df.iloc[i, 3] - df.iloc[i, 4]) * (df.iloc[i, 3] - df.iloc[i, 4]) for i in
         range(timestep * trial, (timestep * trial + timestep))])
    MSEOfElement = errorSequenceOfElement2.mean()
    totalerrorSequenceOfElement2.append(MSEOfElement)
    # 第3成分の誤差
    errorSequenceOfElement3 = np.array(
        [(df.iloc[i, 5] - df.iloc[i, 6]) * (df.iloc[i, 5] - df.iloc[i, 6]) for i in
         range(timestep * trial, (timestep * trial + timestep))])
    MSEOfElement = errorSequenceOfElement3.mean()
    totalerrorSequenceOfElement3.append(MSEOfElement)

    # 第1成分と第2成分の誤差合計
    errorSequenceOfElement = np.array(
        [(df.iloc[i, 1] - df.iloc[i, 2]) * (df.iloc[i, 1] - df.iloc[i, 2]) + (df.iloc[i, 3] - df.iloc[i, 4]) * (
            df.iloc[i, 3] - df.iloc[i, 4]) + (df.iloc[i, 5] - df.iloc[i, 6]) * (
             df.iloc[i, 5] - df.iloc[i, 6]) for i in range(timestep * trial, (timestep * trial + timestep))])
    MSEOfElement = errorSequenceOfElement.mean()
    totalerrorSequenceOfElement.append(MSEOfElement)
    print("trial =", trial, " finished")
# 1~3, 1, 2, 3 成分MSEをそれぞれ加えてゆく．
MSEs.append(totalerrorSequenceOfElement)
MSEs.append(totalerrorSequenceOfElement1)
MSEs.append(totalerrorSequenceOfElement2)
MSEs.append(totalerrorSequenceOfElement3)

# create different box plot
# create boxplot of sum
axsum = plt.axes()
# create boxplot of each element
axeach = axsum.twinx()  # x軸を共有するという意味
# plt.hold(True) hold true

# box plot of sum
axsum.boxplot(MSEs[0], positions=[0])
# change ylim
axsum.set_ylim(0, 700)

# box plot of each element
axeach.boxplot(MSEs[1], positions=[1])
axeach.boxplot(MSEs[2], positions=[2])
axeach.boxplot(MSEs[3], positions=[3])
axeach.set_ylim(0, 350)

# x軸を-1から4に変更
axeach.set_xlim(-1, 4)

# x軸のメモリを，0,1,2,3に設定する．データ範囲のどこに目盛りが入るか
axeach.set_xticks([0, 1, 2, 3])

# メモリにラベルを設定する．
axeach.set_xticklabels(["sum", "x1", "x2", "x3"])

# グリッドをつける．
axeach.grid()
# 一気にboxplotを作るコマンド
# plt.boxplot(MSEs)
