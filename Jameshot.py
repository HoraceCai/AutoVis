
import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os


x1 = []
y1 = []
x2 = []
y2 = []


with open('KingJames.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if int(row[20]) == 1:
            x1.append(int(row[17]))
            y1.append(int(row[18]))
        else:
            x2.append(int(row[17]))
            y2.append(int(row[18]))


#plt.scatter(x1, y1)
#plt.hist2d(x,y)
plt.scatter(x1, y1, marker='o', color='red', s=40)
#                   记号形状       颜色           点的大小    设置标签
plt.scatter(x2, y2, marker='x', color='red', s=40)

plt.legend(loc='best')    # 设置 图例所在的位置 使用推荐位置
plt.show()
