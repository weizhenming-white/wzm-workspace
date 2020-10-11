#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-09 16:02
brief:学习numpy基础
"""


import numpy as np


def eg2_1():
    """
    2.1 NumPy 数组对象
    """
    # 使用arange创建数组
    a = np.arange(5)
    # 获取其数据类型
    print a.dtype
    # 获取数组的属性
    print a.shape


def eg2_2():
    """
    2.2 动手实践：创建多维数组
    """
    # 创建二维数组，并查看
    a = np.array([np.arange(2), np.arange(2)])
    print a
    # 显示该数组的维度
    print a.shape


def eg2_3():
    """
    2.3 动手实践：创建自定义数据类型
    """
    # 创建数据类型
    t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
    print t
    # 查看某一段数据类型
    print t['name']


def eg2_4():
    """
    2.4 一维数组的索引和切片
    """
    # 用下标3~7来选取元素3~6：
    a = np.arange(9)
    print a[3:7]
    # 也可以用下标0~7，以2为步长选取元素：
    print a[:7:2]
    # 和Python中一样，我们也可以利用负数下标翻转数组：
    print a[::-1]


def eg2_5():
    """
    2.5 动手实践：多维数组的切片和索引
    """
    # (1)先用arange函数创建一个数组并改变其维度，使之变成一个三维数组：
    b = np.arange(24).reshape(2, 3, 4)
    print b
    # (2)可以用三维坐标来选定任意一个房间，即楼层、行号和列号。例如，选定第1层楼、
    # 第1行、第1列的房间（也可以说是第0层楼、第0行、第0列，这只是习惯问题），可以这样表示：
    print b[0, 0, 0]
    # (3) 如果我们不关心楼层，也就是说要选取所有楼层的第1行、第1列的房间，那么可以将第1
    # 个下标用英文标点的冒号:来代替：
    print b[:, 0, 0]
    # 我们还可以这样写，选取第1层楼的所有房间：
    print b[0, :, :]
    # 多个冒号可以用一个省略号（...）来代替，因此上面的代码等价于：
    print b[0, ...]
    # 进而可以选取第1层楼、第2排的所有房间：
    print b[0, 1, :]
    # (4) 再进一步，我们可以在上面的数组切片中间隔地选定元素：
    print b[0, 1, ::2]
    # (5) 如果要选取所有楼层的位于第2列的房间，即不指定楼层和行号，用如下代码即可：
    print b[:, :, 1]
    # 类似地，我们可以选取所有位于第2行的房间，而不指定楼层和列号：
    print b[:, 1, :]
    # 如果要选取第1层楼的所有位于第2列的房间，在对应的两个维度上指定即可：
    print b[0, :, 1]
    # (6) 如果要选取第1层楼的最后一列的所有房间，使用如下代码：
    print b[0, :, -1]
    # 如果要反向选取第1层楼的最后一列的所有房间，使用如下代码：
    print b[0, ::-1, -1]
    # 在该数组切片中间隔地选定元素：
    print b[0, ::2, -1]
    # 如果在多维数组中执行翻转一维数组的命令，将在最前面的维度上翻转元素的顺序，在我们
    # 的例子中将把第1层楼和第2层楼的房间交换：
    print b[::-1]


def eg2_6():
    """
    2.6 动手实践：改变数组的维度
    """
    # (1) ravel 我们可以用ravel函数完成展平的操作：
    b = np.arange(24).reshape(2, 3, 4)
    print b.ravel()
    # (2) flatten 这个函数恰如其名，flatten就是展平的意思，与ravel函数的功能相同。
    # 不过，flatten函数会请求分配内存来保存结果，而ravel函数只是返回数组的一个视图（view）：
    print b.flatten()
    # (3) 用元组设置维度 除了可以使用reshape函数，我们也可以直接用一个正整数元组来设置数组的维度，如下所示：
    b.shape = (6, 4)
    print b
    # (4) transpose 在线性代数中，转置矩阵是很常见的操作。对于多维数组，我们也可以这样做：
    print b.transpose()
    # (5) resize resize和reshape函数的功能一样，但resize会直接修改所操作的数组：
    b.resize((2, 12))
    print b


def eg2_7():
    """
    2.7 数组的组合
        NumPy数组有水平组合、垂直组合和深度组合等多种组合方式，我们将使用vstack、
    dstack、hstack、column_stack、row_stack以及concatenate函数来完成数组的组合。
    """
    pass


def eg2_8():
    """
    2.8 动手实践：组合数组
    """
    # 首先，我们来创建一些数组：
    a = np.arange(9).reshape(3, 3)
    print a
    b = a * 2
    print b
    # (1) 水平组合 我们先从水平组合开始练习。将ndarray对象构成的元组作为参数，传给
    # hstack函数。如下所示：
    print np.hstack((a, b))
    # 我们也可以用concatenate函数来实现同样的效果，如下所示：
    print np.concatenate((a, b), axis=1)
    # (2) 垂直组合 垂直组合同样需要构造一个元组作为参数，只不过这次的函数变成了
    # vstack。如下所示：
    print np.vstack((a, b))
    # (3) 深度组合 将相同的元组作为参数传给dstack函数，即可完成数组的深度组合。所谓
    # 深度组合，就是将一系列数组沿着纵轴（深度）方向进行层叠组合。举个例子，有若干张二维平
    # 面内的图像点阵数据，我们可以将这些图像数据沿纵轴方向层叠在一起，这就形象地解释了什么
    # 是深度组合。
    print np.dstack((a, b))
    # (4) 列组合 column_stack函数对于一维数组将按列方向进行组合，如下所示：
    oned = np.arange(2)
    twice_oned = 2 * oned
    print np.column_stack((oned, twice_oned))
    # 而对于二维数组，column_stack与hstack的效果是相同的：
    print np.column_stack((a, b))
    # 我们可以用==运算符来比较两个NumPy数组，是不是很简洁？
    print np.column_stack((a, b)) == np.hstack((a, b))
    # (5) 行组合 当然，NumPy中也有按行方向进行组合的函数，它就是row_stack。对于两
    # 个一维数组，将直接层叠起来组合成一个二维数组。
    print np.row_stack((oned, twice_oned))
    # 对于二维数组，row_stack与vstack的效果是相同的：
    print np.row_stack((a, b))
    print np.row_stack((a, b)) == np.vstack((a, b))


def eg2_9():
    """
    2.9 数组的分割
        NumPy数组可以进行水平、垂直或深度分割，相关的函数有hsplit、vsplit、dsplit和
    split。我们可以将数组分割成相同大小的子数组，也可以指定原数组中需要分割的位置。
    """
    pass


def eg2_10():
    """
    2.10 动手实践：分割数组
    """
    # (1) 水平分割 下面的代码将把数组沿着水平方向分割为3个相同大小的子数组：
    a = np.arange(9).reshape(3, 3)
    print a
    print np.hsplit(a, 3)
    # 对同样的数组，调用split函数并在参数中指定参数axis=1，对比一下结果：
    print np.split(a, 3, axis=1)
    # (2) 垂直分割 vsplit函数将把数组沿着垂直方向分割：
    print np.vsplit(a, 3)
    # 同样，调用split函数并在参数中指定参数axis=0，也可以得到同样的结果：
    print np.split(a, 3, axis=0)
    # (3) 深度分割 不出所料，dsplit函数将按深度方向分割数组。我们先创建一个三维数组：
    c = np.arange(27).reshape(3, 3, 3)
    print c
    print np.dsplit(c, 3)


def eg2_11():
    """
    2.11 数组的属性
        除了shape和dtype属性以外，ndarray对象还有很多其他的属性，在下面一一列出。
    """
    # ndim属性，给出数组的维数，或数组轴的个数：
    b = np.arange(24).reshape(2, 12)
    print b
    print b.ndim
    # size属性，给出数组元素的总个数，如下所示：
    print b.size
    # itemsize属性，给出数组中的元素在内存中所占的字节数：
    print b.itemsize
    # 如果你想知道整个数组所占的存储空间，可以用nbytes属性来查看。这个属性的值其实
    # 就是itemsize和size属性值的乘积：
    print b.nbytes
    # T属性的效果和transpose函数一样，如下所示：
    b.resize(6, 4)
    print b
    print b.T
    # 对于一维数组，其T属性就是原数组：
    c = np.arange(5)
    print c
    print c.ndim
    print c.T
    # 在NumPy中，复数的虚部是用j表示的。例如，我们可以创建一个由复数构成的数组：
    d = np.array([1.j + 1, 2.j + 3])
    print d
    # real属性，给出复数数组的实部。如果数组中只包含实数元素，则其real属性将输出原
    # 数组：
    print d.real
    # imag属性，给出复数数组的虚部：
    print d.imag
    # 如果数组中包含复数元素，则其数据类型自动变为复数型：
    print d.dtype
    print d.dtype.str
    # flat属性将返回一个numpy.flatiter对象，这是获得flatiter对象的唯一方式——我
    # 们无法访问flatiter的构造函数。这个所谓的“扁平迭代器”可以让我们像遍历一维数
    # 组一样去遍历任意的多维数组，如下所示：
    e = np.arange(4).reshape(2, 2)
    print e
    f = e.flat
    print f
    for item in f:
        print item
    # 我们还可以用flatiter对象直接获取一个数组元素：
    print e.flat[2]
    # 或者获取多个元素：
    print b.flat[[1, 3]]
    # flat属性是一个可赋值的属性。对flat属性赋值将导致整个数组的元素都被覆盖：
    e.flat = 7
    print e


def eg2_12():
    """
    2.12 动手实践：数组的转换
        我们可以使用tolist函数将NumPy数组转换成Python列表。
    """
    # (1) 转换成列表：
    b = np.array([1 + 1j, 3 + 2j])
    print b.tolist()
    # (2) astype函数可以在转换数组时指定数据类型：
    print b.astype(int)
    # 在上面将复数转换为整数的过程中，我们丢失了复数的虚部。astype函数
    # 也可以接受数据类型为字符串的参数。
    print b.astype('complex')


def eg2_13():
    """
    2.13 本章小结
        在本章中，我们学习了很多NumPy的基础知识：数据类型和NumPy数组。对于数组而言，
    有很多属性可以用来描述数组，数据类型就是其中之一。在NumPy中，数组的数据类型是用对象
    来完善表示的。
        类似于Python列表，NumPy数组也可以方便地进行切片和索引操作。在多维数组上，NumPy
    有明显的优势。
        涉及改变数组维度的操作有很多种——组合、调整、设置维度和分割等。在这一章中，对很
    多改变数组维度的实用函数进行了说明。这样的处理。
    在学习完基础知识后，我们将进入到第3章来学习NumPy中的常用函数，包括基本数学函数
    和统计函数等。
    """
    pass


if __name__ == '__main__':
    eg2_12()