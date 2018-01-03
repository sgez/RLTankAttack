import numpy as np
import matplotlib.pyplot as plt

import os, glob, md5, datetime, re, string
from pprint import pprint

path = os.getcwd()

path = path[:path.rfind('graphs')]+""
moveslist = sorted(glob.glob(path+'games/*/rlactions'), key=os.path.getmtime)

smart = list()
random = list()
for rla in moveslist:
    rl = open(rla,'r')
    rltxt = rl.read()
    print rla
    rltxt = rltxt[:rltxt.rfind('\n')]
    rl = rltxt.split('\n')
    print 'smart\t/\trandom'
    print rl.count('smart'), '\t/\t', rl.count('random')#, '\t', rl
    #print ""
    smart.append(rl.count('smart'))
    random.append(rl.count('random'))
print ' SMART: ',smart
print 'RANDOM: ',random



N = len(smart)


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

rects1 = ax.bar(ind, smart, width, color='g')

rects2 = ax.bar(ind+width, random, width, color='r')

# add some
ax.set_ylabel('Actions')
ax.set_title('Actions: Random & Smart in each game')
ax.set_xticks(ind+width)
lbls = list()
for i in range(0,N):
    lbls.append('G'+str(i+1))
ax.set_xticklabels( lbls)

ax.legend( (rects1[0], rects2[0]), ('Smart', 'Random') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.15*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
dt = datetime.date.today()
dt = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
pngfile = ".\images\RLGraphActions_"+dt+".png"
plt.savefig(pngfile, dpi=200) 
plt.show()