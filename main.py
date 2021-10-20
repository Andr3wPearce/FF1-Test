import fastf1 as ff1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ff1.Cache.enable_cache("cache/")
season = []
for i in range(1,17):
  season.append(ff1.get_session(2021,i,"R"))
  #season[i-1]=season[i-1].load_laps()
winners = {'Driver':['HAM','BOT','VER','PER','NOR','RIC','STR','VET','ALO','OCO','LEC','SAI','GAS','TSU','RAI','GIO','MAZ','MSC','RUS','LAT'],'1st':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'2nd':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'3rd':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
for i in range(0,16):
  result = season[i].results
  index = winners['Driver'].index(result[0]['Driver']['code'])
  winners['1st'][index]=winners['1st'][index]+1
  index = winners['Driver'].index(result[1]['Driver']['code'])
  winners['2nd'][index]=winners['2nd'][index]+1
  index = winners['Driver'].index(result[2]['Driver']['code'])
  winners['3rd'][index]=winners['3rd'][index]+1
multD = pd.DataFrame(winners)
print(multD)


drivers = multD['Driver'].array
wins = multD['1st'].array
seconds = multD['2nd'].array

x = np.arange(len(drivers))
width=0.4

fig, ax = plt.subplots()
rects1 = ax.bar((x-width*2)/3, wins, width, label="Wins")
rects2 = ax.bar(x, seconds, width, label="Second Place")

ax.set_ylabel('# of times position acheived')
ax.set_title("Frequency of Positions Scored by Drivers")
ax.set_xticks(x)
ax.set_xticklabels(drivers, fontsize=7)
ax.legend()   
ax.bar_label(rects1, padding=width*10)
ax.bar_label(rects2, padding=width*10)
fig.tight_layout()

plt.show()