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

# 粒子数を変え，複数実行した結果をとる．
# 粒子数
noOfParticles = [12, 18, 24, 30]
# 各粒子に対するMSEを格納する配列
MSEs = []
# 試行回数
trialNo = 100
# タイムステップ
timestep = 300
for i in noOfParticles:

    # データ取得
    df = pd.read_csv('C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/result' + str(i) + '.csv')
    # 全trialNo分のログ
    totalerrorSequenceOfElement = []
    for trial in range(trialNo):
        # 第1成分と第2成分の誤差合計
        errorSequenceOfElement = np.array(
            [(df.iloc[i, 1] - df.iloc[i, 2]) * (df.iloc[i, 1] - df.iloc[i, 2]) + (df.iloc[i, 3] - df.iloc[i, 4]) * (
                df.iloc[i, 3] - df.iloc[i, 4]) for i in range(timestep * trial, (timestep * trial + timestep))])
        MSEOfElement = errorSequenceOfElement.mean()
        totalerrorSequenceOfElement.append(MSEOfElement)
        print("particle = ", i, " and trial =", trial, " finished")
    MSEs.append(totalerrorSequenceOfElement)

# box plot
plt.boxplot(MSEs)
plt.grid()
