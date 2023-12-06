import numpy as np
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
times = [int(time) for time in lineLst[0].split(": ")[1].split(" ") if time != ""]
dists = [int(dist) for dist in lineLst[1].split(": ")[1].split(" ") if dist != ""]
races = [(times[i], dists[i]) for i in range(len(times))]

amnts = []
for race in races:
  cumDist = []
  for time in range(1, race[0] + 1):
    cumDist.append(time*(race[0]-time))
  amnt = sum([dist > race[1] for dist in cumDist])
  amnts.append(amnt)
print(np.prod(amnts))

bigTime = int("".join([str(time) for time in times]))
bigDist = int("".join([str(dist) for dist in dists]))
cumDist = []
for time in range(1, bigTime + 1):
  cumDist.append(time*(bigTime-time))
amnt = sum([dist > bigDist for dist in cumDist])
print(amnt)