import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


results = {}
with open("results.txt", "r") as f:
  for line in f:
    res = line.split()
    results[res[0]] = [res[1],res[2]]
  f.close()

colorWheel = ['r','b','g','c','m','y','black']
categories = ['Musicians', 'Politicians', 'Athletes',
'News Stations', 'Businesses', 'Education', 'Entertainers']
patches = []
for i,category in enumerate(categories):
  patches.append(mpatches.Patch(color=colorWheel[i],label=category))

x = []
y = []
labels = []
colors = []

with open("list.txt") as r:
  i = 0
  lines = r.read().splitlines()
  for line in lines:
    if len(line) == 0:
      i = (i + 1)%7
    else:
      labels.append(line)
      x.append(results[line][0])
      y.append(results[line][1])
      colors.append(colorWheel[i])

plt.scatter(x, y, c=colors, label=categories)
plt.legend(handles=patches,bbox_to_anchor=(1.1, 1.05),framealpha=1.0)

plt.show()