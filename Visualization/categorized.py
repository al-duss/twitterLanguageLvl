import matplotlib.pyplot as plt
import numpy as np
import os

categories = ['Musicians', 'Politicians', 'Athletes',
'News Stations', 'Businesses', 'Education', 'Entertainers']
dir_path = os.path.dirname(os.path.realpath(__file__))

#Category number
def plot(catNo):
  results = {}
  with open(dir_path+"/results.txt", "r") as f:
    for line in f:
      res = line.split()
      results[res[0]] = [res[1],res[2]]
    f.close()

  colorWheel = ['r','b','g','c','m','y','black']
  x = []
  y = []
  labels = []
  colors = []


  with open(dir_path+"/../list.txt") as r:
    i = 0
    lines = r.read().splitlines()
    for line in lines:
      if len(line) == 0:
        i = (i + 1)
      elif i == catNo:
        labels.append(line)
        x.append(results[line][0])
        y.append(results[line][1])

  plt.scatter(x, y, c=colorWheel[catNo])

  for label, a, b, in zip(labels,x,y):
    plt.annotate(
      label,
      xy=(a,b),va='bottom')

  plt.show()

if __name__ == '__main__':
  import argparse
  ap = argparse.ArgumentParser(description='Process the category Name')
  ap.add_argument('name', help='Category Name', nargs='?', default="nostring")
  args = ap.parse_args()
  catNo = categories.index(args.name.title())
  if(args.name != "nostring"):
    plot(catNo)