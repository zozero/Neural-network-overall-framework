from 工具.特征 import 训练集预处理


class 多层感知机:
    def __init__(self, 数据, 标签, 层数, 是否归一化=False):
        print("【信息】多层感知机类")
        预处理的数据 = 训练集预处理(数据, 是否归一化)
