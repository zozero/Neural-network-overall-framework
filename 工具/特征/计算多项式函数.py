import numpy as np

from 工具.特征.归一化函数 import 归一化


def 计算多项式(数据集, 多项式项数, 是否归一化=False):
    分割的特征 = np.array_split(数据集, 2, axis=1)
    数据集1 = 分割的特征[0]
    数据集2 = 分割的特征[1]

    (数据集1的样本数, 数据集1的特征数) = 数据集1.shape
    (数据集2的样本数, 数据集2的特征数) = 数据集2.shape

    if 数据集1的样本数 != 数据集2的样本数:
        raise ValueError('无法为具有不同行数的两组数据生成多项式')
    if 数据集1的特征数 != 数据集2的特征数:
        raise ValueError('无法为具有不同列数的两组数据生成多项式')

    if 数据集1的特征数 == 0:
        数据集1 = 数据集2
    if 数据集2的特征数 == 0:
        数据集2 = 数据集1

    特征数 = 数据集1的特征数 if 数据集1的特征数 < 数据集2的特征数 else 数据集2的特征数
    数据集1 = 数据集1[:, :特征数]
    数据集2 = 数据集2[:, :特征数]

    多项式 = np.empty((数据集1的样本数, 0))

    for i in range(1, 多项式项数 + 1):
        for j in range(i + 1):
            特征的多项式 = (数据集1 ** (i - j)) * (数据集2 ** j)
            多项式 = np.concatenate((多项式, 特征的多项式), axis=1)

    if 是否归一化:
        多项式 = 归一化(多项式)[0]

    return 多项式
