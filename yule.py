import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math
import os
from matplotlib.font_manager import FontManager, FontProperties
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

plt.rcParams['figure.dpi'] = 300 #分辨率
with np.errstate(divide='ignore'):
    np.float64(1.0) / 0.0
filelist=[]
for name in os.listdir('归档/全部/'):
     filelist.append(name)
print(filelist)
for name in filelist:
    try:
        file=pd.read_csv('归档/全部/'+name,names=['R','F'],encoding='utf8')
        #file=pd.read_csv('six/vowel.csv',names=['R','F'],encoding='utf8')
        #file2 = pd.read_csv('six/'+filename, names=['R', 'F'])
        #print(file)
        f=list(file['R'])
        r=list(file['F'])
        def func(r, a, b, c):
            #return a * np.power(c, r) / np.power(r, b)  # yule
            #return  a/ np.power(r,b)#zipf
            #return a * np.power(10, -b * r)#指数
            return a*np.power(b,r-1)#sigurd
        x=(np.array(r))
        y=(np.array(f))
        xdata = x
        ydata = y
        popt, pcov = curve_fit(func, x, y)
        print(popt)
        print('参数a='+str(popt[0]))
        print('参数b='+str(popt[1]))
        #print('参数c='+str(popt[2]))
        plt.plot(xdata, y, 'b-', label='data',linestyle=":")
        plt.plot(xdata, (func(xdata, *popt)), 'r-',label='fitting' ,alpha=0.5)
        plt.legend(bbox_to_anchor=(1.1,1.15))
        newx=[]
        newy1=[]
        newy2=[]
        for i in xdata:
            newx.append(math.log(i))
        for i in ydata:
            newy1.append(math.log(i))
        for i in func(xdata, *popt):
            newy2.append(math.log(i))
        #plt.plot(xdata, newy1, 'green', label='log_data',linestyle=":")
        #plt.plot(xdata, newy2, 'black',label='log_fit')
        #print(func(xdata, *popt))
        #plt.savefig('+y_log.jpg')
        def cal_rr(y0,y):
            sstot=0
            ave=np.mean(y)
            for i in y:
                sstot=sstot+(i-ave)**2
            ssreg=0
            for i in y0:
                ssreg=ssreg+(i-ave)**2
            ssres=0
            for i in range(len(y0)):
                ssres=ssres+(y[i]-y0[i])**2
            r2=1-ssres/sstot
            return r2
        print('拟合度指标R^2='+str(cal_rr(func(xdata, *popt),ydata)))
        plt.title('sigurd拟合度指标R^2='+str(cal_rr(func(xdata, *popt),ydata)),fontproperties=getChineseFont())
        plt.xlabel('全部匹配对', fontproperties=getChineseFont())
        plt.ylabel('数量', fontproperties=getChineseFont())
        plt.legend()
        #plt.show()
        plt.savefig('图像/全部/'+name[:-4]+'.png')
        plt.close()
    except:
        print(name+'xxx')

