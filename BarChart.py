#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:41:11 2020

@author: yeoboonhong
"""
import pandas as pd
import matplotlib.pyplot as matplot
import numpy as np

data = pd.read_excel("artificial_data.xlsx")
data.columns



# 3 lines bar chart 
#data_bar_plot = data_visual.plot(kind='bar', figsize=(10, 10), fontsize=12)
#data_bar_figure = data_bar_plot.get_figure()
#data_bar_figure.savefig('stacked_bar_pandas.pdf')

# single line bar chart 
data_visual = data.pivot(index='index (day)', columns='group', values='value (booking)')
data_figure = data_visual.plot(kind='bar', stacked=True, figsize=(10, 10), fontsize=12).get_figure().savefig('stacked_bar_pandas.png')

#fig, ax = matplot.subplots(figsize=(10,7))  


colors = ["#006D2C", "#31A384","#74C476"]

group_info =  data.groupby(['group'], as_index=False).mean()['group']

width = 0.35

legends = []
headers = []

for index, group in enumerate(group_info):
    
    x_values = list(data[data['group'] == group].loc[:, 'index (day)'])
    y_values = list(data[data['group'] == group].loc[:, 'value (booking)'])
    print(index, group, y_values)
    
    
    if index == 0:
        margin_bottom = np.zeros(len(x_values))


    p = matplot.bar(x_values, y_values, width, bottom = margin_bottom, color=colors[index])
    
    headers.append(group)
    legends.append(p[0])
    
    margin_bottom += y_values
    
matplot.ylabel('value (booking)')
matplot.xlabel('index (day)')
matplot.legend(legends, headers, loc=2, title="group")


matplot.savefig('stacked_bar_matplotlib.png', dpi=216)







