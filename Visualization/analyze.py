import os

def analyze():
  with open ('results.txt', 'w') as w:
    for root, dirs, files in os.walk("./../MapReduce/results"):
      for file in files:
        if file.endswith("part-r-00000"):
          with open(os.path.join(root,file),'r') as f:
            count = countWords(f.readlines())
            f.close()
            w.write(os.path.join(root,file).split('/')[3]+" "+str(count['total'])+" "+str(count['diff']) +'\n')
    w.close()

def countWords(lines):
  count = {'total':0,'diff':0}
  for line in lines:
    value = int(line.split()[1])
    if(value > 0):
      count['diff'] += 1
      count['total'] += value

  return count

