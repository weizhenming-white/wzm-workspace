#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-25 19:36
brief:学习使用Matplotlib绘图
    Matplotlib是一个非常有用的Python绘图库。它和NumPy结合得很好，但
本身是一个单独的开源项目。你可以访问http://matplotlib.sourceforge.net/
gallery.html查看美妙的示例图库。
Matplotlib中有一些功能函数可以从雅虎财经频道下载并处理数据。我们
将看到几个股价图的例子。
    本章涵盖以下内容：
     简单绘图；
     子图；
     直方图；
     定制绘图；
     三维绘图；
     等高线图；
     动画；
     对数坐标图。
"""


import numpy as np
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.pylab import date2num
import pandas_datareader.data as web
import yfinance as yf
from mpl_finance import candlestick_ochl
# from matplotlib.finance import quotes_yahoo_historical_ochl
# from matplotlib.finance import candlestick
import sys
from datetime import date, datetime
from matplotlib.pylab import date2num
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation


def eg9_1():
    """
    9.1 简单绘图
        matplotlib.pyplot包中包含了简单绘图功能。需要记住的是，随后调用的函数都会改变
    当前的绘图。最终，我们会将绘图存入文件或使用show函数显示出来。不过如果我们用的是运
    行在Qt或Wx后端的IPython，图形将会交互式地更新，而不需要等待show函数的结果。这类似于
    屏幕上输出文本的方式，可以源源不断地打印出来。
    """
    pass


def eg9_2():
    """
    9.2 动手实践：绘制多项式函数
        为了说明绘图的原理，我们来绘制多项式函数的图像。我们将使用NumPy的多项式函数poly1d来创建多项式。
    """
    # (1) 以自然数序列作为多项式的系数，使用poly1d函数创建多项式。
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    print func
    # (2) 使用NumPy的linspace函数创建x轴的数值，在-10和10之间产生30个均匀分布的值。
    x = np.linspace(-10, 10, 30)
    print x, "\n", len(x)

    # (3) 计算我们在第一步中创建的多项式的值。
    y = func(x)
    print y

    # (4) 调用plot函数，这并不会立刻显示函数图像。
    plt.plot(x, y)

    # (5) 使用xlabel函数添加x轴标签。
    plt.xlabel('x')

    # (6) 使用ylabel函数添加y轴标签。
    plt.ylabel('y(x)')

    # (7) 调用show函数显示函数图像。
    plt.show()


def eg9_3():
    """
    9.3 格式字符串
        plot函数可以接受任意个数的参数。在前面一节中，我们给了两个参数。我们还可以使用
    可选的格式字符串参数指定线条的颜色和风格，默认为b-即蓝色实线。你可以指定为其他颜色和
    风格，如红色虚线。
    """

    # （1）借用9.2里面的变量
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    x = np.linspace(-10, 10, 30)
    y = func(x)

    # （2）设置线条颜色为红色，线段类型为"--"虚线
    plt.plot(x, y, '--r')

    # （3）显示图像
    plt.show()


def eg9_4():
    """
    9.4 动手实践：绘制多项式函数及其导函数
        我们来绘制一个多项式函数，以及使用derive函数和参数m为1得到的其一阶导函数。我们
    已经在之前的“动手实践”教程中完成了第一部分。我们希望用两种不同风格的曲线来区分两条
    函数曲线。

    """
    # (1) 创建多项式函数及其导函数。
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    func1 = func.deriv(m=1)
    x = np.linspace(-10, 10, 30)
    y = func(x)
    y1 = func1(x)

    # (2)以两种不同风格绘制多项式函数及其导函数：红色圆形和绿色虚线。你可能无法在本书
    # 的印刷版中看到彩色图像，因此只能自行尝试绘制图像。
    plt.plot(x, y, 'ro', x, y1, 'g--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def eg9_5():
    """
    9.5 子图
        绘图时可能会遇到图中有太多曲线的情况，而你希望分组绘制它们。这可以使用subplot
    函数完成。
    """
    pass


def eg9_6():
    """
    9.6 动手实践：绘制多项式函数及其导函数
        我们来绘制一个多项式函数及其一阶和二阶导函数。为了使绘图更加清晰，我们将绘制3张
    子图。
    """
    # (1)创建多项式函数及其导函数。
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    x = np.linspace(-10, 10, 30)
    y = func(x)
    # 创建一阶导函数
    func1 = func.deriv(m=1)
    y1 = func1(x)
    # 创建二阶导函数
    func2 = func.deriv(m=2)
    y2 = func2(x)

    # (2) 使用subplot函数创建第一个子图。该函数的第一个参数是子图的行数，第二个参数
    # 是子图的列数，第三个参数是一个从1开始的序号。另一种方式是将这3个参数结合成一个数
    # 字，如311。这样，子图将被组织成3行1列。设置子图的标题为Polynomial，使用红色实线
    # 绘制。
    plt.subplot(311)
    plt.plot(x, y, 'r-')
    plt.title("Polynomial")

    # (3) 使用subplot函数创建第二个子图。设置子图的标题为First Derivative，使用蓝色
    # 三角形绘制。
    plt.subplot(312)
    plt.plot(x, y1, 'b^')
    plt.title("First Derivative")

    # (4) 使用subplot函数创建第三个子图。设置子图的标题为Second Derivative，使用绿
    # 色圆形绘制。
    plt.subplot(313)
    plt.plot(x, y2, 'go')
    plt.title("Second Derivative")
    # 设置x轴标签和y轴标签，并显示图像
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def eg9_7():
    """
    9.7 财经
        Matplotlib可以帮助我们监控股票投资。使用matplotlib.finance包中的函数可以从雅虎
    财经频道（http://finance.yahoo.com/）下载股价数据，并绘制成K线图（candlestick）。
    """
    pass


def eg9_8():
    """
    9.8 动手实践：绘制全年股票价格
        我们可以使用matplotlib.finance包绘制全年的股票价格。获取数据源需要连接到雅虎
    财经频道。

    """
    # (1)将当前的日期减去1年作为起始日期。
    """
    from matplotlib.dates import DateFormatter
    from matplotlib.dates import DayLocator
    from matplotlib.dates import MonthLocator
    from matplotlib.finance import quotes_historical_yahoo
    from matplotlib.finance import candlestick
    import sys
    from datetime import date
    import matplotlib.pyplot as plt
    # 将这些库添加到开头
    """
    today = date.today()
    start = date(today.year - 1, today.month, today.day)
    print start, today

    # (2) 我们需要创建所谓的定位器（locator），这些来自matplotlib.dates包中的对象可以在
    # x轴上定位月份和日期。
    alldays = DayLocator()
    months = MonthLocator()
    # print alldays, months

    # (3) 创建一个日期格式化器（date formatter）以格式化x轴上的日期。该格式化器将创建一个
    # 字符串，包含简写的月份和年份。
    month_formatter = DateFormatter("%b %Y")
    # print month_formatter

    # (4) 从雅虎财经频道下载股价数据。
    apple = web.get_data_yahoo('AAPL', start, today)
    apple.head()
    # 修改apple的值，从【High Low Open Close Volume Adj_Close】变为【Open Close High Low Adj_Close】
    del apple['Volume']  # 永久删除'Volume'
    # 移动"Open"和"Close"到第一列和第二列
    cols = list(apple)
    cols.insert(0, cols.pop(cols.index('Open')))
    cols.insert(1, cols.pop(cols.index('Close')))
    apple = apple.ix[:, cols]
    print apple
    # 保存pandas DataFrame数据为csv
    apple.to_csv('output/AAPL.csv')
    # 1、读取行情数据文件
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)  # header=0表示第一行为列名
    print df_stock

    print df_stock.shape[0]
    # 2、构造传入数据的数据结构quotes
    # 画k线图需传的参数，包括(交易日时间戳，开盘价，收盘价，最高价，最低价)
    quotes = []
    # 构造要画k线图的数据结构，获取第一个日期时刻(20200424)，将其转为数字值，后面每个日期-1
    date_plt = 0
    date_num = 0
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            print df_stock.ix[[i]].values[0][0]
            print date_num
            date_plt = date_num
        else:
            print df_stock.ix[[i]].values[0][0]
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        print(df_stock.ix[[i]].values[0])       # 打印每行数据 ['000001-SZE' '2020-04-24' 13.17 13.28 13.11 13.24 56600161 747473770.46 nan]
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列  df_stock.iloc[i]['开盘价']，用这个似乎输出了的列对不上，输出成了下一列值(最高价)
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        print(datas)                             # (737539.0, 13.17, 13.24, 13.28, 13.11)
        quotes.append(datas)

    # (5) 创建一个Matplotlib的figure对象——这是绘图组件的顶层容器。
    fig = plt.figure()

    # (6) 增加一个子图。
    ax = fig.add_subplot(111)

    # (7) 将x轴上的主定位器设置为月定位器。该定位器负责x轴上较粗的刻度。
    ax.xaxis.set_major_locator(months)

    # (8) 将x轴上的次定位器设置为日定位器。该定位器负责x轴上较细的刻度。
    ax.xaxis.set_minor_locator(alldays)

    # (9) 将x轴上的主格式化器设置为月格式化器。该格式化器负责x轴上较粗刻度的标签。
    ax.xaxis.set_major_formatter(month_formatter)

    # (10) matplotlib.finance包中的一个函数可以绘制K线图。这样，我们就可以使用获取的
    # 股价数据来绘制K线图。我们可以指定K线图的矩形宽度，现在先使用默认值。

    candlestick_ochl(ax, quotes)

    # (11) 将x轴上的标签格式化为日期。为了更好地适应x轴的长度，标签将被旋转。
    fig.autofmt_xdate()
    plt.show()


def eg9_9():
    """
    9.9 直方图
        直方图（histogram）可以将数据的分布可视化。Matplotlib中有便捷的hist函数可以绘制直
    方图。该函数的参数中有这样两项——包含数据的数组以及柱形的数量。
    """
    pass


def eg9_10():
    """
    9.10 动手实践：绘制股价分布直方图
        我们来绘制从雅虎财经频道下载的股价数据的分布直方图。
    """
    # (1) 下载一年以来的数据：
    today = date.today()
    start = date(today.year - 1, today.month, today.day)

    # (2) 上一步得到的股价数据存储在Python列表中。将其转化为NumPy数组并提取出收盘价数据：
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)
    quotes = []
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            date_plt = date_num
        else:
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        quotes.append(datas)
    quotes = np.array(quotes)
    close = quotes.T[4]
    print close

    # (3) 指定合理数量的柱形，绘制分布直方图：
    print len(close)
    print np.sqrt(len(close))
    plt.hist(close, int(np.sqrt(len(close))))    # 返回len(close)的平方根，保留为整数
    plt.show()


def eg9_11():
    """
    9.11 对数坐标图
        当数据的变化范围很大时，对数坐标图（logarithmic plot）很有用。Matplotlib中有semilogx
    函数（对x轴取对数）、semilogy函数（对y轴取对数）和loglog函数（同时对x轴和y轴取
    对数）。
    """
    pass


def eg9_12():
    """
    9.12 动手实践：绘制股票成交量
        股票成交量变化很大，因此我们需要对其取对数后再绘制。首先，我们需要从雅虎财经
    频道下载历史数据，从中提取出日期和成交量数据，创建定位器和日期格式化器，创建图像
    并以子图的方式添加。在前面的“动手实践”教程中我们已经完成过这些步骤，因此这里不
    再赘述。
    """
    # (1) 加载苹果的股票数据
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)
    quotes = []
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            date_plt = date_num
        else:
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        quotes.append(datas)
    quotes = np.array(quotes)
    dates = quotes.T[0]
    volume = quotes.T[4]
    alldays = DayLocator()
    months = MonthLocator()
    month_formatter = DateFormatter("%b %Y")

    # (2) 使用对数坐标绘制成交量数据。
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.semilogy(dates, volume)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(month_formatter)
    fig.autofmt_xdate()
    plt.show()


def eg9_13():
    """
    9.13 散点图
        散点图（scatter plot）用于绘制同一数据集中的两种数值变量。Matplotlib的scatter函数可
    以创建散点图。我们可以指定数据点的颜色和大小，以及图像的alpha透明度。
    """
    pass


def eg9_14():
    """
    9.14 动手实践：绘制股票收益率和成交量变化的散点图
        我们可以便捷地绘制股票收益率和成交量变化的散点图。同样，我们先从雅虎财经频道下载
    所需的数据。
    """
    # (1) 加载苹果的股票信息，并转化成numpy
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)
    quotes = []
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            date_plt = date_num
        else:
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        quotes.append(datas)
    quotes = np.array(quotes)

    # (2) 提取出收盘价和成交量数据。
    close = quotes.T[2]
    volume = quotes.T[4]

    # (3) 计算股票收益率和成交量的变化值。
    ret = np.diff(close) / close[:-1]
    volchange = np.diff(volume) / volume[:-1]

    # (4) 创建一个Matplotlib的figure对象。
    fig = plt.figure()

    # (5) 在图像中添加一个子图。
    ax = fig.add_subplot(111)

    # (6) 创建散点图，并使得数据点的颜色与股票收益率相关联，数据点的大小与成交量的变化
    # 相关联。
    ax.scatter(ret, volchange, c=ret * 100, s=volchange * 100, alpha=0.5)

    # (7) 设置图像的标题并添加网格线。
    ax.set_title('Close and volume returns')
    ax.grid(True)
    plt.show()


def eg9_15():
    """
    9.15 着色
        fill_between函数使用指定的颜色填充图像中的区域。我们也可以选择alpha通道的取值。
    该函数的where参数可以指定着色的条件。
    """
    pass


def eg9_16():
    """
    9.16 动手实践：根据条件进行着色
        假设你想对股票曲线图进行着色，并将低于均值和高于均值的收盘价填充为不同颜色。
    fill_between函数是完成这项工作的最佳选择。我们仍将省略下载一年以来历史数据、提取日
    期和收盘价数据以及创建定位器和日期格式化器的步骤。
    """
    # (1) 加载苹果的股票信息，并转化成numpy
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)
    quotes = []
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            date_plt = date_num
        else:
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        quotes.append(datas)
    quotes = np.array(quotes)
    dates = quotes.T[0]
    close = quotes.T[2]
    alldays = DayLocator()
    months = MonthLocator()
    month_formatter = DateFormatter("%b %Y")

    # (2) 创建一个Matplotlib的figure对象。
    fig = plt.figure()

    # (3) 在图像中添加一个子图。
    ax = fig.add_subplot(111)

    # (4) 绘制收盘价数据。
    ax.plot(dates, close)

    # (5) 对收盘价下方的区域进行着色，依据低于或高于平均收盘价使用不同的颜色填充。
    plt.fill_between(dates, close.min(), close, where=close > close.mean(), facecolor="green", alpha=0.4)
    plt.fill_between(dates, close.min(), close, where=close < close.mean(), facecolor="red", alpha=0.4)

    #  (6) 现在，我们将设置定位器并将x轴格式化为日期，从而完成绘制。
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(month_formatter)
    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()


def eg9_17():
    """
    9.17 图例和注释
        对于高质量的绘图，图例和注释是至关重要的。我们可以用legend函数创建透明的图例，
    并由Matplotlib自动确定其摆放位置。同时，我们可以用annotate函数在图像上精确地添加注释，
    并有很多可选的注释和箭头风格
    """
    pass


def eg9_18():
    """
    9.18 动手实践：使用图例和注释
        在第3章中我们学习了如何计算股价的指数移动平均线。我们将绘制一只股票的收盘价和对
    应的三条指数移动平均线。为了清楚地描述图像的含义，我们将添加一个图例，并用注释标明两
    条平均曲线的交点。部分重复的步骤将被略去。
    """
    # 加载苹果的股票信息，并转化成numpy
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)
    quotes = []
    for i in range(df_stock.shape[0]):  # 遍历每行，shape为dataframe大小(x,y)，表示x行y列
        if i == 0:
            # 将交易日期日期转为数字
            date_num = date2num(datetime.strptime(df_stock.ix[[i]].values[0][0], '%Y-%m-%d'))  # 1表示第一列，为交易日
            date_plt = date_num
        else:
            date_plt = date_num + i  # 由于csv文件中日期为升序排序，这里为加号
        open = df_stock.ix[[i]].values[0][1]  # 开盘价： i行第2列
        close = df_stock.ix[[i]].values[0][2]  # 收盘价：i行第3列
        high = df_stock.ix[[i]].values[0][3]  # 最高价：i行第4列
        low = df_stock.ix[[i]].values[0][4]  # 最低价：i行第5列
        datas = (date_plt, open, close, high, low)
        quotes.append(datas)
    quotes = np.array(quotes)
    dates = quotes.T[0]
    close = quotes.T[2]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # (1) 计算并绘制指数移动平均线：如果需要，请回到第3章中复习一下指数移动平均线的计算
    # 方法。分别使用9、12和15作为周期数计算和绘制指数移动平均线。
    emas = []
    for i in range(9, 18, 3):
        weights = np.exp(np.linspace(-1., 0., i))
        weights /= weights.sum()
        ema = np.convolve(weights, close)[i - 1:-i + 1]
        idx = (i - 6) / 3
        ax.plot(dates[i - 1:], ema, lw=idx, label="EMA(%s)" % (i))
        data = np.column_stack((dates[i - 1:], ema))
        emas.append(np.rec.fromrecords(data, names=["dates", "ema"]))

    # (2) 我们来找到两条指数移动平均曲线的交点。
    first = emas[0]["ema"].flatten()
    second = emas[1]["ema"].flatten()
    bools = np.abs(first[-len(second):] - second) / second < 0.0001
    xpoints = np.compress(bools, emas[1])

    # (3) 我们将找到的交点用注释和箭头标注出来，并确保注释文本在交点的不远处。
    for xpoint in xpoints:
        ax.annotate('x', xy=xpoint, textcoords='offset points',
                    xytext=(-50, 30),
                    arrowprops=dict(arrowstyle="->"))

    # (4) 添加一个图例并由Matplotlib自动确定其摆放位置。
    leg = ax.legend(loc='best', fancybox=True)

    # (5) 设置alpha通道值，将图例透明化。
    leg.get_frame().set_alpha(0.5)

    # (6) 显示图像
    alldays = DayLocator()
    months = MonthLocator()
    month_formatter = DateFormatter("%b %Y")
    ax.plot(dates, close, lw=1.0, label="Close")
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(month_formatter)
    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()


def eg9_19():
    """
    9.19 三维绘图
        三维绘图非常壮观华丽，因此我们必须涵盖这部分内容。对于3D作图，我们需要一个和三
    维投影相关的Axes3D对象。
    """
    pass


def eg9_20():
    """
    9.20 动手实践：在三维空间中绘图
        我们将在三维空间中绘制一个简单的三维函数。
            z = x² + y²
    """
    # (1) 我们需要使用3d关键字来指定图像的三维投影。
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # (2) 我们将使用meshgrid函数创建一个二维的坐标网格。这将用于变量x和y的赋值。
    u = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(u, u)
    z = x ** 2 + y ** 2

    # (3) 我们将指定行和列的步幅，以及绘制曲面所用的色彩表（color map）。步幅决定曲面上“瓦
    # 片”的大小，而色彩表的选择取决于个人喜好。
    ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r)
    plt.show()


def eg9_21():
    """
    9.21 等高线图
        Matplotlib中的等高线3D绘图有两种风格——填充的和非填充的。我们可以使用contour函
    数创建一般的等高线图。对于色彩填充的等高线图，可以使用contourf绘制。
    """
    pass


def eg9_22():
    """
    9.22 动手实践：绘制色彩填充的等高线图
        我们将对前面“动手实践”中的三维数学函数绘制色彩填充的等高线图。代码也非常简单，
    一个重要的区别是我们不再需要指定三维投影的参数。使用下面这行代码绘制等高线图：
                ax.contourf(x, y, z)
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(u, u)
    z = x ** 2 + y ** 2
    ax.contourf(x, y, z)
    plt.show()


