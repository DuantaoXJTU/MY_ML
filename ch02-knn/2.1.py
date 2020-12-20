# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:08:55 2020

@author: duan
"""
import numpy as np
import operator
import collections

def createDataSet():
    group = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
    labels = ['爱情片','爱情片','爱情片','动作片','动作片','动作片']
    return group,labels

"""
Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果
"""
# 函数说明:kNN算法,分类器

def classify0(inX, dataSet, labels, k):
    
    dataSetSize = dataSet.shape[0]#numpy函数shape[0]返回dataSet的行数
    #在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    #二维特征相减后平方
    sqDiffMat = diffMat**2
    #sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    #开方，计算出距离
    distances = sqDistances**0.5
    #返回distances中元素从小到大排序后的索引值 前面的几个对应就是distance最小的label的索引
    sortedDistIndices = distances.argsort()
    #定一个记录类别次数的字典
    #classCount = {}
    
    
    classCount = collections.Counter()
    for i in range(k):
        #取出前k个元素的类别  前k个distance最小的
        voteIlabel = labels[sortedDistIndices[i]]
        #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        #计算类别次数
        #若使用classCount = {}，必须classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        #若用counter计数，可以直接classCount[voteIlabel] +=1
        #classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        classCount[voteIlabel] +=1
   
    #key=operator.itemgetter(1)根据字典的值进行排序
    #key=operator.itemgetter(0)根据字典的键进行排序
    #reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]
    #sorted后得到的是一个以原来字典键值对组成元组作为元素的列表    [('x1',y1),('x2',y2)......]

if __name__ == '__main__':
    #创建数据集
    group, labels = createDataSet()
    #测试集
    test = [101,20]
    #kNN分类
    test_class = classify0(test, group, labels, 3)
    #打印分类结果
    print(test_class)