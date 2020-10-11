#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-11 20:26
brief:学习numpy常用函数
    在本章中，我们将学习NumPy的常用函数。具体来说，我们将以分析历
史股价为例，介绍怎样从文件中载入数据，以及怎样使用NumPy的基本数学
和统计分析函数。这里还将学习读写文件的方法，并尝试函数式编程和NumPy
线性代数运算。
    本章涵盖以下内容：
     数组相关的函数；
     从文件中载入数据；
     将数组写入文件；
     简单的数学和统计分析函数。
"""


import numpy as np
import datetime


def datestr2num(s):
    """
    # 星期一 0
    # 星期二 1
    # 星期三 2
    # 星期四 3
    # 星期五 4
    # 星期六 5
    # 星期日 6
        我们将日期作为字符串传给datestr2num函数，如“28-01-2011”。这个字符串首先会按照
    指定的形式"%d-%m-%Y"转换成一个datetime对象。补充一点，这是由Python标准库提供的功能，
    与NumPy无关。随后，datetime对象被转换为date对象。最后，调用weekday方法返回一个数
    字。如同你在注释中看到的，这个数字可以是0到6的整数，0代表星期一，6代表星期天。当然，
    具体的数字并不重要，只是用作标识。
    """
    return datetime.datetime.strptime(s, "%d-%m-%Y").date().weekday()


def eg3_1():
    """
    3.1 文件读写
        首先，我们来学习使用NumPy读写文件。通常情况下，数据是以文件形式存储的。学会读写
    文件是深入学习NumPy的基础。
    """
    pass


def eg3_2():
    """
    3.2 动手实践：读写文件
        作为文件读写示例，我们创建一个单位矩阵并将其存储到文件中，并按照如下步骤完成。
    """
    # (1) 单位矩阵，即主对角线上的元素均为1，其余元素均为0的正方形矩阵。在NumPy中可以
    # 用eye函数创建一个这样的二维数组，我们只需要给定一个参数，用于指定矩阵中1的元素个数。
    # 例如，创建2×2的数组：
    i2 = np.eye(2)
    print i2
    # (2) 使用savetxt函数将数据存储到文件中，当然我们需要指定文件名以及要保存的数组。
    np.savetxt('output/eye.txt', i2)


def eg3_3():
    """
    3.3 CSV 文件
        CSV（Comma-Separated Value，逗号分隔值）格式是一种常见的文件格式。通常，数据库的
    转存文件就是CSV格式的，文件中的各个字段对应于数据库表中的列。众所周知，电子表格软件
    （如Microsoft Excel）可以处理CSV文件。
    """
    pass


def eg3_4():
    """
    3.4 动手实践：读入 CSV 文件
        我们应该如何处理CSV文件呢？幸运的是，NumPy中的loadtxt函数可以方便地读取CSV
    文件，自动切分字段，并将数据载入NumPy数组。下面，我们以载入苹果公司的历史股价数据为
    例展开叙述。股价数据存储在CSV文件中，第一列为股票代码以标识股票（苹果公司股票代码为
    AAPL），第二列为dd-mm-yyyy格式的日期，第三列为空，随后各列依次是开盘价、最高价、最低
    价和收盘价，最后一列为当日的成交量。下面为一行数据：
        AAPL,28-01-2011, ,344.17,344.4,333.53,336.1,21144800

    """

    # 从现在开始，我们只关注股票的收盘价和成交量。在上面的示例数据中，收盘价为336.1，
    # 成交量为21144800。我们将收盘价和成交量分别载入到两个数组中，如下所示：
    c, v = np.loadtxt('output/data.csv', delimiter=',', usecols=(6, 7), unpack=True)
    print c, v
    """
    可以看到，数据存储在data.csv文件中，我们设置分隔符为,（英文标点逗号），因为我们要
    处理一个CSV文件。usecols的参数为一个元组，以获取第7字段至第8字段的数据，也就是股票
    的收盘价和成交量数据。unpack参数设置为True，意思是分拆存储不同列的数据，即分别将收
    盘价和成交量的数组赋值给变量c和v。
    """


def eg3_5():
    """
    3.5 成交量加权平均价格（VWAP）
        VWAP（Volume-Weighted Average Price，成交量加权平均价格）是一个非常重要的经济学量，
    它代表着金融资产的“平均”价格。某个价格的成交量越高，该价格所占的权重就越大。VWAP
    就是以成交量为权重计算出来的加权平均值，常用于算法交易。
    """
    pass


def eg3_6():
    """
    3.6 动手实践：计算成交量加权平均价格
        我们将按如下步骤计算。
        (1) 将数据读入数组。
        (2) 计算VWAP。
    """
    c, v = np.loadtxt('output/data.csv', delimiter=',', usecols=(6, 7), unpack=True)
    vwap = np.average(c, weights=v)
    print vwap
    """
    3.6.1 算术平均值函数
        NumPy中的mean函数很友好，一点儿也不mean（该词有“尖酸刻薄”的意思）。这个函数可
    以计算数组元素的算术平均值。具体用法如下：
    """
    print "mean = ", np.mean(c)
    """
    3.6.2 时间加权平均价格
        在经济学中，TWAP（Time-Weighted Average Price，时间加权平均价格）是另一种“平均”
    价格的指标。既然我们已经计算了VWAP，那也来计算一下TWAP吧。其实TWAP只是一个变种
    而已，基本的思想就是最近的价格重要性大一些，所以我们应该对近期的价格给以较高的权重。
    最简单的方法就是用arange函数创建一个从0开始依次增长的自然数序列，自然数的个数即为收
    盘价的个数。当然，这并不一定是正确的计算TWAP的方式。事实上，本书中关于股价分析的大
    部分示例都仅仅是为了说明问题。计算TWAP的代码如下。
    """
    t = np.arange(len(c))
    print "twap =", np.average(c, weights=t)


def eg3_7():
    """
    3.7 取值范围
        通常，我们不仅仅想知道一组数据的平均值，还希望知道数据的极值以及完整的取值范
    围——最大值和最小值。我们的股价示例数据中已经包含了每天的股价范围——最高价和最低
    价。但是，我们还需要知道最高价的最大值以及最低价的最小值。不然，我们怎样才能知道自己
    的股票是赚了还是赔了呢？
    """
    pass


def eg3_8():
    """
    3.8 动手实践：找到最大值和最小值
        min函数和max函数能够满足需求。我们按如下步骤来找最大值和最小值。
    """
    # (1)首先，需要再次读入数据，将每日最高价和最低价的数据载入数组：
    h, l = np.loadtxt('output/data.csv', delimiter=',', usecols=(4, 5), unpack=True)
    print h, l
    # (2) 下方的代码即可获取价格区间
    print "highest =", np.max(h)
    print "lowest =", np.min(l)
    # (3) NumPy中有一个ptp函数可以计算数组的取值范围。该函数返回的是数组元素的最大值
    # 和最小值之间的差值。也就是说，返回值等于max(array) - min(array)。调用ptp函数：
    print "Spread high price", np.ptp(h)
    print "Spread low price", np.ptp(l)


def eg3_9():
    """
    3.9 统计分析
        股票交易者对于收盘价的预测很感兴趣。常识告诉我们，这个价格应该接近于某种均值。算
    数平均值和加权平均值都是在数值分布中寻找中心点的方法。然而，它们对于异常值（outlier）
    既不鲁棒也不敏感。举例来说，如果我们有一个高达100万美元的收盘价，这将影响到我们的计
    算结果。
    """
    pass


def eg3_10():
    """
    3.10 动手实践：简单统计分析
        我们可以用一些阈值来除去异常值，但其实有更好的方法，那就是中位数。将各个变量值按
    大小顺序排列起来，形成一个数列，居于数列中间位置的那个数即为中位数。例如，我们有1、2、
    3、4、5这5个数值，那么中位数就是中间的数字3。下面是计算中位数的步骤。
    """
    # (1) 计算收盘价的中位数。创建一个新的Python脚本文件，命名为simplestats.py。你已经知道
    # 如何从CSV文件中读取数据到数组中了，因此只需要复制一行代码并确保只获取收盘价数据即
    # 可，如下所示：
    c = np.loadtxt('output/data.csv', delimiter=',', usecols=(6,), unpack=True)
    print c
    # (2) 一个叫做median的函数将帮助我们找到中位数。我们调用它并立即打印出结果。添加下
    # 面这行代码：
    print "median =", np.median(c)
    # (3) 既然这是我们首次使用median函数，我们来检查一下结果是否正确。这可不是因为我
    # 们多疑！当然，我们可以将整个数据文件浏览一遍并人工找到正确的答案，但那样太无趣了。
    # 我们将对价格数组进行排序，并输出排序后居于中间位置的值，这也就是模拟了寻找中位数的
    # 算法。msort函数可以帮我们完成第一步。我们将调用这个函数，获得排序后的数组，并输出
    # 结果。
    sorted_close = np.msort(c)
    print "sorted =", sorted_close
    # 太好了，代码生效了！现在，我们来获取位于中间的那个数字：
    N = len(c)
    print "middle =", sorted_close[(N - 1)/2]
    """
    # 书上印刷错误，故测试当前这段代码的实现方式
    错误例子：print "middle =", sorted[(N - 1)/2] 
    正确写法：print "middle =", sorted_close[(N - 1)/2]
    tmp = [1, 2, 3, 4, 5, 6]
    print np.msort(tmp)
    print "median = ", np.median(tmp)
    print "middle = ", tmp[(len(tmp) - 1) / 2]
    """
    # (4) 咦，这个值和median函数给出的值不一样，这是怎么回事？经过仔细观察我们发现，
    # median函数返回的结果甚至根本没有在我们的数据文件里出现过。这就更奇怪了！在给NumPy
    # 团队提交bug报告之前，我们先来看下文档。原来这个谜团很容易解开。原因就在于我们的简单
    # 算法模拟只对长度为奇数的数组奏效。对于长度为偶数的数组，中位数的值应该等于中间那两个
    # 数的平均值。因此，输入如下代码：
    print "average middle =", (sorted_close[N / 2] + sorted_close[(N - 1) / 2]) / 2
    # (5) 另外一个我们关心的统计量就是方差。方差能够体现变量变化的程度。在我们的例子中，
    # 方差还可以告诉我们投资风险的大小。那些股价变动过于剧烈的股票一定会给持有者制造麻烦。
    # 在NumPy中，计算方差只需要一行代码，看下面：
    print "variance =", np.var(c)
    # (6) 既然我们不相信NumPy的函数，那就再次根据文档中方差的定义来复核一下结果。注意，
    # 这里方差的定义可能与你在统计学的书中看到的不一致，但这个定义在统计学上更为通用。
    print "variance from definition =", np.mean((c - c.mean()) ** 2)


def eg3_11():
    """
    3.11 股票收益率
        在学术文献中，收盘价的分析常常是基于股票收益率和对数收益率的。简单收益率是指相邻
    两个价格之间的变化率，而对数收益率是指所有价格取对数后两两之间的差值。我们在高中学习
    过对数的知识，“a”的对数减去“b”的对数就等于“a除以b”的对数。因此，对数收益率也可
    以用来衡量价格的变化率。注意，由于收益率是一个比值，例如我们用美元除以美元（也可以是
    其他货币单位），因此它是无量纲的。总之，投资者最感兴趣的是收益率的方差或标准差，因为
    这代表着投资风险的大小。
    """
    pass


def eg3_12():
    """
    3.12 动手实践：分析股票收益率
        按照如下步骤分析股票收益率。
    """
    # (1) 首先，我们来计算简单收益率。NumPy中的diff函数可以返回一个由相邻数组元素的差
    # 值构成的数组。这有点类似于微积分中的微分。为了计算收益率，我们还需要用差值除以前一天
    # 的价格。不过这里要注意，diff返回的数组比收盘价数组少一个元素。经过仔细考虑，我们使
    # 用如下代码：
    c = np.loadtxt('output/data.csv', delimiter=',', usecols=(6,), unpack=True)
    returns = np.diff(c) / c[: -1]
    # 注意，我们没有用收盘价数组中的最后一个值做除数。接下来，用std函数计算标准差：
    print "Standard deviation =", np.std(returns)
    # (2) 对数收益率计算起来甚至更简单一些。我们先用log函数得到每一个收盘价的对数，再
    # 对结果使用diff函数即可。
    logreturns = np.diff(np.log(c))
    print logreturns
    # 一般情况下，我们应检查输入数组以确保其不含有零和负数。否则，将得到一个错误提示。
    # 不过在我们的例子中，股价总为正值，所以可以将检查省略掉。

    # (3) 我们很可能对哪些交易日的收益率为正值非常感兴趣。在完成了前面的步骤之后，我们
    # 只需要用where函数就可以做到这一点。where函数可以根据指定的条件返回所有满足条件的数
    # 组元素的索引值。输入如下代码：
    posretindices = np.where(returns > 0)
    print "Indices with positive returns", posretindices

    # (4) 在投资学中，波动率（volatility）是对价格变动的一种度量。历史波动率可以根据历史价
    # 格数据计算得出。计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率。年波动
    # 率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根，通常交易日取252天。我
    # 们用std和mean函数来计算，代码如下所示：
    annual_volatility = np.std(logreturns) / np.mean(logreturns)
    annual_volatility = annual_volatility / np.sqrt(1. / 252.)
    print annual_volatility

    # (5) 请注意sqrt函数中的除法运算。在Python中，整数的除法和浮点数的除法运算机制不同，
    # 我们必须使用浮点数才能得到正确的结果。与计算年波动率的方法类似，计算月波动率如下：
    print "Monthly volatility", annual_volatility * np.sqrt(1. / 12.)

    """
    刚才做了些什么
        我们用计算数组相邻元素差值的diff函数计算了简单收益率，用计算数组元素自然对数的
    log函数计算了对数收益率。最后，我们计算了年波动率和月波动率。
    """


def eg3_13():
    """
    3.13 日期分析
        你是否有时候会有星期一焦虑症和星期五狂躁症？想知道股票市场是否受上述现象的影
    响？我认为这值得深入研究。

    """
    pass


def eg3_14():
    """
    3.14 动手实践：分析日期数据
        首先，我们要读入收盘价数据。随后，根据星期几来切分收盘价数据，并分别计算平均价格。
    最后，我们将找出一周中哪一天的平均收盘价最高，哪一天的最低。在我们动手之前，有一个善
    意的提醒：你可能希望利用分析结果在某一天买股票或卖股票，然而我们这里的数据量不足以做
    出可靠的决策，请先咨询专业的统计分析师再做决定！
    程序员不喜欢日期，因为处理日期总是很烦琐。NumPy是面向浮点数运算的，因此需要对日
    期做一些专门的处理。请自行尝试如下代码，单独编写脚本文件或使用本书附带的代码文件：
    dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6), unpack=True)
    执行以上代码后会得到一个错误提示：
    ValueError: invalid literal for float(): 28-01-2011
    按如下步骤处理日期。
    """
    # (1) 显然，NumPy尝试把日期转换成浮点数。我们需要做的是显式地告诉NumPy怎样来转换
    # 日期，而这需要用到loadtxt函数中的一个特定的参数。这个参数就是converters，它是一本
    # 数据列和转换函数之间进行映射的字典。

    # (2) 接下来，我们将日期转换函数挂接上去，这样就可以读入数据了。
    dates, close = np.loadtxt('output/data.csv', delimiter=',', usecols=(1, 6), converters={1: datestr2num}, unpack=True)
    print "Dates =", dates
    # 如你所见，没有出现星期六和星期天。股票交易在周末是休市的。

    # (3) 我们来创建一个包含5个元素的数组，分别代表一周的5个工作日。数组元素将初始化为0。
    averages = np.zeros(5)
    print averages
    # 这个数组将用于保存各工作日的平均收盘价。

    # (4) 我们已经知道，where函数会根据指定的条件返回所有满足条件的数组元素的索引值。
    # take函数可以按照这些索引值从数组中取出相应的元素。我们将用take函数来获取各个工作日
    # 的收盘价。在下面的循环体中，我们将遍历0到4的日期标识，或者说是遍历星期一到星期五，然
    # 后用where函数得到各工作日的索引值并存储在indices数组中。在用take函数获取这些索引值
    # 相应的元素值。最后，我们对每个工作日计算出平均值存放在averages数组中。代码如下：
    for i in range(5):
        indices = np.where(dates == i)
        prices = np.take(close, indices)
        avg = np.mean(prices)
        print "Day", i, "prices", prices, "Average", avg
        averages[i] = avg

    # (5) 如果你愿意，还可以找出哪个工作日的平均收盘价是最高的，哪个是最低的。这很容易
    # 做到，用max和min函数即可，代码如下：
    top = np.max(averages)
    print "Highest average", top
    print "Top day of the week", np.argmax(averages)
    bottom = np.min(averages)
    print "Lowest average", bottom
    print "Bottom day of the week", np.argmin(averages)


def eg3_15():
    """
    3.15 周汇总
        在之前的“动手实践”教程中，我们用的是盘后数据。也就是说，这些数据是将一整天的交
    易数据汇总得到的。如果你对棉花市场感兴趣，并且有数十年的数据，你可能希望对数据做进一
    步的汇总和压缩。开始动手吧。我们来把苹果股票数据按周进行汇总。
    """


def eg3_16():
    """
    3.16 动手实践：汇总数据
        我们将要汇总整个交易周中从周一到周五的所有数据。数据覆盖的时间段内有一个节假日：
    2月21日是总统纪念日。这天是星期一，美国股市休市，因此在我们的示例数据中没有这一天的
    数据记录。数据中的第一天为星期五，处理起来不太方便。按照如下步骤来汇总数据。
    """
    dates, close = np.loadtxt('output/data.csv', delimiter=',', usecols=(1, 6), converters={1: datestr2num},
                              unpack=True)
    # (1) 为了简单起见，我们只考虑前三周的数据，这样就避免了节假日造成的数据缺失。你可
    # 以稍后尝试对其进行拓展。
    close = close[:16]
    dates = dates[:16]
    print close
    print dates

    # (2) 首先我们来找到示例数据中的第一个星期一。回忆一下，在Python中星期一对应的编码
    # 是0，这可以作为where函数的条件。接着，我们要取出数组中的首个元素，其索引值为0。但where
    # 函数返回的结果是一个多维数组，因此要用ravel函数将其展平。
    # 找到第一个星期一
    first_monday = np.ravel(np.where(dates == 0))[0]
    print "The first Monday index is", first_monday

    # (3) 下面要做的是找到示例数据的最后一个星期五，方法和找第一个星期一类似。星期五相
    # 对应的编码是4。此外，我们用1作为索引值来定位数组的最后一个元素。
    # 找到最后一个星期五
    last_friday = np.ravel(np.where(dates == 4))[-1]
    print "The last Friday index is", last_friday
    # 接下来创建一个数组，用于存储三周内每一天的索引值。
    weeks_indices = np.arange(first_monday, last_friday + 1)
    print "Weeks indices initial", weeks_indices

    # (4) 按照每个子数组5个元素，用split函数切分数组：
    weeks_indices = np.split(weeks_indices, 3)
    print "Weeks indices after split", weeks_indices

    # (5) 在NumPy中，数组的维度也被称作轴。现在我们来熟悉一下apply_along_axis函数。
    # 这个函数会调用另外一个由我们给出的函数，作用于每一个数组元素上。目前我们的数组中有3
    # 个元素，分别对应于示例数据中的3个星期，元素中的索引值对应于示例数据中的1天。在调用
    # apply_along_axis时提供我们自定义的函数名summarize，并指定要作用的轴或维度的编号
    # （如取1）、目标数组以及可变数量的summarize函数的参数。
    weeksummary = np.apply_along_axis(summarize, 1, weeks_indices,open, high, low, close)
    print "Week summary", weeksummary


if __name__ == '__main__':
    eg3_16()
    # m = [1, 3, 8, 5]
    # print m[: -1]