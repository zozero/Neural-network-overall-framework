# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas

from 多层感知机类 import 多层感知机

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 数据 = pandas.read_csv('./数据/mnist-demo.csv', nrows=30)
    数据 = pandas.read_csv('./数据/mnist-demo.csv')

    # 展示数据
    # 展示数量 = 25
    # 单元数 = math.ceil(math.sqrt(展示数量))
    # plt.figure(figsize=(10, 10))
    # for 绘图索引 in range(展示数量):
    #     数字 = 数据[绘图索引:绘图索引 + 1].values
    #     数字标签 = 数字[0][0]
    #     数字像素点 = 数字[0][1:]
    #     图片大小 = int(math.sqrt(数字像素点.shape[0]))
    #     帧 = 数字像素点.reshape((图片大小, 图片大小))
    #     plt.subplot(单元数, 单元数, 绘图索引 + 1)
    #     plt.imshow(帧, cmap='Greys')
    #     plt.title(数字标签)
    # plt.subplots_adjust(wspace=0.5, hspace=0.5)
    # plt.show()

    训练数据 = 数据.sample(frac=0.8)
    测试数据 = 数据.drop(训练数据.index).values
    训练数据 = 训练数据.values

    # 训练样本数 = 30
    训练样本数 = 5000
    # 第一列是标签,得去掉
    x训练 = 训练数据[:训练样本数, 1:]
    y训练 = 训练数据[:训练样本数, [0]]

    x测试 = 测试数据[:, 1:]
    y测试 = 测试数据[:, [0]]

    # 层数可以改为行列数
    行列数 = [784, 25, 10]

    是否归一化 = True
    最大迭代次数 = 500
    阿尔法 = 0.1

    感知机 = 多层感知机(x训练, y训练, 行列数, 是否归一化)
    损失值矩阵 = 感知机.训练(最大迭代次数, 阿尔法)
    西塔值矩阵 = 感知机.西塔值矩阵

    # plt.plot(range(len(损失值矩阵)),损失值矩阵)
    # plt.xlabel("grident")
    # plt.ylabel("costs")
    # plt.show()

    预测结果 = 感知机.预测(x测试)
    准确率 = np.sum(y测试 == 预测结果) / y测试.shape[0] * 100
    print("准确率", 准确率)

    展示数量 = 64
    单元数 = math.ceil(math.sqrt(展示数量))
    plt.figure(figsize=(15, 15))
    for 绘图索引 in range(展示数量):
        标签 = y测试[绘图索引, 0]
        数据 = x测试[绘图索引, :]
        预测标签 = 预测结果[绘图索引][0]

        图片大小 = int(math.sqrt(数据.shape[0]))
        帧 = 数据.reshape((图片大小, 图片大小))
        颜色 = 'Greens' if 标签 == 预测标签 else 'Reds'
        plt.subplot(单元数, 单元数, 绘图索引 + 1)
        plt.imshow(帧, cmap=颜色)
        plt.title(预测标签)
        plt.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()
