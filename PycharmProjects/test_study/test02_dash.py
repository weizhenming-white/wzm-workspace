#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-02-03 16:13
brief:练习dash可视化
"""
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()
server = app.server
# 数据载入
df = pd.read_csv('https://raw.githubusercontent.com/ffzs/dataset/master/insurance.csv')
# app的layout
app.layout = html.Div([
    html.Div([
        html.Label('Gender'),
        html.Div([
            dcc.Dropdown(   # 功能性组件， 设定id值作为标签关联callback函数中的标签
                id='gender',
                options=[{'label': i, 'value': i} for i in ['female', 'male']],
                value='female'),
        ]),
        html.Label('Color'),
        html.Div([
            dcc.Dropdown(
                id='color',
                options=[{'label': i, 'value': i} for i in ['region', 'smoker', 'children']],
                value='region'),
        ]),
    ], className="three columns"),  # 直接加入css的功能
    html.Div([
        dcc.Graph(id='scatter')    # 关联graph
    ], className="eight columns")
], className="page")

# 对callback函数进行设置， 与上面的对应， 将数据return回对应id的Graph
@app.callback(
    dash.dependencies.Output('scatter', 'figure'),
    [dash.dependencies.Input('gender','value'),
     dash.dependencies.Input('color','value')]
)
def update_scatter(value_gender, value_color):
    grouped = df.groupby('sex')  # 以性别分组
    data = grouped.get_group(value_gender)  # 获取选取的性别为变量
    # color_col = value_color   # 获取颜色分类的属性
    color_class = pd.Categorical(data[value_color])   # 将颜色分类数据明确化
#     c = [Spectral8[i] for i in color_class.codes]   # 获取颜色列表
    s = [(np.sqrt(i)+2) for i in data['age']]   # 将年龄数据开方用大小表示用以区别年龄大小
    trace = go.Scatter(
                x=data["bmi"],
                y=data["charges"],
                mode='markers',
                marker=dict(
                    size=s,
                    sizemode='diameter',
                    sizeref=0,
                    color=color_class.codes,
                    colorscale='Earth'
                ))

    layout = go.Layout(margin=dict(l=20, r=20, t=0, b=30))
    fig = go.Figure(data=[trace], layout=layout)
    return fig

# css的设置
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://codepen.io/ffzs/pen/mjjXGM.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)  # 运行app 设置host 默认是localhost
