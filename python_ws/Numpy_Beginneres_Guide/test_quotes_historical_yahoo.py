#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-27 14:53
brief:股票OHLC历史数据爬取——Yahoo
    OHLC 指 open，high，low，close，老外的网站数据规范，相比从国内的网站获取股票、
场内基金的数据，yahoo更可靠，JSON的数据结构也使得获取数据更方便、准确。

Yahoo API
    过去python的pandas中直接提供了yahoo、google等数据的接口，pandas.io.data，
在《Python金融大数据分析》中有详细介绍，现在该接口已经移除，网上也有一些第三方的API，但也已经很久没有维护，失效了。

如果数据量不大，对频率要求不高，可以考虑直接从Yahoo网页直接提取数据。

API 接口
https://finance.yahoo.com/quote/510300.SS/history?period1=1511924498&period2=1543460498&interval=1d&filter=history&frequency=1d

510300.SS：股票代码
1511924498：起始日时间戳
1543460498：截止日时间戳
1d：频率，日
"""
import pandas_datareader.data as web
import pandas as pd
import datetime
import yfinance as yf
# import fix_yahoo_finance as yf


def quotes_yahoo_historical_ochl():
    # data = web.get_data_yahoo('AAPL', start='2019-01-01', end='2020-01-01')
    # data.head()
    # print data

    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.today()
    print start, end
    apple = web.get_data_yahoo('AAPL', start, end)
    apple.head()
    print apple

    # 删除第二行
    # apple.drop(1)
    # print apple

    # 打印第一个值，以便验证
    # print apple.iloc[0, 0]

    # 删除“Volume”列
    # apple.drop(['Volume'], axis=1)   # 临时删除
    del apple['Volume']     # 永久删除
    print apple

    # 移动列
    # get a list of columns
    cols = list(apple)
    for i in cols:
        print i
    # move the column to head of list using index, pop and insert
    cols.insert(0, cols.pop(cols.index('Open')))
    cols.insert(1, cols.pop(cols.index('Close')))
    apple = apple.ix[:, cols]
    print cols
    print apple
    apple.to_csv('output/AAPL.csv')

    # quotes=quotes,  # 传入的数据，形式：(time, open, close, high, low, ...)


def analysis_panda_data():
    # 1、读取行情数据文件
    df_stock = pd.read_csv('output/AAPL.csv', header=0, index_col=None)  # header=0表示第一行为列名
    print df_stock
    # 重置列索引（不然以第一列"证券代码"为列索引，经测试发现会导致读取的列对不上号）
    # df_stock = df_stock.reset_index(drop=False)  # drop=False表示不删除以前的索引，这里以前的索引为读取的第一列(即证券代码)


if __name__ == '__main__':
    quotes_yahoo_historical_ochl()
    analysis_panda_data()