# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:11:03 2020

@author: duan

function:
    加载数据，并将数据可视化，判断数据是否线性可分
"""

# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

"""
函数说明:读取数据

Parameters:
    fileName - 文件名
Returns:
    dataMat - 数据矩阵
    labelMat - 数据标签

"""
def loadDataSet(fileName):
    dataMat = []; labelMat = []  #注意 这里将数据先存到列表中 -->后续需要将数据转化成array 
    fr = open(fileName)
    for line in fr.readlines():                                     #逐行读取，滤除空格等
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])      #添加数据 注意 这里将list存在 元素中
        labelMat.append(float(lineArr[2]))                          #添加标签
    return dataMat,labelMat

"""
函数说明:数据可视化

Parameters:
    dataMat - 数据矩阵
    labelMat - 数据标签
Returns:
    无
"""
def showDataSet(dataMat, labelMat):
    data_plus = []                                  #正样本
    data_minus = []                                 #负样本
    for i in range(len(dataMat)):
        if labelMat[i] > 0:
            data_plus.append(dataMat[i])
        else:
            data_minus.append(dataMat[i])
    data_plus_np = np.array(data_plus)              #转换为numpy矩阵 转换成一个有len(dataMat)行 两列的矩阵
    data_minus_np = np.array(data_minus)            #转换为numpy矩阵
    #plt.scatter的两个参数是横纵坐标 分别是数据矩阵的第一列、第二列。x=data_plus_np[:,0]可以取到第一列
    #np.transpose(data_plus_np)[0]也可以取到第一列--转置后取第一行
    plt.scatter(np.transpose(data_plus_np)[0], np.transpose(data_plus_np)[1])   #正样本散点图
    plt.scatter(np.transpose(data_minus_np)[0], np.transpose(data_minus_np)[1]) #负样本散点图
    plt.show()

if __name__ == '__main__':
    dataMat, labelMat = loadDataSet('testSet.txt')
    showDataSet(dataMat, labelMat)
