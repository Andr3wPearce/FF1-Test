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
dframe = pd.DataFrame(winners)
print(dframe)


drivers=dframe.Driver
first=dframe['1st'].array
second=dframe['2nd'].array
third=dframe['3rd'].array

x = np.arange(len(drivers))
width = 0.3
constshift=width/2
plt.figure(figsize=(20, 3))
fig, ax = plt.subplots()

rects1 = ax.bar((x-width)-constshift, first, width, label='Wins', align='edge')
rects2 = ax.bar(x-constshift, second, width, label='Second Place',align='edge')
rects3 = ax.bar((x+width)-constshift, third, width, label="Third Place",align='edge')
ax.set_ylabel('# of times position acheived')
ax.set_title("Frequency of Positions Scored by Drivers")
ax.set_xticks(x)
ax.set_xticklabels(drivers, fontsize=7)
ax.legend()   


plt.show()