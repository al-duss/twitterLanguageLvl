#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
results = {}
with open(dir_path+"/results.txt", "r") as f:
  for line in f:
    res = line.split()
    results[res[0]] = res[4]
  f.close()

colorWheel = ['r','b','g','c','m','y','black']
categories = ['Musicians', 'Politicians', 'Athletes',
'News Stations', 'Businesses', 'Education', 'Entertainers']

patches = []
for i,category in enumerate(categories):
  patches.append(mpatches.Patch(color=colorWheel[i],label=category))

x = []
labels = []
colors = []


with open(dir_path+"/../list.txt") as r:
  i = 0
  lines = r.read().splitlines()
  for line in lines:
    if len(line) == 0:
      i = (i + 1)%7
    else:
      labels.append(line)
      x.append(results[line])
      colors.append(colorWheel[i])

fig, ax = plt.subplots()
ax.bar(range(0,len(labels)),x,color=colors)
ax.set_xticks(range(0,len(labels)))
ax.set_xticklabels(labels, rotation='vertical')
ax.legend(handles=patches,framealpha=1.0)
plt.title("Word count per different word")
plt.show()