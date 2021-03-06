# 神经网络整体框架
## 关于程序
    使用中文编程
    该项目只用于学习
    使用中文让我明白了我做的事情的真正含义
    代码基于唐宇迪老师所教授内容
    编程语言和版本python3.8
    该程序编写命名时可能存在逻辑性错误（裂开）

## 命名规则
### 函数命名
    文件内容是函数则文件名末尾加入“函数”，内部具体函数名不添加“函数”二字，原因是函数是一个过程或者动作
    例如某一个函数文件叫做“计算多项式”，而函数名叫“计算多项式”
    它可能是一个动宾结构
### 类命名
    文件内容是类则文件名末尾加入“类”，内部具体函数名不添加“类”二字
    原因是类是一个名词，你很明显知道的它是什么
    例如某一个类文件叫做“多层感知机类”，而类名叫“多层感知机”
### 变量命名
    它应该是一个名词，例如“预处理的数据”，“数据集”，“数据”
    可以根据上下语境简写
    它一般是由形容词加名词构成
    表示整体应该使用整体的名词，例如“激活层”表示整个激活层，意味着有大于等于一层的激活层
    表示单独的某一个时使用形容词加以具体，例如“当前激活层”，特指每次循环内需要赋值变化的激活层
### 说明
    可以分为功能性命名、数据类型命名
    最好描述清楚，例如“西塔值矩阵”，如果只命名为“西塔值”那就你知道它是什么类型了，你可能会认为它只是一个数字，而不是很多数字
    要命名准确，例如“深”和“浅”相对，最好不要用“深度”与“层数”相对，可以根据具体情况使用，例如“行”和“列”
    命名的精度和用词的数量有关，越明确用词越多，例如"某一深度内的西塔值数量"，你可能需要指明是“哪个的什么的位置的什么的什么？？？”
    可能会出现无限叠形容词的变量，例如“西塔值”，“展平的西塔值”，“优化后展平的西塔值”，
    如果你命名错了很可能导致后面使用错误的变量，甚至都认不出该变量；逻辑的严谨可以避免很多错误

## 中文编程缺陷
    部分插件，封装的包可能不支持中文......
    敲键盘时需要中英文转换......
    需要对文字足够理解才能命名正确，例如“多项式次数”，"次数"可能理解为多项式的多次方，所以建议使用“多项式项数”
    可能会为了易于理解而不得不增加文字，例如“数据集1”，“数据集1的样本数”，“数据集2”，“数据集2的样本数”，当然也可以使用"样本数1"
    你需要打出至少一个字，编程软件才能识别补足
    无法突出变量之间的区别，例如”活化的输入层数据“与”活化的输出层数据“，解决方法可以靠编辑器自动标注改色，但我没有这样的编辑器......

## 其他
    很多语言支持中文编程
    中文和英文在编程里本质都是符号，没有差别，最都会变成0，1
    但基础的ASCII编码只有英文，中文放不下，所以有些编程语言可能识别不了，但现在大都用Unicode，问题解决
    一般用于减少程序体积都是用自动化转编，例如“预处理的数据”转为“aa1“,这样体积就变小了
    
    

## 让我叠一些增益（狗头）
    本人并非语言学专业
    处于对我国文字文化的喜爱
    以上为个人认知，仅供参考，勿喷，接受指正、优化
    使用简体字编程并不意味着放弃英语
    当我发现我命名出现问题后，那一定是我逻辑出现了问题，特别是在学习状态下......
    这份代码看看就好，因为是先后逻辑，结果内容过于耦合，且序列化，一步一步的，如果前一步没看懂后一步可能没法看（裂开）
    建议初学者看《Python神经网络编程（异步图书）》，塔里克。拉希德写的
    
    