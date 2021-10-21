#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fastf1 as ff1
import fastf1.plotting as ff1plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# We create a cache so that our program will load faster in the future(thanks ff1!)

# In[2]:


ff1.Cache.enable_cache("cache/")


# Now we get all races from the 2021 season so far, and store them in a array called "races"

# In[3]:


races = []


# Now we collect all the ones out so far, so races 1-17. We also load lap times if not already cached, as this will help us later.

# In[4]:


for i in range(1,17):
    races.append(ff1.get_session(2021, i, 'R'))
    races[i-1].load_laps()


# Create a dictionary to hold winners from each session

# In[5]:


winners = {'Driver':['HAM','BOT','VER','PER','NOR','RIC','STR','VET','ALO','OCO','LEC','SAI','GAS','TSU','RAI','GIO','MAZ','MSC','RUS','LAT'],'1st':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'2nd':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'3rd':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}


# Now we collect our data

# In[6]:


for race in races:
    results = race.results
    index = winners['Driver'].index(results[0]['Driver']['code'])
    winners['1st'][index]=winners['1st'][index]+1
    index = winners['Driver'].index(results[1]['Driver']['code'])
    winners['2nd'][index]=winners['2nd'][index]+1
    index = winners['Driver'].index(results[2]['Driver']['code'])
    winners['3rd'][index]=winners['3rd'][index]+1


# Now we convert that data into a data frame to make it easier on us

# In[7]:


dframe = pd.DataFrame(winners)
print(dframe)


# Now that we have our data, we can begin setting up our graph.
# 
# First, we initialize our arrays to actually be used in the creation of the graph

# In[8]:


drivers=dframe.Driver
first=dframe['1st'].array
second=dframe['2nd'].array
third=dframe['3rd'].array


# Second, we determine the width of our bars and the spacing nessesary between them

# In[9]:


x = np.arange(len(drivers))
width = 0.3
constshift=width/2


# No clue as to what the following does

# In[10]:


fig, ax = plt.subplots()
plt.figure(figsize=(20, 3))
rects1 = ax.bar((x-width)-constshift, first, width, label='Wins', align='edge')
rects2 = ax.bar(x-constshift, second, width, label='Second Place',align='edge')
rects3 = ax.bar((x+width)-constshift, third, width, label="Third Place",align='edge')
ax.set_ylabel('# of times position acheived')
ax.set_title("Frequency of Positions Scored by Drivers")
ax.set_xticks(x)
ax.set_xticklabels(drivers, fontsize=7)
ax.legend()   


# Now that we've done that, lets graph the points by round between Verstappen and Hamilton

# In[11]:


switcher = {
    1:25,
    2:18,
    3:15,
    4:12,
    5:10,
    6:8,
    7:6,
    8:4,
    9:2,
    10:1
}


# In[12]:


points={'Race':['BRN','ITA','POR','ESP','MON','AZB','FRA','AUT','AUT2','GBR','HUN','BEL','NED','ITA2','RUS','TUR'],'Verstappen':[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],'Hamilton':[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
for i in range(0, len(races)):
    race = races[i]
    position = race.get_driver('VER').position
    #sum up to that point
    if(i!=0):
        points['Verstappen'][i]+=points['Verstappen'][i-1]
        points['Hamilton'][i]+=points['Hamilton'][i-1]
    if(i==11):#fuck off spa-francorchamps(got flooded :-|) 
        points['Verstappen'][i]+=12.5
        points['Hamilton'][i]+=7.5
        continue
    try:
        fastest = races[i].laps.pick_fastest().DriverNumber
    except:
        print(races[i].weekend.name+" "+str(i))
    if(i==9):#british grand prix weird points
        points['Verstappen'][i]+=3
        points['Hamilton'][i]+=27
        continue
    if(i==13):#itialian grand prix weird points
        points['Verstappen'][i]+=2
        points['Hamilton'][i]+=0
        continue
    if(position<11):
        points['Verstappen'][i]+=switcher.get(position)
        if(fastest=='33'and i!=2):
            points['Verstappen'][i]+=1
    position = race.get_driver('HAM').position
    if(position<11):
        points['Hamilton'][i]+=switcher.get(position)
        if(fastest=='44'):
            points['Hamilton'][i]+=1
    
dframe_points = pd.DataFrame(points)
print(dframe_points)


# Now, we graph these points. This is pretty easy.

# In[14]:


plt.plot(points['Verstappen'], color = ff1plot.team_color('RBR'))
plt.plot(points['Hamilton'], color=ff1plot.team_color('MER'))
plt.xticks(np.arange(len(points['Race'])),points['Race'])
plt.title("Verstappen vs. Hamilton")
plt.show()



# %%