def eg9_23():
    """
    9.23 动画
        Matplotlib提供酷炫的动画功能。Matplotlib中有专门的动画模块。我们需要定义一个回调函
    数，用于定期更新屏幕上的内容。我们还需要一个函数来生成图中的数据点。
    """
    pass


def eg9_24():
    """
    9.24 动手实践：制作动画
        我们将绘制三个随机生成的数据集，分别用圆形、小圆点和三角形来显示。不过，我们将只
    用随机值更新其中的两个数据集。
    """
    # (1) 我们将用不同颜色的圆形、小圆点和三角形来绘制三个数据集中的数据点。
    N = 10
    x = np.random.rand(N)
    y = np.random.rand(N)
    z = np.random.rand(N)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    circles, triangles, dots = ax.plot(x, 'ro', y, 'g^', z, 'b.')

    # (2) 下面的函数将被定期调用以更新屏幕上的内容。我们将随机更新两个数据集中的y坐
    # 标值。
    def update(data):
        circles.set_ydata(data[0])
        triangles.set_ydata(data[1])
        return circles, triangles

    # (3) 使用NumPy生成随机数。
    def generate():
        while True:
            yield np.random.rand(2, N)

    # 生成动画
    anim = animation.FuncAnimation(fig, update, generate, interval=150)
    plt.show()


def eg9_25():
    """
    9.25 本章小结
        本章围绕Matplotlib——一个Python绘图库展开，涵盖简单绘图、直方图、定制绘图、子图、
    3D绘图、等高线图和对数坐标图等内容。我们还学习了几个绘制股票数据的例子。显然，我们
    还只是领略了冰山一角。Matplotlib的功能非常丰富，因此我们没有足够的篇幅来讲述LaTex支持、
    极坐标支持以及其他功能。
        Matplotlib的作者John Hunter于2012年8月离开了我们。本书的审稿人之一建议在此提及John
    Hunter纪念基金（John Hunter Memorial Fund，请访问http://numfocus.org/johnhunter/）。该基金由
    NumFocus Foundation发起，可以这么说，它给了我们这些John Hunter作品的粉丝们一个回报的机
    会。更多详情，请访问前面的NumFocus网站链接
    """
    pass


if __name__ == '__main__':
    eg9_24()