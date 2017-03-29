import os

def analyze():
  with open ('results.txt', 'w') as w:
    for root, dirs, files in os.walk("./../MapReduce"):
      for file in files:
        if file.endswith("part-r-00000"):
          with open(os.path.join(root,file),'r') as f:
            count = countWords(f.readlines())
            f.close()
            w.write(os.path.join(root,file).split('/')[3]+" "+str(count) +'\n')
    w.close()

def countWords(lines):
  count = 0
  for line in lines:
    if(line.split()[1] == str(1)):
      count += 1
  return count

