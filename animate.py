'''
@Author: Swapnil Bhoyar
@Date: 2021-08-21
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-21
@Title : Program to plot twitter sentiment analysis.
'''
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib import style 

# plt.style.available
style.use("seaborn")

def animate(i):
    data = pd.read_csv('data.csv')
    x1 = 7
    x2 = 8
    y1 = data['pos']
    y2 = data['neg']
    plt.cla()
    plt.bar(x1,y1,label="positive",width=0.2)
    plt.bar(x2,y2,label='negative',width=0.2)
    plt.xlabel("sentiments")
    plt.ylabel("count")
    plt.legend(loc='center')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate)

plt.tight_layout()
plt.show()