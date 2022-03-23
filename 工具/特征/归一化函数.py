import numpy as np


def 归一化(特征):
    归一化的特征 = np.copy(特征).astype(float)

    特征均值 = np.mean(特征, 0)
    特征标准差 = np.std(特征, 0)

    # 计算标准差
    if 特征.shape[0] > 1:
        归一化的特征 -= 特征均值

    # 防止除以0
    特征标准差[特征标准差 == 0] = 1
    归一化的特征 /= 特征标准差

    return 归一化的特征, 特征均值, 特征标准差
