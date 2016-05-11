import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import random


#sns.set_style("whitegrid")
#data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
#sns.boxplot(data=data);
#print data
sns.set_style("dark")
#sinplot()
#plt.tight_layout()
#plt.set_tight_layout(True)
#plt.plot([0,0],[0,5], 'k-', lw=2)
for x in range(0,40):
    y1 = random.randint(1,5)
    duration =  random.randint(1, 10)
    y2 = y1+duration
    plt.hlines(x,y1,y2)
#plt.hlines(5,0,2)
#plt.hlines(5.1,1,3)
#plt.hlines(5.2,1,4)

plt.show()