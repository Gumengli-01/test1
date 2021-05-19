# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:43:50 2021

@author: GML
"""

import matplotlib.pyplot as plt #调用matplotlib库
import numpy as np
x=np.linspace(0,3*np.pi,100) #0代表初始值，3*np.pi代表最后的值
y=np.sin(x) #代表正弦波

plt.rcParams['font.sans-serif']=['SimHei']#加上这句可以在图表中显示中文
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
plt.subplot(1,2,1)        #subplot(a,b,c) a:列，b:行, c:图像序列 这里表示 显示2行1 列的图像中的第一个
plt.title(r'$f(x)=sin(x)$')#显示标题
plt.plot(x,y)#x表示x轴的数据，y表示y轴的数据
plt.show()#显示图表

x1=[t*0.375*np.pi for t in x]
y1=np.sin(x1)
plt.subplot(1,2,2)
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8}\pi$')
plt.plot(x,y1)
plt.show()