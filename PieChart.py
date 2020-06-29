#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:25:54 2020

@author: yeoboonhong
"""
import pandas as pd
import matplotlib.pyplot as matplot

data = pd.read_excel("artificial_data.xlsx")
data.columns

##### Pandas libraries #####
data_bar_figure = data.groupby(['group']).sum().plot(kind='pie', y='value (booking)', shadow = True, startangle=90, figsize=(10,10), autopct='%1.1f%%')
data_figure = data_bar_figure.get_figure().savefig('pie_pandas.png')


##### Matplotlib library #####

mat_fig, mat_ax = matplot.subplots()
data_processed = data.groupby(['group'], as_index=False).sum()
labels = data_processed['group'].to_list()
values = data_processed["value (booking)"].to_list()

matplot.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
mat_ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
mat_ax.legend(labels, loc="upper right",  bbox_to_anchor=(1, 0, 0, 1))
#matplot.show()

matplot.ylabel("value (booking)")

matplot.savefig('pie_matplotlib.png')
