#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:01:00 2020

@author: alex yeo
"""
import pandas as pd
import matplotlib.pyplot as plt
import random


data = pd.read_excel("artificial_data.xlsx")
data.columns


##### Pandas multi line chart #####
data_visual = data.pivot(index='index (day)', columns='group', values='value (booking)')
data_visual.plot(figsize=(10, 10), fontsize=12).get_figure().savefig('line_pandas.png')




###### Matplotlib multi line chart #####
index_info = data["index (day)"]

x_min = index_info.min()
x_max = index_info.max()


xy_content_dict = {}
x_index = [val for val in range(x_min, x_max+1, 1)]
xy_content_dict["index (day)"] = x_index


group_labels = data.groupby(['group'], as_index=False).mean()
    
    
for index, content in group_labels.iterrows():
    group_info = content["group"]
        
    condition = data["group"] == group_info
    xy_content = data[condition]
    
    key_content = group_info
    booking_list = []
    
    for xy_index, xy_content in xy_content.iterrows():
        x_value = xy_content["index (day)"]
        y_value = xy_content["value (booking)"]
        booking_list.append(y_value)
    xy_content_dict[key_content] = booking_list
    
colour_num = 0 
skip_index = 0 
for index, content in xy_content_dict.items():
    if index != "index (day)":
        skip_index += 1
        
        if skip_index % 1 != 0:
            continue
        colour_num += 1
        
        plt.plot(xy_content_dict['index (day)'], content, marker='', color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)), linewidth=1, alpha=0.9, label=index)

plt.legend(loc=2, ncol=1, prop={'size': 8}, title="group")
 
# Add titles
plt.xlabel("index (day)")
plt.ylabel("value (booking)")
#plt.show()
plt.savefig('line_matplotlib.png', dpi=216)
 

