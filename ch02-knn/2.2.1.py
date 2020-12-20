# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:39:05 2020

@author: duan
"""
import numpy as np 

def file2matrix(filename):
    with open(filename) as fr:
        files_list=fr.readlines()
        file_row_num=len(files_list)
        returnMat=np.zeros((file_row_num,3))#返回的NumPy矩阵,解析完成的数据:file_row_num行,3列
        classLabelVector = []#分类标签向量
        index=0 #NumPy矩阵的行索引
        for l in files_list:
            l=l.strip()#删除每行末尾空白符(包括'\n','\r','\t',' ')
            line_list=l.split('\t')#切片
            returnMat[index,:]=line_list[0:3]#将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
            #构造分类标签向量
            if line_list[-1] == 'didntLike':
                classLabelVector.append(1)
            elif line_list[-1] == 'smallDoses':
                classLabelVector.append(2)
            elif line_list[-1] == 'largeDoses':
                classLabelVector.append(3)
            index += 1
        return returnMat, classLabelVector
            
if __name__ == '__main__':
    #打开的文件名
    filename = "datingTestSet.txt"
    #打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    print(datingDataMat)
    print(datingLabels)        
        
