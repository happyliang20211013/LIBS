import numpy as np
import csv
import scipy.signal as sg
import matplotlib.pyplot as plt

#120种原料的峰值寻找

#-------------------------------------------
#读入数据
#-------------------------------------------
x = list()
x2 = list()
yyy = list() #存放第一列数据

with open('x.csv','r',encoding='utf-8-sig') as f:  #读入x，取整，为了寻找峰值
    reader=csv.reader(f)
    for row in reader:
        x.append(int(row[0]))
x=np.array(x)

'''
with open('x2.csv','r',encoding='utf-8-sig') as f: #读入X，是原值，浮点数，为了画峰值图，但最后没有找到循环画图的方法，这节可以省略
    reader=csv.reader(f)
    for row in reader:
        x2.append(float(row[0]))
'''

with open('yyy.csv','r',encoding='utf-8-sig') as f: #读入y，即不同波数下的吸光度，csv文件中，每一行代表一种原料
    reader=csv.reader(f)
    for row in reader:
        yyy.append(row)

#-------------------------------------------
#寻找峰值
#-------------------------------------------
peak_x=list()
peak_y=list()
for i in range(0,len(yyy)):
    peak_id,peak_property = sg.find_peaks(yyy[i], height=0, distance=1, prominence=185)
    #print(peak_id,peak_property)
    peak_freq = x[peak_id]
    peak_height = peak_property['peak_heights'] #peak_freq,peak_height是数组
    #print('peak_freq',peak_freq)
    #print('peak_height',peak_height)
    #c=yyy[i]
    #plt.plot(x2, c, marker='o')
    #c.clear()
    #a=peak_freq
    #b=peak_height
    #plt.plot(a, b, "x")
    #a.clear()
    #b.clear()
    #plt.show() #作图我现在程序跑不出来，能跑出来的话，这也可以作为一部分说明
    peak_x.append(peak_freq.tolist())
    peak_y.append(peak_height.tolist()) #这两步输出的是嵌套列表了，好像更麻烦。另外并不一定所有的原料都是distance=200都可以找到峰，是不是应该做一个python的图，表示一下结果的准确性，在分析的时候可以写

#-------------------------------------------
#导出数据
#-------------------------------------------
#print(peak_x,peak_y)
output=csv.writer(open('peaks-.csv','a+',newline=''),dialect='excel')
output.writerows(map(lambda x:[x],peak_x)) #这样写在一列里了，怎么写成多列：用excel分列

#for i in range(0,len(peak_x)):
