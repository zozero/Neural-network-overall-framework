import numpy as np


# sin(x)
def 计算正弦(数据集, 正弦度数):
    样本数 = 数据集.shape[0]
    正弦 = np.empty((样本数, 0))

    for 度数 in range(1, 正弦度数 + 1):
        特征的正弦 = np.sin(度数 * 数据集)
        正弦 = np.concatenate((正弦, 特征的正弦), axis=1)

    return 正弦
