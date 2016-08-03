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
df = pd.read_csv( 'C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/result.csv' )
# アンサンブルの集合データを取得
#df_ensamble = pd.read_csv( 'C:/Users/Hitoshi_Nakamura/Documents/Eclipse_workspace/Filtering/ensambleresult.csv' )
plt.plot( df.iloc[:, 0], df.iloc[:, 1] , label = 'true_theta' )# θの真値
plt.plot( df.iloc[:, 0], df.iloc[:, 2] , label = 'estimate_theta' )# θの推定値
plt.plot( df.iloc[:, 0], df.iloc[:, 3] , label = 'true_theta_dot' )# θ_dotの真値
plt.plot( df.iloc[:, 0], df.iloc[:, 4] , label = 'estimate_theta_dot' )# θ_dotの推定値
plt.grid( True )
plt.xlabel( 'Value' )
plt.ylabel( 'Time Series' )
plt.title( 'Target & Estimate of PF' )
plt.xlim( [0, 10000] ) # x軸の範囲
plt.ylim( [-0.5, 0.5] ) # y軸の範囲
plt.legend( loc = 'best' )# 凡例
# plt.savefig( trialName + prob + 'paratofront.pdf' );

# ヒストグラムの表示(縮退を起こしていないかチェック)
plt.figure()
plt.subplot(221)
plt.hist( df_ensamble.iloc[int( whenOfPartDist1 ), :], bins = 50, label = 'ensamble histogram' )
plt.axvline( x = df.iloc[whenOfPartDist1, 1], color = "red", lw = 5, label = 'true value' )     # x=~に沿ってx軸垂直に引く
plt.axvline( x = df.iloc[whenOfPartDist1, 2], color = "green", lw = 5, label = 'estimated value' )     # x=~に沿ってx軸垂直に引く
title = 'Distribution of Particle at t=' + str( whenOfPartDist1 )
plt.xlim( [-0.4, 0.4] )
plt.title( title )
plt.xlabel( 'x' )
plt.ylabel( 'freq' )
plt.legend( loc = 'best' )# 凡例
plt.subplot(222)
plt.hist( df_ensamble.iloc[int( whenOfPartDist2 ), :], bins = 50, label = 'ensamble histogram' )
plt.axvline( x = df.iloc[whenOfPartDist2, 1], color = "red", lw = 5, label = 'true value' )     # x=~に沿ってx軸垂直に引く
plt.axvline( x = df.iloc[whenOfPartDist2, 2], color = "green", lw = 5, label = 'estimated value' )     # x=~に沿ってx軸垂直に引く
title = 'Distribution of Particle at t=' + str( whenOfPartDist2 )
plt.xlim( [-0.4, 0.4] )
plt.title( title )
plt.xlabel( 'x' )
plt.ylabel( 'freq' )
plt.legend( loc = 'best' )# 凡例
plt.subplot(223)
plt.hist( df_ensamble.iloc[int( whenOfPartDist3 ), :], bins = 50, label = 'ensamble histogram' )
plt.axvline( x = df.iloc[whenOfPartDist3, 1], color = "red", lw = 5, label = 'true value' )     # x=~に沿ってx軸垂直に引く
plt.axvline( x = df.iloc[whenOfPartDist3, 2], color = "green", lw = 5, label = 'estimated value' )     # x=~に沿ってx軸垂直に引く
title = 'Distribution of Particle at t=' + str( whenOfPartDist3 )
plt.xlim( [-0.4, 0.4] )
plt.title( title )
plt.xlabel( 'x' )
plt.ylabel( 'freq' )
plt.legend( loc = 'best' )# 凡例
plt.subplot(224)
plt.hist( df_ensamble.iloc[int( whenOfPartDist4 ), :], bins = 50, label = 'ensamble histogram' )
plt.axvline( x = df.iloc[whenOfPartDist4, 1], color = "red", lw = 5, label = 'true value' )     # x=~に沿ってx軸垂直に引く
plt.axvline( x = df.iloc[whenOfPartDist4, 2], color = "green", lw = 5, label = 'estimated value' )     # x=~に沿ってx軸垂直に引く
title = 'Distribution of Particle at t=' + str( whenOfPartDist4 )
plt.xlim( [-0.4, 0.4] )
plt.title( title )
plt.xlabel( 'x' )
plt.ylabel( 'freq' )
plt.legend( loc = 'best' )# 凡例

# 平均と95%区間を同時にプロットする．
# x軸
time = range( len( df_ensamble ) )
# 平均値
mean = df_ensamble.mean( 1 ).values

# 95%区間
semVal = df_ensamble.apply( sem, axis = 1 ).mul( 1.65 ).values
plt.figure()
plt.fill_between( time, mean - semVal ,
                 mean + semVal, color = "#3F5D7D" )
plt.xlabel( 'Value' )
plt.ylabel( 'Time Series' )
plt.xlim( [8000, 10000] ) # x軸の範囲
plt.ylim( [-0.5, 0.5] ) # y軸の範囲
plt.plot( time, mean, color = "yellow", lw = 2 )
plt.title( "Mean Value and 90% Intervals of Ensamble", fontsize = 22 )
plt.grid( True )
plt.show()













