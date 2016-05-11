import pandas as pd
import matplotlib.pyplot as plt
def convert_time(t):
    #t = "1:12:23"
    (h, m, s) = t.split(':')
    result = int(h) * 3600 + int(m) * 60 + int(s)
    return  result

data = pd.read_csv("data.csv")
plotviews= data.Views.plot(kind='bar', figsize=(17, 6), width = .9, color = '#278DBC', edgecolor= 'none', grid = False, clip_on=False)


#for location in ['right', 'left', 'top', 'bottom']:
#    plotvisitors.spines[location].set_visible(False)

Y= data['util']
X= data['time_stamp']
Z= [convert_time(x) for x in data['time_stamp'] ]
plt.plot(Z,Y)
plt.show()