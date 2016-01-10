+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "wawa mining"

+++



It’s the experiment of Introduction to Data Mining. All by tobe, kiic and Jun.

<pre><code>
import math

def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]:
  if item in prefs[p2]: si[item]=1

  n=len(si)

  if n==0:
    return 1

  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

  num=pSum-(sum1*sum2/n)
  den=math.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0:
    return 0

  r=num/den

  return r

def getPredictRankings(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}

  result = {}

  for other in prefs:
    if other==person:
      continue

  sim = similarity(prefs, person, other)

  if sim<=0:
    continue
   for item in prefs[other]:
     if item not in prefs[person] or prefs[person][item]==0:
     totals.setdefault(item, 0)
     totals[item] += prefs[other][item]*sim

  simSums.setdefault(item, 0)
  simSums[item] += sim

  for item,total in totals.items():
    result[item] = round(total/simSums[item])

  return result

def calculateMAE(prefs, predict, result):
  total = 0
  counter = 0

  for reader in result:
    readers = result.get(reader)
  for film in readers:
   score = readers.get(film)

  if reader in predict:
    if film in predict[reader]:
      total += abs(float(score)-float(predict[reader][film]))
      counter += 1
    else:
    total += abs(float(score) - sum([prefs[reader][filmName] for filmName in prefs[reader]]) / len(prefs[reader]))
    counter += 1
    else:
      #no data here, so...
      pass

  return float(total)/counter

import time
startTime = time.time()

critics = {}
predict = {}
result = {}

trainFile = open("80train.txt", "r")
try:
  for line in trainFile:
    items = line.split("\t")
    if critics.has_key(items[0]):
      critics[items[0]][items[1]] = float(items[2])
    else:
    critics[items[0]] = {items[1]:float(items[2])}
  finally:
  trainFile.close()

testFile = open("test.txt", "r")
try:
  n for line in testFile:
  items = line.split("\t")
  if result.has_key(items[0]):
    result[items[0]][items[1]] = float(items[2])
  else:
    result[items[0]] = {items[1]:float(items[2])}
finally:
  testFile.close()

for everybody in critics:
  predict[everybody] = getPredictRankings(critics, everybody, sim_pearson)

mae = calculateMAE(critics, predict, result)
print "MAE :", mae
#MAE : 0.771823562626

endTime = time.time()
print "Total time : %f" % (endTime - startTime)
#Total time : 63.313000
</code></pre>

实现步骤：

1. 文件读入，将训练集和测试集的数据全部读入内存，保存到dictionary的数据结构里面。
2. 根据Pearson算法计算出每两个用户之间的相似度。
3. 以用户之间的相似度为权重，乘以该用户的评分来预测每一位用户对所有电影的评分（若用户已对该电影评分则无需预测）。
4. 计算MAE。
5. 如果测试集的电影没有出现在训练集中，则以测试用户的平均评分来预测。
6. 将结果输出到result.txt中。

实验结果：  
MAE： 0.771823562626  
运行时间： 63.313000秒（实验室机器）  